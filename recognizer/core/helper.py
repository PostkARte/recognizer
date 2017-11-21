import cv2
import numpy as np
import os

FEATURE_FOLDER = "Features"
FLANN = None


def extractFeatures(live_picture):
    sift = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift.detectAndCompute(live_picture, None)
    return des2


def getFlannMatcher():
    global FLANN
    if (FLANN is None):
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        FLANN = cv2.FlannBasedMatcher(index_params, search_params)
    return FLANN


def loadFeature(number):
    return np.load(FEATURE_FOLDER + "/" + str(number) + ".npy")

def loadAllFeatures():
    features = {}
    featureNames = [f for f in os.listdir(FEATURE_FOLDER) if os.path.isfile(os.path.join(FEATURE_FOLDER, f))]
    for x in featureNames:
        file = os.path.splitext(x)
        features[file[0]] = loadFeature(file[0])
    return features

def getFeatureCount():
    return len([f for f in os.listdir(FEATURE_FOLDER)
                if os.path.isfile(os.path.join(FEATURE_FOLDER, f))]) + 1
