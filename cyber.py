__author__ = 'hengross'

import psutil
import time

class pro:
        def __init__(self,id,name):
                self.name = name
                self.id = id

# list = psutil.pids()
f = open("processFile",'w')
willContinue = 0
isChanged = False

#firat list of processes
FirstlistProcess = []
for proc in psutil.process_iter():
        n = proc.name()
        i = proc.pid
        FirstlistProcess.append(pro(i, n))
list1 = psutil.pids()
f.write("first list")
f.write("\n")
for i in range(0,len(FirstlistProcess)):
  f.write(str(FirstlistProcess[i].name))
  f.write(", ")
f.write("\n")
#end of first proccesses

print "choose 0  to continue or any other key to stop"
willContinue = input()
addProcessList = []
removeProcessList = []
t = 0

while(willContinue == 0):
        listProcess = []
        for proc in psutil.process_iter() :
                n = proc.name()
                i = proc.pid
                listProcess.append(pro(i,n))
        list2 = psutil.pids()
        listSize = len(listProcess)
        for i in range(0,listSize):
                print listProcess[i].name , listProcess[i].id
        f.write(str(t))
        f.write(" :")
        f.write("the process list:")
        f.write("\n")
        for i in range(0, len(listProcess)):
                f.write(str(listProcess[i].name))
                f.write(", ")
        f.write("\n")
        if(cmp(list1,list2) == 0):
                print "processes list hasn't changed"
        else:
                print "processes list has changed"
                for element in FirstlistProcess:
                        if element not in listProcess:
                                addProcessList.append(element.id)
                for element in listProcess:
                        if element not in FirstlistProcess:
                                removeProcessList.append(element.id)

        time.sleep(1)
        t = t + 1
        print "choose 0  to continue or any other key to stop"
        willContinue = input()