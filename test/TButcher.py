#!/usr/bin/env python3

import unittest
import src
import nmap

class TButcher(unittest.TestCase):
    def setUp(self):
        self.properties = src.Properties()
        self.logger = src.Logger(self.properties)
        self.crud = src.CRUD(self.properties, self.logger)
        self.butcher=src.Butcher(self.properties,self.crud,self.logger)
        self.nm = nmap.PortScanner()


#    def test_setup(self):
 #       self.nm.scan(hosts="10.42.31.*",arguments="-sn -T4",sudo=True)
  #      hostlist = self.butcher.processSweepScan(self.nm)
   #     for index,host in enumerate(hostlist):
    #        print(index,"-",host.mac,":",host.ip,":",host.hostname)

    def test_processScan(self):
        self.nm.scan(hosts="10.42.31.203",arguments="-O -sV -T4",sudo=True)
        result = self.butcher.processScan(self.nm)
        print(result.elapsed)
        print(result.online)
        print(result.date)