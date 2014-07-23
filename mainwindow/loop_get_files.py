
import threading
import time

class LoopGetFiles(threading.Thread):
    def __init__(self,main):
        self.main = main
        
        threading.Thread.__init__(self)
    def run(self):
        while(self.main.run_flag):            
            time.sleep(1)
            flag = self.main.cmd_test.get_new_data() 
            if flag:
                print 'flag:',flag
                self.main.mainframe.initList(self.main.cmd_test)