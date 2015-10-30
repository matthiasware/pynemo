#!/usr/bin/env python3
import Host
import random

class HostQueue:

    def __init__(self,properties,crud,logger):
        self.crud=crud
        self.logger=logger
        self.prperties=properties
        self.hostqueue = []

    def calculateHostPriority(self,host):
        return random.randint(0,100)

    def getHost(self):
        print(len(self.hostqueue))
        if len(self.hostqueue) > 0:
            result = self.hostqueue[0][1]
            del self.hostqueue[0]
            print(result.ip," : ",result.mac," : ",result.hostname)
            return result
        else:
            return None


    def updateHostQueue(self,hosts):
        self.updateAvailableHosts(hosts)
        for host in hosts:
            priority = self.calculateHostPriority(host)
            self.insertHostInQueue(host,priority)


        #self.updateAvailableHosts(hosts)


    def insertHostInQueue(self,host,priority):
        position = 0;
        for index,hostqueueHost in enumerate(self.hostqueue):
            if hostqueueHost[0] < priority:
                position += 1
                continue;
            else:
                break;
        self.hostqueue.insert(position,(priority,host))


    def updateAvailableHosts(self, hosts):
        hostqueueNew = []
        for hostOld in self.hostqueue:
            if self.hostInHosts(hostOld[1], hosts):
                hostqueueNew.append(hostOld)
                self.deleteHostFromHosts(hostOld[1],hosts)
        self.hostqueue = hostqueueNew


    def outline(self):
        for host in self.hostqueue:
            print(host[0], " : ",host[1].mac, " ", host[1].ip, " ", host[1].hostname)

    def hostInHosts(self, host, hosts):
        for hostItem in hosts:
            if host.mac == hostItem.mac:
                return True
        return False

    def deleteHostFromHosts(self,host,hosts):
        macs = []
        for hostItem in hosts:
            macs.append(hostItem.mac)

        for index,mac in enumerate(macs):
            if host.mac == mac:
                del hosts[index]
