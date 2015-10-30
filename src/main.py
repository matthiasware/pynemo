#!/usr/bin/env python3

import Properties
import Cull
import Properties
import Butcher
import CRUD
import Logger
import HostQueue
import ScanBuilder
import time
import datetime

properties = Properties.Properties()
logger = Logger.Logger(properties)
crud = CRUD.CRUD(properties,logger)
hostQueue = HostQueue.HostQueue(properties,crud,logger)
scanBuilder = ScanBuilder.ScanBuilder(properties,crud)
butcher = Butcher.Butcher(properties,crud,logger)
cull = Cull.Cull(butcher,scanBuilder,properties,hostQueue,crud)

sweepscan=cull.getSweepScan()
sweepscan.run()
cull.setSweepScanResult(sweepscan)
scan=cull.getScan()
scan.start()
scan.join()
cull.setScanResult(scan)

scans = []
for i in range(4):
    scans.append(None)

while True:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"LOOPITERATION")
    if not sweepscan.isAlive():
        cull.setSweepScanResult(sweepscan)
        sweepscan=cull.getSweepScan()
        sweepscan.start()
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Sweepscan - START")

    for i in range(4):
        if scans[i] == None:
            scans[i] = cull.getScan()
            if scans[i] != None:
                scans[i].start()
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," SCAN: ",i, " - START")

    for i in range(4):
        if not scans[i] == None:
            if not scans[i].isAlive():
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," SCAN: ",i, " - TERMINATED")
                cull.setScanResult(scans[i])
                scans[i]=None
    time.sleep(10)




#from properties get parallel scans
#start sweep scan
#get result
#put result in cull
#start loop