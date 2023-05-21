import numpy as np
import cv2
import tensorflow as tf
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import threading

from sign import sign
from FACIAL import FACIAL

if __name__ == '__main__':
    t1 = threading.Thread(target = sign)
    t2 = threading.Thread(target= FACIAL)
    t1.start()
    t2.start()
