#!/usr/bin/env python3

import unittest
import src

class TLogger(unittest.TestCase):
    def setUp(self):
        self.properties=src.Properties()
        self.logger=src.Logger(self.properties)

    def test_setup(self):
        self.logger.debug("LOG")
        self.logger.warn("WARN")
        self.logger.info("info")