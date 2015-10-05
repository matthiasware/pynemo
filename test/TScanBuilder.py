#!/usr/bin/env python3
import src
import unittest

class TScanBuilder (unittest.TestCase):
    def setUp(self):
        self.properties = src.Properties()
        self.crud = src.CRUD(properties=self.properties)
        self.scanBuilder = src.ScanBuilder(properties=self.properties, crud=self.crud)

    def test_getSweepScan(self):
        scan = self.scanBuilder.getSweepScan()
        scan.start()
        scan.join()
        print(scan.result)
        print(scan.nm.scaninfo())
        print(scan.nm.scanstats())
        print(scan.nm._scan_result)

if __name__ == '__main__':
    unittest.main()