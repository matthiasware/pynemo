#!/usr/bin/env python3

class Butcher:
    def __init__(self):
        print("")

    def getMacsAndIpFromScanResult(self, scanner):
        result = {}
        hosts = scanner.all_hosts()

        for host in hosts:
            host_address = scanner[host]["addresses"]
            if "mac" in host_address:
                result.update({host_address["mac"] : {"ip":host,"scanned": 0, "lds" : "", "arguments" :""}})
            else:
                print("ERROR - HOST %s WITHOUT MAC!" % (host))
                continue

        print(result)
        return result
