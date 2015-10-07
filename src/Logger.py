#!/usr/bin/env python3
import logging
import logging.handlers

class Logger:
    def __init__(self,properties):
        self.properties = properties
        dir = properties.getProjectDirectory()
        self.file = dir+self.properties.getProperty("logging","file")
        self.log = self.setUpLogging()

    def setUpLogging(self):
        serverlog = logging.FileHandler(self.file)
        serverlog.setLevel(logging.DEBUG)
        serverlog.setFormatter(logging.Formatter('%(asctime)s %(pathname)s [%(process)d]: %(levelname)s %(message)s'))

        logger = logging.getLogger('wbs-server-log')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(serverlog)

        return logger

    def debug(self,msg):
        self.log.debug(msg)

    def info(self,msg):
        self.log.info(msg)

    def warn(self,msg):
        self.log.warning(msg)