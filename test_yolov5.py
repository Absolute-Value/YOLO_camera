import argparse, os
import torch
import cv2

parser = argparse.ArgumentParser(description='test_yolo')
parser.add_argument('--img_path', type=str, default='/data/dataset/jikuya/imagenet/val/n03706229/ILSVRC2012_val_00001229.JPEG')
parser.add_argument('--output_img_path', type=str, default='origins')
parser.add_argument('--output_path', type=str, default='outputs')
args = parser.parse_args()

os.makedirs(args.output_img_path, exist_ok=True)
img_name = args.img_path.split('/')[-1]

model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
img = cv2.imread(args.img_path)
cv2.imwrite(os.path.join(args.output_img_path, img_name), img)

result = model(img)
result.files[0] = img_name
print(result.files[0])
if len(result.pred[0]>0):
    for pred in result.pred[0]:
        x1, y1, x2, y2, conf, obj_id = pred.to('cpu').detach().numpy()
        obj_name = result.names[int(obj_id)]
        print(x1, y1, x2, y2, conf, int(obj_id), obj_name)
    result.save(save_dir=args.output_path, exist_ok=True)