#! /usr/bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from fenPrincipale import fenPrincipale
import sys, os

def main(args):
    a=QApplication(args)
    splashImage = QPixmap('logo.png')
    splash = QSplashScreen(splashImage, Qt.WindowStaysOnTopHint)
    splash.setMask(splashImage.mask())
    splash.show()
    configFic = open('courant.rmc', 'r')
    contenuConfig = configFic.readlines()
    configFic.close()
    theme = str(contenuConfig[3]).split("=")[1]
    FS = str(contenuConfig[2]).split("=")[1]
    if theme == 'Moderne\n':
        theme='Cleanlooks'
    else:
        theme='Motif'
    f=fenPrincipale()
    if FS=="1\n":
        f.showFullScreen()
    QApplication.setStyle(QStyleFactory.create(theme))
    f.show()
    splash.finish(f)
    r=a.exec_()
    return r

if __name__ == '__main__':
    main(sys.argv)
