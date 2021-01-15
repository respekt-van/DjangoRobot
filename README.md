# Robot
# Python implementation of YOLO v3 using OpenCV

## Overview

This program performs object detection on input images of your choice. I employed YOLO v3 model trained on COCO data set. The model is implemented using functions provided by OpenCV library.

## Source files

 - `main.py` : Python file. This is the main file for this program.
 - `coco.names` : Txt file. This contains names.
 - `Neural.py` : Python file. Neural file.
 - `Robot.py` : Python file. Robot logic file.
## Input files

 - `yolo/yolov3-320.cfg` : YOLO v3 config file
 - `yolo/yolov3-320.weights` : YOLO v3 weights file

These files were obtained by following the instruction described in **Darknet**'s ["YOLO: Real-Time Object Detection"](https://pjreddie.com/darknet/yolo/)

## Version
  - Django 3.1.5
  - Django Rest Framework
  - Python 3
  - Numpy 1.14.3
  - OpenCV 4.2

## Usage

After you download those files above, simply execute the command below in the directory where 'yolo_od.py' is located.
```
 > main.py
```

Before you run this command, you need to prepare image files you want to try out. It's possible to specify multiple image files. If you do so, it performs object detection on each image file in a row.

When you run this program, the image with the bounding boxes is shown in the window, and you can see the result. To close the output image, you need to put the mouse pointer on the window and press any key. If you specify multiple image files, the output images are shown one by one.
