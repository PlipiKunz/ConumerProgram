import sys
from ConsumerProgram import consumer

fromBucket = "usu-cs5260-bluemoon-requests"
storageType = "DDB"
storageName = "widgets"


if(len(sys.argv)>=4):
    fromBucket = sys.argv[1]
    storageType = sys.argv[2]
    storageName = sys.argv[3]

c = consumer(fromBucket, storageType, storageName)
c.main()