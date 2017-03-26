#!/usr/bin/env python3

import sys
import copy
import random

import pprint
pprint = pprint.PrettyPrinter(indent=1).pprint

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gameWidget import gameWidget

def main(): #life
    app = QApplication(sys.argv)

    w = gameWidget()
    w.show()

    sys.exit(app.exec_())

main()
