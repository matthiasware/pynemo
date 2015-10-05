#!/usr/bin/env python3
import CRUD
import Properties
import Scan
import Host

class ScanBuilder:
    def __init__(self, properties, crud):
        self.properties = properties
        self.crud = crud

    def getScan(self,host):
        return None

    def getSweepScan(self):
        arguments = self.properties.getProperty("sweep","arguments")
        hosts = self.properties.getProperty("sweep","hosts")
        sudo = True
        return Scan.Scan(arguments=arguments, hosts=hosts, sudo=sudo)

    def getScan(self,host):
        arguments=self.properties.getProperty("scans","arguments")
        ip = host.ip
        sudo = True
        return Scan.Scan(arguments=arguments,hosts=ip,sudo=sudo)

