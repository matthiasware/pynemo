#!/usr/bin/env python3
import unittest
import src
import datetime

class TCRUD(unittest.TestCase):
    def setUp(self):
        self.properties = src.Properties()
        self.crud = src.CRUD(self.properties)
        self.crud.createTables

    def test_insertAndSelectIntoAndFromUphosts(self):
        ip="192.168.10.10"
        mac="10:A4:AF:8C:EE:AA"
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        host ="Nanana"
        scan=1
        id = self.crud.insertIntoUphosts(ip,host,mac,date,scan)

        result = self.crud.selectAllFromUphostsById(id)
        self.assertEqual(ip,result["ip"])
        self.assertEqual(mac,result["mac"])
        self.assertEqual(host,result["host"])
        self.assertEqual(date,result["date"])
        self.assertEqual(id,result["id"])
        self.assertEqual(scan,result["scan"])

    def test_insertAndSelectFromSweepscans(self):

        uphosts = 50
        hosts = 200
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed = 2.45
        argument = "-T4 -sn"

        id=self.crud.insertIntoSweepscans(uphosts,hosts,date,elapsed,argument)
        result = self.crud.selectAllFromSweepscan(id)

        self.assertEqual(uphosts,result["uphosts"])
        self.assertEqual(hosts,result["hosts"])
        self.assertEqual(date,result["date"])
        self.assertEqual(elapsed,result["elapsed"])
        self.assertEqual(id,result["id"])
        self.assertEqual(argument,result["argument"])