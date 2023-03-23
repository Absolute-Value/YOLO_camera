import argparse, os
import time, datetime
import torch
import cv2
from logger import get_logger

WIDTH = 960
HEIGHT = 720

parser = argparse.ArgumentParser(description='test_yolo')
parser.add_argument('--interval', type=int, default=10)
parser.add_argument('--output_img_path', type=str, default='origins')
parser.add_argument('--output_path', type=str, default='outputs')
parser.add_argument('--only_human', action='store_true')
args = parser.parse_args()

logger = get_logger('./', 'anno.log')

model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
if args.only_human:
    model.classes = [0]

while True:
    start_time = time.time()
    
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    
    # キャプチャが成功したかどうかを確認する
    if not cap.isOpened():
        print("カメラが見つかりません")
    
    # ビデオストリームを取得し、ウィンドウに表示する
    ret, frame = cap.read()

    if not ret:
        print("ビデオストリームが停止しました")

    dt_now = datetime.datetime.now()
    dt_time = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    print(dt_time)
    
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = model(img)
    
    if len(result.pred[0]>0):
        img_day_dir, img_name = dt_time.split(' ')
        img_name = f'{img_name}.png'
        result.files[0] = img_name
        logger.info(result.files[0])
        os.makedirs(os.path.join(args.output_img_path, img_day_dir), exist_ok=True)
        cv2.imwrite(os.path.join(args.output_img_path, img_day_dir, img_name), frame)
        for pred in result.pred[0]:
            x1, y1, x2, y2, conf, obj_id = pred.to('cpu').detach().numpy()
            obj_name = result.names[int(obj_id)]
            logger.info(f'{x1} {y1} {x2} {y2} {conf} {int(obj_id)} {obj_name}')
        result.save(save_dir=os.path.join(args.output_path, img_day_dir), exist_ok=True)
    
    cap.release()
    
    elasp_time = time.time() - start_time
    # print(elasp_time)
    
    time.sleep(max(0,args.interval-elasp_time))