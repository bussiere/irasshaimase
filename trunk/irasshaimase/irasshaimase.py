#!/usr/bin/env python
import threading,time,bluetooth,os,random
filelist = []
filelist = os.listdir("annonce")
random.shuffle(filelist)
class T (threading.Thread) :
    def __init__(self,_filelist) :
        threading.Thread.__init__(self)
        self.present = 0
        self.filelist = _filelist
    def run(self) :
        while(True):
            time.sleep(8)
            jeton = 0
            nearby_devices = bluetooth.discover_devices(lookup_names = True)
            for name, addr in nearby_devices:
                if name == "00:14:A7:9C:0D:2B":
                    if self.present == 0:
                        os.system("mplayer annonce/%s"%self.filelist[0])
                        self.present = 1
                    jeton = 1
            if jeton == 0 and self.present == 1 :
                self.present = 0

                
t = T(filelist)               
t.start()