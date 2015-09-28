#!/usr/bin/env python3
import sqlite3

class CRUD:

    columns = {
    "argument" : "argument text",
    "date" : "date datetime",
    "discoverd" : "discovered integer",
    "elapsed" : "elapsed real",
    "entries" : "entries integer",
    "end" : "end datetime",
    "fds" : "fds datetime",
    "hosts" : "hosts integer",
    "host" : "host text",
    "id" : "id integer primary key not null",
    "ip" : "ip text",
    "lds" : "lds datetime",
    "mac" : "mac text",
    "name" : "name text",
    "osvendor" : "osvendor text",
    "osfamily" : "osfamily text",
    "osgeneration" : "osgeneration text",
    "port" : "port integer",
    "product" : "product text",
    "scanned" : "scanned integer",
    "start" : "datetime",
    "uphosts" : "uphosts integer",
    "version" : "version text",
    }

    def __init__(self, properties):
        self.properties = properties
        self.dir = self.properties.getProjectDirectory()
        self.dir += self.properties.getProperty("database","dir")
        self.createDatabaseConnection()

    def createDatabaseConnection(self):
        uptime = self.properties.getProperty("database", "uptime.name")
        meta = self.properties.getProperty("database","meta.name")
        self.uptimepath = "%s/%s" % (self.dir, uptime)
        self.metapath = "%s/%s" % (self.dir, meta)

    def createTables(self):
        self.createTableMAC()
        self.createTableIp()
        self.createTableHosts()
        self.createTableSoftvendors()
        self.createTableHardvendors()
        self.createTablePorts()
        self.createTableOsInfo()
        self.createTableProtocolls()
        self.createTableServices()
        self.createTableArguments()
        self.createTableSweepscans()
        self.createTableUptimes()

    def createTableMAC(self):
        mac = [self.columns["id"],self.columns["mac"],self.columns["fds"],self.columns["lds"],self.columns["scanned"],self.columns["discoverd"]]
        self.createTableIfNotExists(self.metapath,"macaddress",mac)

    def createTableIp(self):
        ip = [self.columns["id"],self.columns["ip"],self.columns["fds"],self.columns["lds"],self.columns["scanned"],self.columns["discoverd"]]
        self.createTableIfNotExists(self.metapath,"ipaddress",ip)

    def createTableHosts(self):
        host = [self.columns["id"],self.columns["host"],self.columns["fds"],self.columns["lds"],self.columns["scanned"],self.columns["discoverd"]]
        self.createTableIfNotExists(self.metapath,"hostnames",host)

    def createTableSoftvendors(self):
        vendor = [self.columns["id"],self.columns["name"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"softvendors",vendor)

    def createTableHardvendors(self):
        vendor = [self.columns["id"],self.columns["name"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"hardvendors",vendor)

    def createTablePorts(self):
        port = [self.columns["id"],self.columns["port"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"ports",port)

    def createTableOsInfo(self):
        osinfo = [self.columns["id"],self.columns["osvendor"],self.columns["osfamily"],self.columns["osgeneration"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"osinfo",osinfo)

    def createTableProtocolls(self):
        protocol = [self.columns["id"],self.columns["name"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"protocols",protocol)

    def createTableServices(self):
        service = [self.columns["id"],self.columns["name"],self.columns["version"],self.columns["product"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"services",service)

    def createTableArguments(self):
        argument = [self.columns["id"],self.columns["name"],self.columns["fds"],self.columns["lds"],self.columns["scanned"]]
        self.createTableIfNotExists(self.metapath,"arguments",argument)

    def createTableSweepscans(self):
        sweepscan = [self.columns["id"],self.columns["uphosts"],self.columns["hosts"],self.columns["date"],self.columns["elapsed"],self.columns["argument"]]
        self.createTableIfNotExists(self.metapath,"sweepscans",sweepscan)

    def createTableUptimes(self):
        uptime = [self.columns["id"],self.columns["name"],self.columns["start"],self.columns["end"],self.columns["entries"]]
        self.createTableIfNotExists(self.metapath,"uptimes",uptime)

    def createTableIfNotExists(self, path,tablename,columnitems):
        conn = sqlite3.connect(path)
        columns = ",".join(columnitems)
        command = "create table if not exists %s(%s);" % (tablename,columns)
        conn.execute(command)
        conn.close()