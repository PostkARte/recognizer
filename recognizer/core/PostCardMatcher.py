import cv2
import imutils
import recognizer.core.helper as h
import sys

class PostCardMatcher:
    features = {}

    def __init__(self):
        self.reloadFeatures()

    def reloadFeatures(self):
        global features
        features = h.loadAllFeatures()

    def findPicture(self, live_picture):
        print('1')
        picture = imutils.resize(live_picture, height=500)
        print('2')
        desLive = h.extractFeatures(picture)
        print('3')
        flann = h.getFlannMatcher()
        print('4')
        return self.findBestMatch(desLive, flann)

    def findBestMatch(self, desLive, flann):
        global features
        bestIndex = 0;
        bestMatch = 0;

        for id, feature in features.items():
            matches = flann.knnMatch(feature, desLive, k=2)
            goodMatches = 0;
            for i, (m, n) in enumerate(matches):
                if m.distance < 0.7 * n.distance:
                    goodMatches += 1

            if (bestMatch < goodMatches):
                bestIndex = id
                bestMatch = goodMatches
        print('5')
        return bestIndex
