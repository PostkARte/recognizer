import cv2
import imutils
import recognizer.core.helper as h
import sys

class PostCardMatcher:

    def findPicture(self, live_picture):
        picture = imutils.resize(live_picture, height=500)
        desLive = h.extractFeatures(picture)
        flann = h.getFlannMatcher()
        return self.findBestMatch(desLive, flann)

    def findBestMatch(self, desLive, flann):
        global features
        bestIndex = 0;
        bestMatch = 0;

        for featureName in h.loadFeatureNames():
            feature = h.loadFeature(featureName)
            matches = flann.knnMatch(feature, desLive, k=2)

            goodMatches = 0;
            for i, (m, n) in enumerate(matches):
                if m.distance < 0.7 * n.distance:
                    goodMatches += 1

            if (goodMatches > 20 and bestMatch < goodMatches):
                bestIndex = h.splitFeaturename(featureName)
                bestMatch = goodMatches


        return bestIndex
