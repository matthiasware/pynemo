#!/usr/bin/env python3

class ScanResult():
    def __init__(self):
        self.ip = None
        self.mac = None
        self.hardvendor = None
        self.hostname = None
        self.date = None
        self.elapsed = None
        self.arguments = None
        self.online = None
        self.osvendor = None
        self.osfamily = None
        self.osgeneration = None
        self.osaccuracy = None
        self.ostype = None
        self.uptime = None
        self.openports = None
        self.ports = []
