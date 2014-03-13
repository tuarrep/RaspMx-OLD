#! /usr/bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from fenPrincipale import fenPrincipale
import sys, os

def main(args):
    a=QApplication(args)
    QApplication.setStyle(QStyleFactory.create("Plastique"))
    splashImage = QPixmap('logo.png')
    splash = QSplashScreen(splashImage, Qt.WindowStaysOnTopHint)
    splash.setMask(splashImage.mask())
    splash.show()
    f=fenPrincipale()
    f.show()
    splash.finish(f)
    r=a.exec_()
    return r
if __name__ == '__main__':
    main(sys.argv)
