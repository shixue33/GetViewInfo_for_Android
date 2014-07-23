# -*- coding: utf-8 -*-

from PyQt4 import QtGui

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self):
        self.t1 = QtGui.QLabel()
        self.t1.setText('author:shixue33')
        self.t2 = QtGui.QLabel()
        self.t2.setText('mailto:shixue33@qq.com')
        self.layout=QtGui.QGridLayout()
        self.layout.addWidget(self.t1,0,0)
        self.layout.addWidget(self.t2,1,0)
        self.setLayout(self.layout)
        self.setWindowTitle('about')
        
        
        