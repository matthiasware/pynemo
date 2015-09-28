#!/usr/bin/env python3
import unittest
import src

class TProperties(unittest.TestCase):

    def setUp(self):
        self.properties = src.Properties()

    def test_getProperty(self):
        dir = self.properties.getProperty("database","dir")
        self.assertEqual(dir, "data")

        meta = self.properties.getProperty("database","meta.name")
        self.assertEqual(meta, "meta.db")

        uptime = self.properties.getProperty("database","uptime.name")
        self.assertEqual(uptime, "uptime.db")

    def test_getProjectDirectory(self):
        dir = self.properties.getProjectDirectory()
        self.assertEqual(dir, "/home/n0mi/hackspace/pynemo/")

