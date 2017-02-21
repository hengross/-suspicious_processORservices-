import psutil
import Tkinter
import tkMessageBox

class service:
    def __init__(self, id, name,type,userName,status):
        self.name = name
        self.id = id
        self.type = type
        self.userName = userName
        self.status = status

firstServiceList = []
firstListSer_pids = []
firstListSer_names = []

percent = psutil.cpu_percent(interval=1)

def firstServicesList(FirstlistProcess):
    for seri in psutil.win_service_iter():
        firstServiceList.append(service(seri.pid(), seri.name(), seri.start_type(), seri.username(), seri.status()))
        firstListSer_pids.append(seri.pid())
        firstListSer_names.append(seri.name())
    return firstServiceList

list = []
firstlist = firstServicesList(list)

def printFirst():
    str = " "
    for element in firstlist:
        str = str + element.name
        str = str + ","
        str = str + "\n"
    tkMessageBox.showinfo("first service list",str)

addServicesList = []
removeServicesList = []

def currentProcessesList(addList,removeList):
    listServices = []
    ListSer_pids = []
    ListSer_names = []
    for ser in psutil.win_service_iter():
        listServices.append(service(ser.pid(), ser.name(), ser.start_type(), ser.username(), ser.status()))
        ListSer_pids.append(ser.pid())
        ListSer_names.append(ser.name())
    if (cmp(firstListSer_pids,ListSer_pids) == 0):
        print "services list hasn't changed"
    else:
        print "services list has changed"
        for element in firstListSer_names:
            if element not in ListSer_names:
                print "hjdjh"
                addList.append(element)
        for element in ListSer_names:
            if element not in firstListSer_names:
                print"popop"
                removeList.append(element)
    return listServices

def memoryPercent():
    per = psutil.cpu_percent(interval=1)
    if(per < percent):
        tkMessageBox.showinfo("memory percent","services use less memory than before")
    elif (per > percent):
        tkMessageBox.showinfo("memory percent","services use more memory than before")
    elif (per == percent):
        tkMessageBox.showinfo("memory percent","services use uqual memory as before")

def cuurentList():
    currentList = currentProcessesList(addServicesList, removeServicesList)
    string = " "
    for element in currentList:
        string = string + element.name
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("current processes list", string)

def addList():
    string = " "
    for element in addServicesList:
        string = string + element
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("added processes list", string)

def removeList():
    string = " "
    for element in removeServicesList:
        string = string + element
        string = string + ","
        string = string + "\n"
    tkMessageBox.showinfo("removed processes list", string)

top = Tkinter.Tk()
FirstList = Tkinter.Button(top,text = "first services list",command = printFirst)
FirstList.pack()
currentList = Tkinter.Button(top,text = "current services list",command = cuurentList)
currentList.pack()
addedList = Tkinter.Button(top,text = "added services list",command = addList)
addedList.pack()
removedList = Tkinter.Button(top,text = "removed services list",command = removeList)
removedList.pack()
memory = Tkinter.Button(top,text = "memory percent: ",command = memoryPercent)
memory.pack()
top.mainloop()