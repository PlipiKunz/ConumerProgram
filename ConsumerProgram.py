from ActionDoer import ActionDoer
from ObjectGetter import ObjectGetter
import time

class consumer():
    def __init__(self, fromBucket, storageType, storageName):
        self.bucketFromName = fromBucket
        self.storageType = storageType
        self.storageName = storageName

        self.doer = ActionDoer(self.storageType, self.storageName)
        self.getter = ObjectGetter(fromBucket)

    def main(self):
        while(True):
            widget = self.getter.popAndMakeObject()

            if(widget=="fail"):
                time.sleep(100)
                #add log saying fail to get widget
            else:
                result = self.doer.do(widget)
                #add log of result