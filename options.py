#!/usr/bin/env python3

class options():
    def __init__(self):
        self.squareSize = 10
        self.verticalSize = 100
        self.horizontalSize = 100
        self.buttonWidth = 100
        self.buttonHeight = 50
        self.randMin = 600
        self.randMax = 900
        self.updateTime = 10
    def setVerticalSize(self, y):
        self.verticalSize = int(y)
    def setHorizontalSize(self, z):
        self.horizontalSize = int(x)
    def getSquareSize(self):
        return int(750 / max(self.verticalSize, self.horizontalSize))
        #return self.squareSize
    def getVerticalSize(self):
        return self.verticalSize
    def getHorizontalSize(self):
        return self.horizontalSize
    def getButtonWidth(self):
        return self.buttonWidth
    def getButtonHeight(self):
        return self.buttonHeight
    def getRandMin(self):
        return self.randMin
    def getRandMax(self):
        return self.randMax
    def getUpdateTime(self):
        return self.updateTime
