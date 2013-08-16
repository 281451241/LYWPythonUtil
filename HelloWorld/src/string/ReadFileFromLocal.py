'''
Created on 2013-8-16

@author: GB
'''
import time

class ReadFileFromLocal(object):
    def read(self):
        flag = -1
        files = open('D:/java/apache-maven-3.0.5/build.xml')
        try:
            for line in files:
                if flag == 1 or line.find('<!--') >= 0 :
                    flag = 1
                    
                    if line.find("-->") >= 0:
                        flag = -1
                        pass
                    
                    else:
                        continue
                        pass
                else:
                    print line,
                    flag = -1
                    
        finally:
            files.close()

class LYWDate():
    def osPath(self):
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        
r=ReadFileFromLocal()
r.read()