import unittest
from ConsumerProgram import consumer

class consumerTester(unittest.TestCase):
    def test(self):
        fromBucket = "usu-cs5260-bluemoon-requests"
        storageType = "DDB"
        storageName = "widgets"
        c = consumer(fromBucket, storageType, storageName)

        #testing consumer variables
        self.assertEqual(c.bucketFromName, fromBucket)
        self.assertEqual(c.storageType, storageType)
        self.assertEqual(c.storageName, storageName)

        #testing objectGetter
        og = c.getter
        self.assertEqual(og.bucketName, fromBucket)

        #testing actionDoer
        doer = c.doer
        self.assertEqual(doer.storageName, storageName)
        self.assertEqual(doer.storageType, storageType)