# カメラ映像からYOLOで物体検出
カメラの映像を用いて，YOLOで物体検出します．


## ファイルの説明 (.py)

### test_yolov5.py
Pathを与えた画像に対し，YOLOで物体検出して出力

### camera_yolov5.py
カメラの映像を用いて，YOLOで物体検出して出力

### logger.py
ログ出力用


## ファイルの説明 (.ipynb)

### camera.ipynb
カメラの映像を逐次表示

### camera_yolov5.ipynb
カメラの映像を用いて，YOLOv5でDetectionを逐次行なう

### camera_yolov8.ipynb
カメラの映像を用いて，YOLOv8でDetectionを逐次行なう（実装途中）


## ヒント
* [YOLOの詳細](https://github.com/ultralytics/yolov5)
* [resultで出力できるもの](https://github.com/ultralytics/yolov5/blob/master/models/common.py)