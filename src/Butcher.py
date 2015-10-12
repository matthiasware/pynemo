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
        return scanResult


        return None
        #update macaddress
        #update ipaddress
        #update hostnames
        #update softvendors
        # update ports
        #update osinfo
        # hardvendors
        # protocolls
        # services
        # scan
        # scan

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