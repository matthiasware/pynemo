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


    def test_setup(self):
        self.nm.scan(hosts="10.42.31.*",arguments="-sn -T4",sudo=True)
        hostlist = self.butcher.processSweepScan(self.nm)
        #for index,host in enumerate(hostlist):
            #print(index,"-",host.mac,":",host.ip,":",host.hostname)

    def test_processScan(self):
        self.nm.scan(hosts="10.42.31.127",arguments="-O -sV -T4",sudo=True)
        result = self.butcher.processScan(self.nm)
        print("elapsed {0:>20}".format(result.elapsed))
        print("host {0:>20}".format(result.hostname))
        print("online {0:>20}".format(result.online))
        print("date {0:>20}".format(result.date))
        print("ip {0:>20}".format(result.ip))
        print("mac {0:>20}".format(result.mac))
        print("hardvendor {0:>20}".format(result.hardvendor))
        if result.uptime != None:
            print("uptime {0:>20}".format(result.uptime))
        print("osvendor {0:>20}".format(result.osvendor))
        print("osaccuracy {0:>20}".format(result.osaccuracy))
        print("osgeneration {0:>20}".format(result.osgeneration))
        print("ostype {0:>20}".format(result.ostype))
        print("osfamily {0:>20}".format(result.osfamily))
        print("arguments {0:>20}".format(result.arguments))

        for port in result.ports:
            print("port {0:>20}".format(port.port))
            print("state {0:>20}".format(port.state))
            print("product {0:>20}".format(port.product))
            print("conf {0:>20}".format(port.conf))
            print("name {0:>20}".format(port.name))
            print("reason {0:>20}".format(port.reason))
            print("cpe {0:>20}".format(port.cpe))
            print("version {0:>20}".format(port.version))
            print("extrainfo {0:>20}".format(port.extrainfo))
            print("protocol {0:>20}".format(port.protocol))