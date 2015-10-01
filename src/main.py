#!/usr/bin/env python3

import Properties
import cull
import scan
import Properties

properties = Properties.Properties()
sweepscan_arguments = properties.getProperty("sweep","arguments")
sweepscan_hosts = properties.getProperty("sweep","hosts")
sweepscan_intervall = properties.getProperty("sweep","intervall")
sweepscan_sudo = properties.getProperty("sweep","sudo")


initScan = scan.scan(hosts=sweepscan_hosts,arguments=sweepscan_arguments,sudo=sweepscan_sudo)
initScan.start()
initScan.join()
result = initScan.result
print(result)

print(sweepscan_arguments)
print(sweepscan_hosts)
print(sweepscan_intervall)
#from properties get parallel scans
#start sweep scan
#get result
#put result in cull
#start loop