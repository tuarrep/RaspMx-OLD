#! /usr/bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from fenPrincipale import fenPrincipale
import sys, os

def main(args):
    a=QApplication(args)
    QApplication.setStyle(QStyleFactory.create("Cleanlooks"))
    f=fenPrincipale()
    f.show()
    r=a.exec_()
    return r
if __name__ == '__main__':
    main(sys.argv)
