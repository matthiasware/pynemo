#!/usr/bin/env python3
import unittest
import src
import datetime
import time


class TCRUD(unittest.TestCase):

    def setUp(self):
        self.properties = src.Properties()
        self.logger = src.Logger(self.properties)
        self.crud = src.CRUD(self.properties,self.logger)
        self.crud.deleteAll()
        self.crud.createTables()

    #todp: arguments, protocols

    def test_ups(self):
        ip="192.168.10.10"
        mac="10:A4:AF:8C:EE:AA"
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        host ="Nanana"
        scan=1

        row=self.crud.selectAllFromUphostsById(1)
        self.assertEqual(row,None)

        id=self.crud.insertIntoUphosts(ip,host,mac,date,scan)

        row=self.crud.selectAllFromUphostsById(id)
        self.assertEqual(ip,row["ip"])
        self.assertEqual(mac,row["mac"])
        self.assertEqual(host,row["host"])
        self.assertEqual(date,row["date"])
        self.assertEqual(id,row["id"])
        self.assertEqual(scan,row["scan"])

    def test_scanports(self):
        scan=2
        port=50
        conf="yo"
        reason="mum"
        cpe="is"
        state="cna"
        protocol="tcp"
        version="1"
        name="goku"
        product="kamehame"
        extrainfo="no info"

        row=self.crud.selectAllFromScanportByScan(1)
        self.assertEqual(None,row)

        self.crud.insertIntoScanport(scan,port,conf,reason,cpe,state,protocol,version,name,product,extrainfo)

        row=self.crud.selectAllFromScanportByScan(scan)
        self.assertEqual(scan,row["scan"])
        self.assertEqual(port,row["port"])
        self.assertEqual(conf,row["conf"])
        self.assertEqual(reason,row["reason"])
        self.assertEqual(cpe,row["cpe"])
        self.assertEqual(state,row["state"])
        self.assertEqual(protocol,row["protocol"])
        self.assertEqual(version,row["version"])
        self.assertEqual(name,row["name"])
        self.assertEqual(product,row["product"])
        self.assertEqual(extrainfo,row["extrainfo"])


    def test_scan(self):
        mac="yo"
        ip="fat"
        host="mama"
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arguments="is"
        elapsed="3.45"
        openports=True
        scanfinished=True
        osvendor="cat"
        osfamily="catty"
        osgeneration="mooooh"
        osaccuracy=85
        hardvendor="krupp"

        row=self.crud.selectAllFromScan(1)
        self.assertEqual(row,None)

        id=self.crud.insertIntoScan(mac,ip,host,date,arguments,elapsed,openports,scanfinished,osvendor,osfamily,osgeneration,osaccuracy,hardvendor)

        row=self.crud.selectAllFromScan(id)
        self.assertEqual(mac,row["mac"])
        self.assertEqual(ip,row["ip"])
        self.assertEqual(host,row["host"])
        self.assertEqual(date,row["date"])
        self.assertEqual(arguments,row["arguments"])
        self.assertEqual(openports,row["openports"])
        self.assertEqual(osvendor,row["osvendor"])
        self.assertEqual(scanfinished,row["scanfinished"])
        self.assertEqual(osgeneration,row["osgeneration"])
        self.assertEqual(osaccuracy,row["osaccuracy"])
        self.assertEqual(id,row["id"])
        self.assertEqual(hardvendor,row["hardvendor"])




    def test_sweepscan(self):
        uphosts = 50
        hosts = 200
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed = 2.45
        argument = "-T4 -sn"

        row=self.crud.selectAllFromSweepscan(1)
        self.assertEqual(row,None)

        id=self.crud.insertIntoSweepscans(uphosts,hosts,date,elapsed,argument)
        row = self.crud.selectAllFromSweepscan(id)

        self.assertEqual(uphosts,row["uphosts"])
        self.assertEqual(hosts,row["hosts"])
        self.assertEqual(date,row["date"])
        self.assertEqual(elapsed,row["elapsed"])
        self.assertEqual(id,row["id"])
        self.assertEqual(argument,row["argument"])


    def test_service(self):
        service = "yo"
        version="fat"
        product="moma"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        scanned = 10;
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row=self.crud.selectAllFromService(service,version,product)
        self.assertEqual(row,None)

        self.crud.insertIntoService(service,version,product,fds,fds,scanned)

        row=self.crud.selectAllFromService(service,version,product)
        self.assertEqual(row["service"],service)
        self.assertEqual(row["version"],version)
        self.assertEqual(row["product"],product)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)

        self.crud.updateService(service,version,product,lds)

        row=self.crud.selectAllFromService(service,version,product)
        self.assertEqual(row["service"],service)
        self.assertEqual(row["version"],version)
        self.assertEqual(row["product"],product)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)


    def test_ports(self):
        port = 22
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        scanned = 0;
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row=self.crud.selectAllFromPorts(port)
        self.assertEqual(row,None)

        self.crud.insertIntoPorts(port,fds,fds,scanned)

        row=self.crud.selectAllFromPorts(port)
        self.assertEqual(row["port"],port)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)

        self.crud.updatePort(port,lds)

        row=self.crud.selectAllFromPorts(port)
        self.assertEqual(row["port"],port)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)


    def test_osinfo(self):
        osvendor="yo"
        osfamily="fat"
        osgeneration="mom"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        scanned = 0;
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row=self.crud.selectAllFromOsInfo(osvendor,osfamily,osgeneration)
        self.assertEqual(row,None)

        self.crud.insertIntoOsInfo(osvendor,osfamily,osgeneration,fds,fds,scanned)

        row=self.crud.selectAllFromOsInfo(osvendor,osfamily,osgeneration)
        self.assertEqual(row["osvendor"],osvendor)
        self.assertEqual(row["osfamily"],osfamily)
        self.assertEqual(row["osgeneration"],osgeneration)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)

        self.crud.updateOsInfo(osvendor,osfamily,osgeneration,lds)

        row=self.crud.selectAllFromOsInfo(osvendor,osfamily,osgeneration)
        self.assertEqual(row["osvendor"],osvendor)
        self.assertEqual(row["osfamily"],osfamily)
        self.assertEqual(row["osgeneration"],osgeneration)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)


    def test_hardvendors(self):
        hardvendor = "yo-fat-cat"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanned = 10;

        row = self.crud.selectAllFromHardvendorByHardvendor(hardvendor)
        self.assertEqual(row,None)

        self.crud.insertIntoHardvendor(hardvendor,fds,fds,scanned)

        row = self.crud.selectAllFromHardvendorByHardvendor(hardvendor)
        self.assertEqual(row["hardvendor"],hardvendor)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)

        self.crud.updateHardvendorScanned(hardvendor,lds)

        row = self.crud.selectAllFromHardvendorByHardvendor(hardvendor)
        self.assertEqual(row["hardvendor"],hardvendor)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)



    def test_softvendors(self):
        osvendor = "yo-mama"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanned = 5;

        row = self.crud.selectAllFromSoftvendorBySoftvendor(osvendor)
        self.assertEqual(row,None)

        self.crud.insertIntoSoftvendor(osvendor,fds,fds,scanned)

        row = self.crud.selectAllFromSoftvendorBySoftvendor(osvendor)
        self.assertEqual(row["osvendor"],osvendor)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)

        self.crud.updateSoftvendorScanned(osvendor,lds)

        row = self.crud.selectAllFromSoftvendorBySoftvendor(osvendor)
        self.assertEqual(row["osvendor"],osvendor)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)


    def test_host(self):
        host = "yo-mama-is-a-mainframe"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanned = 5;
        discovered = 6;

        row = self.crud.selectAllFromHostnameByHostname(host)
        self.assertEqual(row,None)

        self.crud.insertIntoHostnames(host,fds,fds,scanned,discovered)

        row = self.crud.selectAllFromHostnameByHostname(host)
        self.assertEqual(row["host"],host)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered)

        self.crud.updateHostnameDiscovered(host)

        row = self.crud.selectAllFromHostnameByHostname(host)
        self.assertEqual(row["host"],host)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered+1)

        self.crud.updateHostnameScanned(host,lds)

        row = self.crud.selectAllFromHostnameByHostname(host)
        self.assertEqual(row["host"],host)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)
        self.assertEqual(row["discovered"],discovered+1)

    def test_mac(self):
        mac="10:A4:AF:8C:EE:AA"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanned = 2;
        discovered = 3;

        row = self.crud.selectAllFromMacByMac(mac)
        self.assertEqual(row,None)

        self.crud.insertIntoMacs(mac,fds,fds,scanned,discovered)

        row = self.crud.selectAllFromMacByMac(mac)
        self.assertEqual(row["mac"],mac)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered)

        self.crud.updateMacDiscovered(mac)

        row = self.crud.selectAllFromMacByMac(mac)
        self.assertEqual(row["mac"],mac)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered+1)

        self.crud.updateMacScanned(mac,lds)

        row = self.crud.selectAllFromMacByMac(mac)
        self.assertEqual(row["mac"],mac)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)
        self.assertEqual(row["discovered"],discovered+1)

    def test_ip(self):
        ip="192.168.1.1"
        fds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        lds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanned = 3;
        discovered = 4;

        row = self.crud.selectAllFromIpsByIp(ip)
        self.assertEqual(row,None)

        self.crud.insertIntoIps(ip,fds,fds,scanned,discovered)

        row = self.crud.selectAllFromIpsByIp(ip)
        self.assertEqual(row["ip"],ip)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered)

        self.crud.updateIpDiscovered(ip)

        row = self.crud.selectAllFromIpsByIp(ip)
        self.assertEqual(row["ip"],ip)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],fds)
        self.assertEqual(row["scanned"],scanned)
        self.assertEqual(row["discovered"],discovered+1)

        self.crud.updateIpScanned(ip,lds)

        row = self.crud.selectAllFromIpsByIp(ip)
        self.assertEqual(row["ip"],ip)
        self.assertEqual(row["fds"],fds)
        self.assertEqual(row["lds"],lds)
        self.assertEqual(row["scanned"],scanned+1)
        self.assertEqual(row["discovered"],discovered+1)

