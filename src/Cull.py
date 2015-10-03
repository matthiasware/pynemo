#!/usr/bin/env python3

class Cull:
    #input, list of macs
    # needs List of hosts (mac, scanned, lds
    targets = {
        "AB:AF:97:1A:F1:31" : {"ip" : "", "scanned": 0, "lds" : "", "arguments" :""},
        "AB:BF:97:1A:F1:31" : {"ip" : "","scanned": 0, "lds" : "", "arguments" :""},
        "AB:CF:97:1A:F1:31" : {"ip" : "","scanned": 2, "lds" : "", "arguments" :""},
        "AB:DF:97:1A:F1:31" : {"ip" : "","scanned": 1, "lds" : "", "arguments" :""},
        "AB:EF:97:1A:F1:31" : {"ip" : "","scanned": 4, "lds" : "", "arguments" :""},
        "AB:FF:97:1A:F1:31" : {"ip" : "","scanned": 3, "lds" : "", "arguments" :""},
        "AC:AF:97:1A:F1:31" : {"ip" : "","scanned": 1, "lds" : "", "arguments" :""},
        "AC:BF:97:1A:F1:31" : {"ip" : "","scanned": 3, "lds" : "", "arguments" :""},
        "AC:CF:97:1A:F1:31" : {"ip" : "","scanned": 4, "lds" : "", "arguments" :""},
        "AC:DF:97:1A:F1:31" : {"ip" : "","scanned": 2, "lds" : "", "arguments" :""},
        "AC:EF:97:1A:F1:31" : {"ip" : "","scanned": 2, "lds" : "", "arguments" :""},
        "AD:AF:97:1A:F1:31" : {"ip" : "","scanned": 1, "lds" : "", "arguments" :""},
        "AD:BF:97:1A:F1:31" : {"ip" : "","scanned": 1, "lds" : "", "arguments" :""},
        "AD:CF:97:1A:F1:31" : {"ip" : "","scanned": 5, "lds" : "", "arguments" :""},
        "AD:DF:97:1A:F1:31" : {"ip" : "","scanned": 1, "lds" : "", "arguments" :""},
        "AD:EF:97:1A:F1:31" : {"ip" : "","scanned": 6, "lds" : "", "arguments" :""}
    }
    frontline = {}
    def __init__(self):
        self.priorityPointer0 = None
        self.priorityPointer1 = None

    def updateTargets(self, newTargets):
        macs_old = list(self.targets.keys())
        macs_new = list(newTargets.keys())
        for mac in macs_old:
            if mac in macs_new:
                print("remove ",mac,"from hosts")
                del newTargets[mac]
            else:
                del self.targets[mac]
                print("remove ",mac,"from targets")

        for mac in newTargets:
            print(mac)

            #check if exists
            #   if scancount < 1
            #       get arguments for new host
            #       put on top
            #   else
            #       if last scan over period
            #           insert beween p0, p1
            #       else
            #           insert after p1 sorted after date
            #
            #else crate new entry
            #   get arguements for new
            #   put on top



    def getTarget(self):
        print("")

    def removeFromFrontline(self):
        print("")
