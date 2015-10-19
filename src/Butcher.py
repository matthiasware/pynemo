#!/usr/bin/env python3
import Host
import Properties
import CRUD
import datetime
import ScanResult
import ScanResultPort

class Butcher:
    def __init__(self,properties,crud,logger):
        self.logger=logger
        self.properties=properties
        self.crud=crud

    def processScan(self,scanner):
        scanResult = self.createScanResultFromScanner(scanner)
        if scanResult.online:
            self.storeScanResult(scanResult)
        else:
            print("Host: %s Ip: %s Mac: %s is not online!" % (scanResult.hostname,scanResult.ip,scanResult.mac))

    def createScanResultFromScanner(self,scanner):
        scanResult = ScanResult.ScanResult()
        scanStats = scanner.scanstats()
        scanResult.elapsed=scanStats["elapsed"]
        scanResult.online = scanStats["uphosts"] == "1"
        scanResult.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanResult.arguments=scanner.command_line()
        if scanResult.online:
            scanResult.ip = scanner.all_hosts()[0]
            print(scanner[scanResult.ip])
            if "addresses" in scanner[scanResult.ip]:
                if "mac" in scanner[scanResult.ip]["addresses"]:
                    scanResult.mac=scanner[scanResult.ip]["addresses"]["mac"]
                    if "vendor" in scanner[scanResult.ip]:
                        if scanResult.mac in scanner[scanResult.ip]["vendor"]:
                            scanResult.hardvendor=scanner[scanResult.ip]["vendor"][scanResult.mac]
            if "osclass" in scanner[scanResult.ip]:
                if "osfamily" in scanner[scanResult.ip]["osclass"]:
                    scanResult.osfamily= scanner[scanResult.ip]["osclass"]["osfamily"]
                if "accuracy" in scanner[scanResult.ip]["osclass"]:
                    scanResult.osaccuracy= scanner[scanResult.ip]["osclass"]["accuracy"]
                if "osgen" in scanner[scanResult.ip]["osclass"]:
                    scanResult.osgeneration= scanner[scanResult.ip]["osclass"]["osgen"]
                if "type" in scanner[scanResult.ip]["osclass"]:
                    scanResult.ostype=scanner[scanResult.ip]["osclass"]["type"]
                if  "vendor" in scanner[scanResult.ip]["osclass"]:
                    scanResult.osvendor=scanner[scanResult.ip]["osclass"]["vendor"]
            if "hostnames" in scanner[scanResult.ip]:
                if len(scanner[scanResult.ip]["hostnames"]) > 0:
                    if "name" in scanner[scanResult.ip]["hostnames"][0]:
                        scanResult.hostname=scanner[scanResult.ip]["hostnames"][0]["name"]
            if "uptime" in scanner[scanResult.ip]:
                if "seconds" in scanner[scanResult.ip]["uptime"]:
                    scanResult.uptime=scanner[scanResult.ip]["uptime"]["seconds"]
            if "tcp" in scanner[scanResult.ip]:
                tcp = scanner[scanResult.ip]["tcp"]
                for port in tcp:
                    scanPort = ScanResultPort.ScanResultPort()
                    portInformation = tcp[port]
                    scanPort.port = port
                    scanPort.protocol="tcp"
                    if "reason" in portInformation:
                        scanPort.reason=portInformation["reason"]
                    if "version" in portInformation:
                        scanPort.version=portInformation["version"]
                    if "name" in portInformation:
                        scanPort.name=portInformation["name"]
                    if "conf" in portInformation:
                        scanPort.conf=portInformation["conf"]
                    if "cpe" in portInformation:
                        scanPort.cpe=portInformation["cpe"]
                    if "extrainfo" in portInformation:
                        scanPort.extrainfo=portInformation["extrainfo"]
                    if "state" in portInformation:
                        scanPort.state=portInformation["state"]
                    if "product" in portInformation:
                        scanPort.product=portInformation["product"]
                    scanResult.ports.append(scanPort)
        return scanResult

    def storeScanResult(self,scanResult):
        if scanResult.mac:
            self.storeScanMacData(scanResult.mac,scanResult.date)
        if scanResult.ip:
            self.storeScanIpData(scanResult.ip,scanResult.date)
        if scanResult.hostname:
            self.storeScanHostnameData(scanResult.hostname,scanResult.date)
        if scanResult.hardvendor:
            self.storeScanHardvendorData(scanResult.hardvendor,scanResult.date)
        if scanResult.osvendor or scanResult.osgeneration or scanResult.osfamily:
            self.storeScanOsInfoData(scanResult.osvendor,scanResult.osfamily,scanResult.osgeneration,scanResult.date)
        if scanResult.osvendor:
            self.storeScanSoftvendorData(scanResult.osvendor,scanResult.date)
        scanid = self.storeScanData(scanResult.mac,scanResult.ip,scanResult.hostname,scanResult.date,
                                    scanResult.arguments,scanResult.elapsed,len(scanResult.ports)>0,scanResult.online,
                                    scanResult.osvendor,scanResult.osfamily,scanResult.osgeneration,scanResult.osaccuracy,scanResult.hardvendor)
        for port in scanResult.ports:
            self.storeScanPortData(port.port,scanResult.date)
            self.storeScanPortServiceData(port.name,port.version,port.product,scanResult.date)
            self.storeScanPortRelation(scanid,port.port,port.conf,port.reason,port.cpe,port.state,port.protocol,
                                       port.version,port.name,port.product,port.extrainfo)

    def storeScanPortRelation(self,scanip,port,conf,reason,cpe,state,protocol,version,name,product,extrainfo):
        rowid=self.crud.insertIntoScanport(scanip,port,conf,reason,cpe,state,protocol,version,name,product,extrainfo)
        return rowid

    def storeScanData(self,mac,ip,host,date,argument,elapsed,openports,scanfinished,osvendor,osfamily,osgeneration,osaccuracy,hardvendor):
        scanid = self.crud.insertIntoScan(mac,ip,host,date,argument,elapsed,openports,scanfinished,osvendor,osfamily,osgeneration,osaccuracy,hardvendor)
        return scanid

    def storeScanPortServiceData(self,service,version,product,date):
        row=self.crud.selectAllFromService(service,version,product)
        if row == None:
            self.crud.insertIntoService(service,version,product,date,date,1)
        else:
            self.crud.updateService(service,version,product,date)

    def storeScanPortData(self,port,date):
        tablePort = self.crud.selectAllFromPorts(port)
        if tablePort == None:
            self.crud.insertIntoPorts(port,date,date,1)
        else:
            self.crud.updatePort(port,date)

    def storeScanOsInfoData(self,osvendor,osfamily,osgeneration,date):
        if (osvendor != None) and (osfamily != None) and (osgeneration != None):
            tableOsInfo = self.crud.selectAllFromOsInfo(osvendor,osfamily,osgeneration)
            if tableOsInfo == None:
                self.crud.insertIntoOsInfo(osvendor,osfamily,osgeneration,date,date,1)
            else:
                self.crud.updateOsInfo(osvendor,osfamily,osgeneration,date)
        else:
            print("TODO LOG OSINFO")

    def storeScanHardvendorData(self,hardvendor,date):
        tableHardvendor = self.crud.selectAllFromHardvendorByHardvendor(hardvendor)
        if tableHardvendor == None:
            self.crud.insertIntoHardvendor(hardvendor,date,date,1)
        else:
            self.crud.updateHardvendorScanned(hardvendor,date)

    def storeScanSoftvendorData(self,softvendor,date):
        tableSoftvendor = self.crud.selectAllFromSoftvendorBySoftvendor(softvendor)
        if tableSoftvendor == None:
            self.crud.insertIntoSoftvendor(softvendor,date,date,1)
        else:
            self.crud.updateSoftvendorScanned(softvendor,date)

    def storeScanHostnameData(self,hostname,date):
        tableHostname = self.crud.selectAllFromHostnameByHostname(hostname)
        if tableHostname == None:
            self.crud.insertIntoHostnames(hostname,date,date,1,0)
        else:
            self.crud.updateHostnameScanned(hostname,date)

    def storeScanIpData(self,ip,date):
        tableIp = self.crud.selectAllFromIpsByIp(ip)
        if tableIp == None:
            self.crud.insertIntoIps(ip,date,date,1,0)
        else:
            self.crud.updateIpScanned(ip,date)

    def storeScanMacData(self,mac,date):
        tableMac = self.crud.selectAllFromMacByMac(mac)
        if tableMac == None:
            self.crud.insertIntoMacs(mac,date,date,1,0)
        else:
            self.crud.updateMacScanned(mac,date)

    def processSweepScan(self,scanner):
        scanid = self.processSweepScanStats(scanner)
        hostlist = self.processSweepScanUpHosts(scanner,scanid)
        return hostlist

    def processSweepScanStats(self,scanner):
        scanstats=scanner.scanstats()
        uphosts = scanstats["uphosts"]
        hosts = scanstats["totalhosts"]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed = scanstats["elapsed"]
        argument = scanner.command_line()
        scanid = self.crud.insertIntoSweepscans(uphosts,hosts,date,elapsed,argument)
        return scanid

    def processSweepScanUpHosts(self,scanner,scanid):
        hosts = scanner.all_hosts()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hostlist = []
        for host in hosts:
            ip = self.getIpFromHost(scanner[host])
            self.updateOrInsertIps(ip,date)
            hostname = self.getHostnameFromHost(scanner[host])
            if hostname != None:
                self.updateOrInsertHostname(hostname,date)
            mac = self.getMacFromHost(scanner[host])
            if mac != None:
                self.crud.insertIntoUphosts(ip,hostname,mac,date,scanid)
                self.updateOrInsertMacs(mac,date)
                hostNew = Host.Host(mac=mac,ip=ip,hostname=hostname)
                hostlist.append(hostNew)
            else:
                print("No Mac for IP: %s, HOST: %s found!" % (ip,hostname))
                continue
        return hostlist

    def updateOrInsertMacs(self,mac,date):
        tableMac = self.crud.selectAllFromMacByMac(mac)
        if tableMac == None:
            self.crud.insertIntoMacs(mac,date,date,0,1)
        else:
            self.crud.updateMacDiscovered(mac)

    def updateOrInsertIps(self,ip,date):
        tableIp = self.crud.selectAllFromIpsByIp(ip)
        if tableIp == None:
            self.crud.insertIntoIps(ip,date,date,0,1)
        else:
            self.crud.updateIpDiscovered(ip)

    def updateOrInsertHostname(self,hostname,date):
        tableHostname = self.crud.selectAllFromHostnameByHostname(hostname)
        if tableHostname == None:
            self.crud.insertIntoHostnames(hostname,date,date,0,1)
        else:
            self.crud.updateHostnameDiscovered(hostname)

    def getIpFromHost(self,host):
        return  host["addresses"]["ipv4"]

    def getMacFromHost(self,host):
        addresses = host["addresses"]
        if "mac" in addresses:
            return addresses["mac"]
        else:
            return None

    def getHostnameFromHost(self,host):
        result = None
        if "hostnames" in host:
            if len(host["hostnames"]) > 0:
                hostname=host["hostnames"][0]
                if "name" in hostname:
                    result = hostname["name"]
        return result