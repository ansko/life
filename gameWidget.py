#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lifeWidget import lifeWidget
from options import options

class gameWidget(QWidget):
    o = options()

    def __init__(self):
        super().__init__()

        self.makeWidget()

    def makeWidget(self):
        b = QWidget()
        l = lifeWidget(self.o)
        l.setFixedSize(l.width(), l.height())

        startButton = QPushButton("Start")
        startButton.clicked.connect(l.startGame)
        startButton.setFixedSize(self.o.getButtonWidth(), 
                                 self.o.getButtonHeight())

        pauseButton = QPushButton("Pause")
        pauseButton.clicked.connect(l.pauseGame)
        pauseButton.setFixedSize(self.o.getButtonWidth(), 
                                 self.o.getButtonHeight())

        clearButton = QPushButton("Clear Field")
        clearButton.clicked.connect(l.makeEmptyField)
        clearButton.setFixedSize(self.o.getButtonWidth(),
                                 self.o.getButtonHeight())

        randomFieldButton = QPushButton("Generate \nRandom Field")
        randomFieldButton.clicked.connect(l.makeRandomField)
        randomFieldButton.setFixedSize(self.o.getButtonWidth(),
                                       self.o.getButtonHeight())

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(self.close)
        exitButton.setFixedSize(self.o.getButtonWidth(),
                                self.o.getButtonHeight())

        gliderButton = QPushButton("Add Glider")
        gliderButton.clicked.connect(lambda: l.changeMode('addingGlider'))
        gliderButton.setFixedSize(self.o.getButtonWidth(),
                                  self.o.getButtonHeight())

        #x, y resize
        #self.t = QLineEdit()
        #self.t.setFixedSize(50, 100)

        v = QVBoxLayout(b)
        v.setSpacing(0)
        v.addWidget(startButton, 0)
        v.addWidget(pauseButton, 0)
        v.addWidget(clearButton)
        v.addWidget(randomFieldButton)
        v.addWidget(gliderButton)
        v.addWidget(exitButton)

        b.setLayout(v)
        h = QHBoxLayout()
        self.setLayout(h) 
        h.addWidget(b)
        h.addWidget(l)
        self.setFixedSize(l.width() + self.o.getButtonWidth() + 100, #???
                          l.height() + self.o.getButtonHeight())

    def updateSizeX(self, x):
        self.o.setSizeX(int(x))

    def updateSizeY(self):
        self.o.setSizeY(int(y))
