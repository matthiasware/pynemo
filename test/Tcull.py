#!/usr/bin/env python3

import unittest
import src

class Tcull(unittest.TestCase):
    def setUp(self):
        self.cull = src.cull()
        self.hosts = {"AB:BF:97:1A:F1:31":"192.168.10.10","AC:BF:97:1A:F1:31":"192.168.10.10",
                      "AC:AF:97:1A:F1:31":"192.168.10.10","AD:BF:97:1A:F1:31":"192.168.10.10",
                      "AD:AF:97:1A:F1:31":"192.168.10.10","AB:BF:97:1A:F1:31":"192.168.10.10",
                      "01:BF:97:1A:F1:31":"192.168.10.10","02:BF:97:1A:F1:31":"192.168.10.10"}

    def test_constructor(self):
        self.cull.updateTargets(self.hosts)