#!/usr/bin/env python3

import unittest
import src

class Tcull(unittest.TestCase):
    def setUp(self):
        self.cull = src.cull()

    def test_constructor(self):
        self.cull.updateTargets(self.hosts)