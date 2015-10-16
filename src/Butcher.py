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
        scanResult = ScanResult.ScanResult()
        scanStats = scanner.scanstats()
        scanResult.elapsed = scanStats["elapsed"]
        scanResult.online = scanStats["uphosts"] == "1"
        scanResult.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        scanResult.ip = scanner.all_hosts()[0]
        print(scanner[scanResult.ip])
        addresses = scanner[scanResult.ip]["addresses"]
        scanResult.mac=addresses["mac"]
        scanResult.arguments = scanner.command_line()
        scanResult.hardvendor = scanner[scanResult.ip]["vendor"][scanResult.mac]
        if "uptime" in scanner[scanResult.ip]:
            scanResult.uptime =  scanner[scanResult.ip]["uptime"]["seconds"]
        if "hostnames" in scanner[scanResult.ip]:
            scanResult.hostname = scanner[scanResult.ip]["hostnames"][0]["name"]
        if "osclass" in scanner[scanResult.ip]:
            osclass = scanner[scanResult.ip]["osclass"]
            if "vendor" in osclass:
                scanResult.osvendor = osclass["vendor"]
            if "accuracy" in osclass:
                scanResult.osaccuracy = osclass["accuracy"]
            if "osgen" in osclass:
                scanResult.osgeneration = osclass["osgen"]
            if "type" in osclass:
                scanResult.ostype = osclass["type"]
            if "osfamily" in osclass:
                scanResult.osfamily = osclass["osfamily"]
        if "tcp" in scanner[scanResult.ip]:
            tcp = scanner[scanResult.ip]["tcp"]
            for port in tcp:
                scanPort = ScanResultPort.ScanResultPort()
                portInformation = tcp[port]
                scanPort.port = port
                scanPort.state = portInformation["state"]
                scanPort.product = portInformation["product"]
                scanPort.conf = portInformation["conf"]
                scanPort.name = portInformation["name"]
                scanPort.reason = portInformation["reason"]
                scanPort.cpe = portInformation["cpe"]
                scanPort.version = portInformation["version"]
                scanPort.extrainfo = portInformation["version"]
                scanPort.protocol = "tcp"
                scanResult.ports.append(scanPort)

        self.writeScanResultToDatabase(scanResult)

        return scanResult
        #update softvendors
        # update ports
        #update osinfo
        # hardvendors
        # protocolls
        # services
        # scan
        # scan

    def writeScanResultToDatabase(self, scanResult):
        self.crud.updateMacScanned(scanResult.mac, scanResult.date)
        self.crud.updateIpScanned(scanResult.ip,scanResult.date)
        self.crud.updateHostnameScanned(scanResult.hostname,scanResult.date)
        if(scanResult.osvendor != None):
            self.updateOrInsertSoftvendors(scanResult.osvendor,scanResult.date)
        if(scanResult.hardvendor != None):
            self.updateOrInsertHardvendors(scanResult.hardvendor,scanResult.date)
        self.updateOrInsertOSInfo(scanResult)
        self.updateOrInsertPorts(scanResult)
        self.insertScan(scanResult)

        return None

    def insertScan(self,scanResult):
        scanid = self.crud.insertIntoScan(scanResult.mac,scanResult.ip,scanResult.hostname,scanResult.date,scanResult.arguments,
                                 scanResult.elapsed,scanResult.openports,scanResult.online,scanResult.osvendor,scanResult.osfamily,
                                 scanResult.osgeneration,scanResult.osaccuracy,scanResult.hardvendor)
        return scanid

    def updateOrInsertPorts(self,scanResult):
        if scanResult.ports:
            for port in scanResult.ports:
                tablePort = self.crud.selectAllFromPorts(port.port)
                if tablePort == None:
                    self.crud.insertIntoPorts(port.port,scanResult.date,scanResult.date,1)
                else:
                    self.crud.updatePort(port.port,scanResult.date)

    def updateOrInsertOSInfo(self,scanResult):
        if (scanResult.osvendor != None) and (scanResult.osfamily != None) and (scanResult.osgeneration != None):
            tableOsInfo = self.crud.selectAllFromOsInfo(scanResult.osvendor,scanResult.osfamily,scanResult.osgeneration)
            if tableOsInfo == None:
                self.crud.insertIntoOsInfo(scanResult.osvendor,scanResult.osfamily,scanResult.osgeneration,scanResult.date,scanResult.date,1)
            else:
                self.crud.updateOsInfo(scanResult.osvendor,scanResult.osfamily,scanResult.osgeneration,scanResult.date)

    def updateOrInsertSoftvendors(self,softvendor,date):
        tableSoftvendor = self.crud.selectAllFromSoftvendorBySoftvendor(softvendor)
        if tableSoftvendor == None:
            self.crud.insertIntoSoftvendor(softvendor,date,date,1)
        else:
            self.crud.updateSoftvendorScanned(softvendor,date)

    def updateOrInsertHardvendors(self,hardvendor,date):
        tableHardvendor = self.crud.selectAllFromHardvendorByHardvendor(hardvendor)
        if tableHardvendor == None:
            self.crud.insertIntoHardvendor(hardvendor,date,date,1)
        else:
            self.crud.updateHardvendorScanned(hardvendor,date)

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
        return  host["hostnames"][0]["name"]