#!/usr/bin/env python3

import Properties
import Cull
import Properties
import Butcher
import CRUD
import Logger
import HostQueue
import ScanBuilder

properties = Properties.Properties()
logger = Logger.Logger(properties)
crud = CRUD.CRUD(properties,logger)
hostQueue = HostQueue.HostQueue(properties,crud)
scanBuilder = ScanBuilder.ScanBuilder(properties,crud)
butcher = Butcher.Butcher(properties,crud,logger)
cull = Cull.Cull(butcher,scanBuilder,properties,hostQueue,crud)

#from properties get parallel scans
#start sweep scan
#get result
#put result in cull
#start loop