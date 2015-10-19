#!/usr/bin/env python3

class ScanResult():
    def __init__(self):
        self.ip = None #D
        self.mac = None #D
        self.hardvendor = None #D
        self.hostname = None #D
        self.date = None #D
        self.elapsed = None #D
        self.arguments = None #D
        self.online = None #D
        self.osvendor = None #D
        self.osfamily = None #D
        self.osgeneration = None #D
        self.osaccuracy = None #D
        self.ostype = None #D
        self.uptime = None #D
        self.ports = [] #D

    def outline(self):
        print("ip: %s" % self.ip)
        print("mac: %s" % self.mac)
        print("hardvendor: %s" % self.hardvendor)
        print("hostname: %s" % self.hostname)
        print("elapsed: %s" % self.elapsed)
        print("arguments: %s" % self.arguments)
        print("online: %s" % self.online)
        print("osvendor: %s" % self.osvendor)
        print("osfamily: %s" % self.osfamily)
        print("osgeneration: %s" % self.osgeneration)
        print("osaccuracy: %s" % self.osaccuracy)
        print("ostype: %s" % self.ostype)
        print("uptime: %s" % self.uptime)
        for port in self.ports:
            print("-------------------------")
            print("\tport: %s" % port.port)
            print("\tconf: %s" % port.conf)
            print("\treason: %s" % port.reason)
            print("\tcpe: %s" % port.cpe)
            print("\tstate: %s" % port.state)
            print("\tproduct: %s" % port.product)
            print("\tversion: %s" % port.version)
            print("\tname: %s" % port.name)
            print("\tprotocol: %s" % port.protocol)
            print("\textrainfo: %s" % port.extrainfo)


