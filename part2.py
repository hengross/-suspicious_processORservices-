import psutil
import time

class service:
    def __init__(self, id, name,type,userName,status):
        self.name = name
        self.id = id
        self.type = type
        self.userName = userName
        self.status = status

willContinue = 0
t = 0
f = open("ServicesFile",'w')


firstServiceList = []
firstListSer_pids = []

for seri in psutil.win_service_iter():
    firstServiceList.append(service(seri.pid(),seri.name(),seri.start_type(),seri.username(),seri.status()))
    firstListSer_pids.append(seri.pid())

f.write("first list")
f.write("\n")
for i in range(0, len(firstServiceList)):
    f.write(str(firstServiceList[i].name))
    f.write(", ")
f.write("\n")

print "choose 0  to continue or any other key to stop"
willContinue = input()

percent = psutil.cpu_percent(interval=1)

add = []
remove = []
while(willContinue == 0):
    serList = []
    listSer_pids = []
    for ser in psutil.win_service_iter():
        serList.append(service(ser.pid(), ser.name(), ser.start_type(), ser.username(), ser.status()))
        listSer_pids.append(ser.pid())
    f.write(str(t))
    f.write(" :")
    f.write("the services list: ")
    f.write("\n")
    for i in range(0, len(serList)):
        f.write(str(serList[i].name))
        f.write(", ")
    f.write("\n")
    if (cmp(firstListSer_pids, listSer_pids) == 0):
        print "services list hasn't changed"
    else:
        print "services list has changed"
        for element in firstServiceList:
            if element not in serList:
                add.append(element.id)
        for element in serList:
            if element not in firstServiceList:
                remove.append(element.id)
    prec = psutil.cpu_percent(interval=1)
    if(prec > percent):
        precent = prec
        print "services use more memory than before"
    elif(prec == percent):
        print "services use less memory than before"
    elif(prec < percent):
        print "services use uqual memory as before"
    time.sleep(1)
    t = t + 1
    print "choose 0  to continue or any other key to stop"
    willContinue = input()
