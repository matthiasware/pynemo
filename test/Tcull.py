#!/usr/bin/env python3

import unittest
import src

class Tcull(unittest.TestCase):
    def setUp(self):
        self.properties = src.Properties()
        self.logger = src.Logger(self.properties)
        self.crud = src.CRUD(self.properties, self.logger)
        self.butcher=src.Butcher(self.properties,self.crud,self.logger)
        self.scanBuilder = src.ScanBuilder(self.properties,self.crud)
        self.hostQueue = src.HostQueue(self.properties,self.crud)
        self.cull = src.Cull(self.butcher,self.scanBuilder,self.properties,self.hostQueue,self.crud)

    def test_constructor(self):
        scan = self.cull.getScan()
