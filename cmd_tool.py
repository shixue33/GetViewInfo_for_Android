#coding=utf-8
'''
Created on 2014年7月14日

@author: huizhi
'''
import subprocess
import os
import time
class CmdTest():
    def __init__(self):
        self.current_dir = ''
        self.current_files = []
        self.local_files = []
        
    def init_dir(self):
        if not os.path.isdir('res'):
            os.mkdir('res')
        if not len(self.current_dir)>0:
            self.current_dir = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            os.mkdir(os.path.join('res',self.current_dir))
    #获取device上的数据，对比数量，如果增加，则把最新的pull到本地
    def get_new_data(self):
        print 'hi this is get_new_data'
        p = subprocess.Popen('adb -d shell ls sdcard/GetInfoFile/', stdout=subprocess.PIPE)
        p.wait()
        print p.returncode
        while(p.returncode!=-1):
            temp = p.stdout.readline()
            self.current_files.append(temp)
            if temp == '' and p.poll() != None:
                break
        update_num = len(self.current_files)-len(self.local_files)
        #通过文件的数量来确定是否有更新的文件，如果新文件数大于0，则需要将新文件pull到本地
        #print 'update_num',update_num
        #print 'len(self.current_files)',len(self.current_files)
        #print 'len(self.local_files)',len(self.local_files)
        if update_num>0:
            for i in range(update_num):
                new_filename = self.current_files[len(self.local_files)]
                self.local_files.append(new_filename)
                subprocess.call('adb -d pull sdcard/GetInfoFile/{} res/{}'.format(new_filename,self.current_dir))
                
                subprocess.call('adb -d pull sdcard/Robotium-Screenshots/{} res/{}'.format(new_filename.replace('.xml','.jpg'),self.current_dir))
            self.current_files = []
            return True
        else:
            self.current_files = []
            return False
        
    def test(self):
        p = subprocess.Popen('adb devices', stdout=subprocess.PIPE)
        p.wait()
        (re,er) = p.communicate()
        if(p.returncode==0):
            print re
            return re
        else:
            print er
            return er
    def load_local(self):
        pass
