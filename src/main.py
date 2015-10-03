#!/usr/bin/env python3

import Properties
import Cull
import Scan
import Properties
import Butcher

properties = Properties.Properties()
sweepscan_arguments = properties.getProperty("sweep","arguments")
sweepscan_hosts = properties.getProperty("sweep","hosts")
sweepscan_intervall = properties.getProperty("sweep","intervall")
sweepscan_sudo = properties.getProperty("sweep","sudo")


initScan = Scan.Scan(hosts=sweepscan_hosts,arguments=sweepscan_arguments,sudo=sweepscan_sudo)
initScan.start()
initScan.join()
scanner = initScan.nm

butcher = Butcher.Butcher()
butcher.getMacsAndIpFromScanResult(scanner)

#from properties get parallel scans
#start sweep scan
#get result
#put result in cull
#start loop