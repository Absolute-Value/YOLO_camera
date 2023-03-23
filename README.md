# カメラ映像からYOLOで物体検出
カメラの映像を用いて，YOLOで物体検出します．

## ファイルの説明

### test_yolov5.py
Pathを与えた画像に対し，YOLOでDetectionして出力

### camera_yolov5.py
カメラで認識し，YOLOでDetectionして出力

### logger.py
ログ出力用

## ヒント
* [YOLOの詳細](https://github.com/ultralytics/yolov5)
* [resultで出力できるもの](https://github.com/ultralytics/yolov5/blob/master/models/common.py)