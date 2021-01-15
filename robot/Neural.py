import numpy as np
import cv2
from math import sqrt
from .Robot import Manipulator
from .Robot import Wannamore

# configuration
cap = cv2.VideoCapture(0)
whT = 320
confThreshold = 0.2
nms_threshold = 0.3

classesFile = 'C:/Users/Respe/PycharmProjects/RobotFinal/Django/robot/coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'C:/Users/Respe/PycharmProjects/RobotFinal/Django/robot/yolov3-320.cfg'
modelWeights = 'C:/Users/Respe/PycharmProjects/RobotFinal/Django/robot/yolov3-320.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

class Neural:
    n_ame = ''
    w = 0
    h = 0
    BottleRange = 0
    HumanRange = 0

    def findObjects(outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []

        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w,h = int(det[2]*wT), int(det[3]*hT)
                    x,y = int((det[0]*wT) -w/2), int(det[1]*hT -h/2)
                    Neural.w = w
                    Neural.h = h
                    bbox.append([x,y,w,h])
                    classIds.append(classId)
                    confs.append(float(confidence))
                    Neural.n_ame = ''
                    Neural.BottleInTarget = False
        indices = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nms_threshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x,y,w,h = box[0], box[1], box[2], box[3]
            if classNames[classIds[i]] == 'bottle' and not Manipulator.busy:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                Neural.n_ame = classNames[classIds[i]].upper()
                d = sqrt(w ** 2 + h ** 2)
                srange = 125 * 82 / d
                Neural.BottleRange = srange
                cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(Neural.BottleRange)}cm',
                            (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
            elif classNames[classIds[i]] == 'person' and Manipulator.busy:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                Neural.n_ame = classNames[classIds[i]].upper()
                d = sqrt(w ** 2 + h ** 2)
                srange = 300 * 80 / d
                Neural.HumanRange = srange
                Wannamore.dontwant = True
                cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(srange)}cm',
                            (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
