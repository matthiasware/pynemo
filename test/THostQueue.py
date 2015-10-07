#!/usr/bin/env python3
import unittest
import src
class THostQueue (unittest.TestCase):
    def setUp(self):
        self.properties=src.Properties()
        self.crud=src.CRUD(self.properties)
        self.queue = src.HostQueue(self.properties,self.crud)

        host_a = src.Host(mac="AB:BF:97:1A:F1:31",ip='192.168.10.0',hostname="a")
        host_b = src.Host(mac="BB:BF:97:1A:F1:31",ip="192.168.10.1",hostname="b")
        host_c = src.Host(mac="CB:BF:97:1A:F1:31",ip="192.168.10.2",hostname="c")
        host_d = src.Host(mac="DB:BF:97:1A:F1:31",ip="192.168.10.3",hostname="d")
        host_e = src.Host(mac="EB:BF:97:1A:F1:31",ip="192.168.10.4",hostname="e")
        host_f = src.Host(mac="FB:BF:97:1A:F1:31",ip="192.168.10.5",hostname="f")
        host_g = src.Host(mac="GB:BF:97:1A:F1:31",ip="192.168.10.6",hostname="g")
        host_h = src.Host(mac="HB:BF:97:1A:F1:31",ip="192.168.10.7",hostname="h")
        host_i = src.Host(mac="IB:BF:97:1A:F1:31",ip="192.168.10.8",hostname="i")
        host_j = src.Host(mac="JB:BF:97:1A:F1:31",ip="192.168.10.9",hostname="j")
        host_k = src.Host(mac="KB:BF:97:1A:F1:31",ip="192.168.10.10",hostname="k")
        host_l = src.Host(mac="LB:BF:97:1A:F1:31",ip="192.168.10.11",hostname="l")

        self.hosts = [host_a,host_b,host_c,host_d,host_e]
        self.hosts2 = [host_a,host_b,host_f,host_g,host_h]

    def test_updateHostQueue(self):
        self.queue.updateHostQueue(self.hosts)
        self.queue.outline()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.queue.outline()
        host = self.queue.getHost()
        print(host.mac, " ", host.ip, " ", host.hostname)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.queue.outline()
        host = self.queue.getHost()
        print(host.mac, " ", host.ip, " ", host.hostname)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.queue.outline()
        host = self.queue.getHost()
        print(host.mac, " ", host.ip, " ", host.hostname)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.queue.outline()
        host = self.queue.getHost()
        print(host.mac, " ", host.ip, " ", host.hostname)