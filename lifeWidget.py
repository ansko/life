#!/usr/bin/env python3

import random
import copy

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class lifeWidget(QWidget):
    def __init__(self, o):
        super().__init__()

        self.o = o

        self.resize(self.o.getSquareSize() * self.o.getHorizontalSize(), 
                    self.o.getSquareSize() * self.o.getVerticalSize())

        self.initRandomField()

        self.timer = QTimer()

        self.mode = None

        self.setMouseTracking(True)

    def startGame(self):
        self.timer.timeout.connect(self.updateField)
        self.timer.start(self.o.getUpdateTime())

    def pauseGame(self):
        self.timer.timeout.connect(self.updateField)
        self.timer.stop()

    def initRandomField(self):
        l = self.o.getSquareSize()
        xs = self.o.getHorizontalSize()
        ys = self.o.getVerticalSize()
        self.field = []
        line = []
        for x in range(xs):
            line = []
            for y in range(ys):
                a = random.randint(0, self.o.getRandMin())
                b = random.randint(0, self.o.getRandMax())
                if a > b:
                    line.append('alive')
                else:
                    line.append('dead')
            self.field.append(copy.deepcopy(line))

    def updateField(self):
        l = self.o.getSquareSize()
        xs = self.o.getHorizontalSize()
        ys = self.o.getVerticalSize()
        newField = copy.deepcopy(self.field)
        for x in range(0, xs):
            for y in range(0, ys):
                neighbours = 0
                disps_x = []
                disps_y = []
                if x == 0:
                    disps_x = [0, 1]
                elif x == xs - 1:
                    disps_x = [-1, 0]
                else:
                    disps_x = [-1, 0, 1]
                if y == 0:
                    disps_y = [0, 1]
                elif y == ys - 1:
                    disps_y = [-1, 0]
                else:
                    disps_y = [-1, 0, 1]
                for dx in disps_x:
                    for dy in disps_y:
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[x + dx][y + dy] in ['alive',
                                                          'alive_onblur']:
                            neighbours += 1
                if neighbours == 3:
                    newField[x][y] = 'alive'
                elif neighbours == 2 and newField[x][y] in ['alive',
                                                            'alive_onblur']:
                    newField[x][y] = 'alive'
                else:
                    newField[x][y] = 'dead'
        self.field = newField
        self.update()

    def paintEvent(self, event):
        l = self.o.getSquareSize()
        xs = self.o.getHorizontalSize()
        ys = self.o.getVerticalSize()

        rp = QPainter()
        rp.begin(self)
        
        for x in range(xs):
            for y in range(ys):
                if self.field[x][y] == 'alive':
                    rp.setBrush(QBrush(QColor(0, 255, 0)))
                    rp.drawRect(x * l, y * l, l, l)
                elif self.field[x][y] == 'dead':
                    rp.setBrush(QBrush(QColor(0, 0, 0)))
                    rp.drawRect(x * l, y * l, l, l)
                elif self.field[x][y] == 'alive_onblur':
                    rp.setBrush(QBrush(QColor(255, 255, 0)))
                    rp.drawRect(x * l, y * l, l, l)
                elif self.field[x][y] == 'dead_onblur':
                    rp.setBrush(QBrush(QColor(133, 133, 133)))
                    rp.drawRect(x * l, y * l, l, l)

        rp.end()

    def makeEmptyField(self):
        l = self.o.getSquareSize()
        xs = self.o.getHorizontalSize()
        ys = self.o.getVerticalSize()

        for x in range(xs):
            for y in range(ys):
                self.field[x][y] = 'dead'

        self.update()

    def makeRandomField(self):
        self.initRandomField()
        self.update()

    def mouseMoveEvent(self, event):
        active_x = int(event.x() / self.o.getSquareSize())
        active_y = int(event.y() / self.o.getSquareSize())
        self.highlightCell(active_x, active_y)

    def changeMode(self, mode=None):
        self.mode = mode
        if mode == 'addingGlider':
            print('Adding gliders mode')

    def addGlider(self, x=0, y=0):
        if (x < 2 or y < 2 or
                x > self.o.getHorizontalSize() - 3 or
                y > self.o.getVerticalSize() - 3):
            print('Not enough space here for glider and emptiness')
            return None

        for dx in [-2, -1, 0, 1, 2]:
            self.field[x + dx][y - 2] = 'dead'
            self.field[x + dx][y + 2] = 'dead'
        for dy in [-1, 0, 1]:
            self.field[x + 2][y + dy] = 'dead'
            self.field[x - 2][y + dy] = 'dead'
        self.field[x + 1][y - 1] = 'alive'
        self.field[x + 1][y ] = 'dead'
        self.field[x + 1][y + 1] = 'dead'
        self.field[x][y - 1] = 'dead'
        self.field[x][y] = 'alive'
        self.field[x][y + 1] = 'alive'
        self.field[x - 1][y - 1] = 'alive'
        self.field[x - 1][y] = 'alive'
        self.field[x - 1][y + 1] = 'dead'
        self.update()

    def mousePressEvent(self, event):
        if self.mode is None:
            return None
        if self.mode == 'addingGlider':
            #print('Adding gli
            #pass
            self.addGlider(int(event.x() / self.o.getSquareSize()),
                           int(event.y() / self.o.getSquareSize()))

    def highlightCell(self, active_x, active_y):
        for x in range(self.o.getHorizontalSize()):
            for y in range(self.o.getVerticalSize()):
                if self.field[x][y] == 'alive_onblur':
                    self.field[x][y] = 'alive'
                elif self.field[x][y] == 'dead_onblur':
                    self.field[x][y] = 'dead'
        if self.field[active_x][active_y] == 'alive':
            self.field[active_x][active_y] = 'alive_onblur'
        elif self.field[active_x][active_y] == 'dead':
            self.field[active_x][active_y] = 'dead_onblur'
        self.update()
