import sys
from ConsumerProgram import consumer
from tester import consumerTester

fromBucket = "usu-cs5260-bluemoon-requests"
storageType = "DDB"
storageName = "widgets"


if("--help" in sys.argv):
    print("Proper Format: python main.py fromBucket storageType storageName")
    print("\tfromBucket: the bucket holding the widget requests")
    print("\tstorageType: if to use DDB or bucket, poper values are DDB or bucket")
    print("\tstorageName: the resource name associated with storage type, eg the dynamoDB table name, or bucket name")

elif("test" in sys.argv):
    ct = consumerTester()
    ct.test()

else:
    if(len(sys.argv)>=4):
        fromBucket = sys.argv[1]
        storageType = sys.argv[2]
        storageName = sys.argv[3]

    c = consumer(fromBucket, storageType, storageName)
    c.main()
