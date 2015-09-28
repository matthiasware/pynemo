#!/usr/bin/env python3
import unittest
import src

class TCRUD(unittest.TestCase):
    def setUp(self):
         self.properties = src.Properties()
         self.crud = src.CRUD(self.properties)

    def test_createTables(self):
        self.crud.createTables()