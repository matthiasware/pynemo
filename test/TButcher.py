#!/usr/bin/env python3

import unittest
import src
import nmap

class TButcher(unittest.TestCase):
    def setUp(self):
        self.properties = src.Properties()
        self.logger = src.Logger(self.properties)
        self.crud = src.CRUD(self.properties, self.logger)
        self.crud.deleteAll()
        self.crud.createTables()
        self.butcher=src.Butcher(self.properties,self.crud,self.logger)
        self.nm = nmap.PortScanner()


    def ttest_sweepscan(self):
        self.nm.scan(hosts="10.42.31.*",arguments="-sn -T4",sudo=True)
        hostlist = self.butcher.processSweepScan(self.nm)
        for index,host in enumerate(hostlist):
            print(index,"-",host.mac,":",host.ip,":",host.hostname)

    def test_processScan(self):
        self.nm.scan(hosts="10.42.31.235",arguments="-O -sV -T4",sudo=True)
        self.butcher.processScan(self.nm)