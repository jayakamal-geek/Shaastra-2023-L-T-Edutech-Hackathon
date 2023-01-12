import cv2
import numpy as np



def readimg(src, target_size=(224,224,3)):
    dst = cv2.resize(src, target_size)
    return dst

def preprocess(vec, reshape_=(224,224,3)):
    vec.reshape(reshape_)
    return vec