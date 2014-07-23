#coding=utf-8
from xml.etree import ElementTree
class XmlAnalysis():
    def __init__(self):
        self.view_node = []
        self.view_info = []
        
    def loadFile(self,file_name):
        self.view_info = []
        self.file_name = file_name
        print self.file_name
        self.root = ElementTree.parse(file_name)
        self.views = self.root.getiterator('View')
        for view in self.views:
            for c in view.getchildren():
                if c.tag=='name':
                    self.view_node.append(c.text)
                if c.tag=='x':
                    self.view_node.append(c.text)
                if c.tag=='y':
                    self.view_node.append(c.text)
                if c.tag=='width':
                    self.view_node.append(c.text)    
                if c.tag=='height':
                    self.view_node.append(c.text)
                if c.tag=='text':
                    self.view_node.append(c.text)  
            self.view_info.append(self.view_node)
            self.view_node = []
        
    def get_simple_name(self):        
        return self.view_info
    
    def get_view_info(self,index):
        info = []
        info_node = []
        print 'len(self.views)',len(self.views)
        for c in self.views[index].getchildren():
            if isinstance(c.text,str) or isinstance(c.text,unicode):
                info_node.append(c.tag)
                info_node.append(c.text)
                info.append(info_node)
                info_node = []            
        return info