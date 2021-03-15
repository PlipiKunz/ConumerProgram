import unittest
from ConsumerProgram import consumer

import logging

class consumerTester(unittest.TestCase):
    def test(self):
        logging.basicConfig(filename='consumerTestLogger.log',level=logging.INFO)


        fromBucket = "usu-cs5260-bluemoon-requests"
        storageType = "DDB"
        storageName = "widgets"
        c = consumer(fromBucket, storageType, storageName)

        #testing consumer variables
        self.assertEqual(c.bucketFromName, fromBucket)
        self.assertEqual(c.storageType, storageType)
        self.assertEqual(c.storageName, storageName)
        logging.info("consumer variables properly set up")

        #testing objectGetter
        og = c.getter
        self.assertEqual(og.bucketName, fromBucket)
        logging.info("getter variables properly set up")

        #testing actionDoer
        doer = c.doer
        self.assertEqual(doer.storageName, storageName)
        self.assertEqual(doer.storageType, storageType)
        logging.info("doer variables properly set up")