#!/usr/bin/env python3

import configparser
import os

class Properties:

    def __init__(self):
        self.filepath = os.path.dirname(os.path.abspath(__file__)) + "/../properties.ini"
        self.configparser = configparser.ConfigParser()

    def getProperty(self,section, key):
        self.configparser.read(self.filepath)
        value = self.configparser.get(section,key)
        return value   