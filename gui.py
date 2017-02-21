import Tkinter
import psutil
import tkMessageBox

class process:
    def __init__(self, id, name):
        self.name = name
        self.id = id

def firstProcessesList(FirstlistProcess):
    for pro in psutil.process_iter():
        n = pro.name()
        d = pro.pid
        FirstlistProcess.append(n)
    return FirstlistProcess

list = []
firstlist = firstProcessesList(list)

def printFirst():
    str = " "
    for element in firstlist:
        str = str + element
        str = str + ","
        str = str + "\n"
    tkMessageBox.showinfo("first processes list",str)

addProcessList = []
removeProcessList = []

def currentProcessesList(addList,removeList):
    listProcess = []
    for pro in psutil.process_iter():
        n = pro.name()
        d = pro.pid
        listProcess.append(n)
    if(len(firstlist) == 0):
        print "click on first Processes List"
    elif (cmp(firstlist,listProcess) == 0):
        print "processes list hasn't changed"
    else:
        print "processes list has changed"
        for element in firstlist:
            if element not in listProcess:
                addList.append(element)
        for element in listProcess:
            if element not in firstlist:
                removeList.append(element)
    return listProcess

# currentList = currentProcessesList(addProcessList,removeProcessList)

def cuurentList():
    currentList = currentProcessesList(addProcessList, removeProcessList)
    string = " "
    for element in currentList:
        string = string + element
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("current processes list", string)

def addList():
    string = " "
    for element in addProcessList:
        string = string + element
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("added processes list", string)

def removeList():
    string = " "
    for element in removeProcessList:
        string = string + element
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("removed processes list", string)

top = Tkinter.Tk()
First = Tkinter.Button(top,text = "first processes list",command = printFirst)
First.pack()
second = Tkinter.Button(top,text = "current processes list",command = cuurentList)
second.pack()
added = Tkinter.Button(top,text = "added processes list",command = addList)
added.pack()
removed = Tkinter.Button(top,text = "removed processes list",command = removeList)
removed.pack()
top.mainloop()