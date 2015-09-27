#!/usr/bin/env python3
import unittest
import src

class TProperties(unittest.TestCase):

    def setUp(self):
        self.properties = src.Properties()

    def test_getProperty(self):
        value = self.properties.getProperty("nmap","nmap.scan.sweep.arguments")
        self.assertEqual(value, "-T4 -sn")
          