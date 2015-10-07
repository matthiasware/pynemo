#!/usr/bin/env python3

class Cull:
    frontline = {}
    def __init__(self,butcher,scanBuilder,properties,hostQueue,crud):
        self.butcher=butcher
        self.scanBuilder=scanBuilder
        self.properties=properties
        self.hostQueue=hostQueue
        self.crud=crud
        return None

    def getSweepScan(self):
        return self.scanBuilder.getSweepScan()

    def setSweepScanResult(self,scan):
        hosts=self.butcher.processSweepScan(scan.nm)
        self.hostQueue.updateAvailableHosts(hosts)

    def getScan(self):
        return None

    def setScanResult(self):
        return None