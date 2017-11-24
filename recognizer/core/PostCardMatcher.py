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
        picture = imutils.resize(live_picture, height=1000)
        desLive = h.extractFeatures(picture)
        flann = h.getFlannMatcher()
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
        return bestIndex