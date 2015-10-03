#!/usr/bin/env python3
import threading
import nmap

class Scan (threading.Thread):
    def __init__(self, hosts, arguments, sudo):
        threading.Thread.__init__(self)
        self.arguments = arguments
        self.hosts=hosts
        self.sudo=sudo

    def run(self):
        self.nm = nmap.PortScanner()
        self.nm.scan(hosts=self.hosts,arguments=self.arguments, sudo=self.sudo)