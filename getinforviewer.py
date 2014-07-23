#coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import frame
import about
import cmd_tool
import loop_get_files
import xml_analysis
import os
import glob

class StartWindow(QMainWindow):
    def __init__(self,parent=None):  
        super(StartWindow,self).__init__(parent)
        self.run_flag = False
        self.cmd_test = cmd_tool.CmdTest()
        self.xml_analysis = xml_analysis.XmlAnalysis()
        self.mainframe = frame.Ui_Frame()
        
        self.mainframe.setupUi(self)
        self.mainframe.initList(self.cmd_test)
        
        self.connect(self.mainframe.pushButton, SIGNAL("clicked()"),self.proStart)
        self.connect(self.mainframe.pushButton_2, SIGNAL("clicked()"),self.proTest)
        self.connect(self.mainframe.pushButton_3, SIGNAL("clicked()"),self.loadLocal) 
        self.connect(self.mainframe.pushButton_5, SIGNAL("clicked()"),self.showAbout)
        self.connect(self.mainframe.listWidget, SIGNAL('clicked(QModelIndex)'),self.flashdata)
        self.connect(self.mainframe.treeWidget, SIGNAL('clicked(QModelIndex)'),self.flashView)
        
        self.loop_get_file = loop_get_files.LoopGetFiles(self)
        self.loop_get_file.start()
    def flashdata(self):
        #self.mainframe.initList(self.cmd_test)
        i = self.mainframe.listWidget.currentRow()
        
        tempfile = os.path.join('res',self.cmd_test.current_dir,self.mainframe.files[i])
        self.xml_analysis.loadFile(tempfile)
        self.mainframe.initTree(self.xml_analysis)
        self.mainframe.loadPic(tempfile.replace('.xml','.jpg'))
    def flashView(self):
        index = self.mainframe.treeWidget.currentRow()
        print index 
        print 'self.mainframe.treeWidget.rowCount()',self.mainframe.treeWidget.rowCount()
        
        self.mainframe.inittable(self.xml_analysis, index)
        
    
    def proStart(self):
        self.cmd_test.init_dir()
        self.run_flag = not self.run_flag
        self.loop_get_file = loop_get_files.LoopGetFiles(self)
        self.loop_get_file.start()
        self.mainframe.swithStartButtun(self.run_flag)
        
    def proTest(self):        
        QMessageBox.information(self, 'Test', self.cmd_test.test())
        print 'proTest'
    def loadLocal(self):
        list=QStringList()
        templist = glob.glob('res/*')
        templist.reverse()
        for temp_path in templist:
            if os.path.isdir(temp_path):
                (p1,p2) = os.path.split(temp_path)
                list.append(p2)
            
        file_path,ok=QInputDialog.getItem(self,'local','Select the folder:',list)

        if ok:
            print p2
            self.cmd_test.current_dir = str(file_path)
            
            self.mainframe.initList(self.cmd_test)
            self.mainframe.treeWidget.clear()
            self.mainframe.tableWidget.clear()
    
    def showAbout(self):
        print 'about'
        ab = about.Ui_Dialog()
        ab.setupUi()
        ab.exec_() 
         

if __name__ == '__main__':
    app=QApplication(sys.argv)
    startwindow=StartWindow()
    startwindow.show()    
    app.exec_()
    