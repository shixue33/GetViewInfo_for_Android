# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame2.ui'
#
# Created: Tue Jul 08 00:21:26 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import glob
import os.path
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(757, 540)
        #Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(Frame)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 10, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.graphicsView = QtGui.QLabel(Frame)
        self.graphicsView.setGeometry(QtCore.QRect(150, 40, 311, 481))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        
        self.graphicsView.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.image = QtGui.QImage()
        self.listWidget = QtGui.QListWidget(Frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 131, 481))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.treeWidget = QtGui.QTableWidget(Frame)
        self.treeWidget.setGeometry(QtCore.QRect(470, 40, 281, 231))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        
        self.treeWidget.verticalHeader().setVisible(False)
        self.treeWidget.horizontalHeader().setVisible(False)
        
        self.tableWidget = QtGui.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(470, 280, 281, 241))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.pushButton.setText(_translate("Frame", "开始", None))
        self.pushButton_2.setText(_translate("Frame", "检测", None))
        self.pushButton_3.setText(_translate("Frame", "载入本地", None))
        
        self.pushButton_5.setText(_translate("Frame", "关于", None))
    #刷新文件列表
    def initList(self,cmd_test):
        print 'initlist'
        #list = QtCore.QStringList()
        #list.append('hellohellohello')
        #list.append(str(123456789))
        self.listWidget.clear()
        temp = ''
        temp2 = ''
        self.files = []
        for temp in glob.glob('res/{}/*.xml'.format(cmd_test.current_dir)):
            (temp2,temp)=os.path.split(temp)            
            self.files.append(temp)
        self.listWidget.insertItems(0,self.files)
        
    def loadPic(self,filename):
        if self.image.load(filename):
            self.image = self.image.scaledToHeight(self.graphicsView.height())
            self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(self.image))       
        
    #刷新文件内的属性树
    def initTree(self,xml_analysis):
        view_simple_name = xml_analysis.get_simple_name()
        self.treeWidget.clear()
        self.treeWidget.clearContents()
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setRowCount(len(view_simple_name))
        num = 0
        for view in view_simple_name:
            temp = '{}[{},{}][{},{}]'.format(view[0].split('.')[-1],view[1],view[2],view[3],view[4])
            if len(view)==6:
                if isinstance(view[5],str) or isinstance(view[5],unicode):
                    temp = temp + view[5]            
            self.treeWidget.setItem(num,0,QtGui.QTableWidgetItem(temp))
            num = num + 1
        self.treeWidget.resizeColumnsToContents()
        self.treeWidget.resizeRowsToContents()
        self.treeWidget.setCurrentCell(0,0)
    #刷新单个view的信息
    def inittable(self,xml_analysis,index):
        view_info = xml_analysis.get_view_info(index)
        num = 0
        for attri in view_info:
            self.tableWidget.setItem(num,0,QtGui.QTableWidgetItem(attri[0]))
            self.tableWidget.setItem(num,1,QtGui.QTableWidgetItem(attri[1]))
            num = num + 1        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def swithStartButtun(self,flag):
        if flag:
            self.pushButton.setText(_translate("Frame", "停止", None))
        else:
            self.pushButton.setText(_translate("Frame", "开始", None))
        
        
        