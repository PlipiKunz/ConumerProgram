from ActionDoer import ActionDoer
from ObjectGetter import ObjectGetter
import time
from datetime import datetime
import logging

class consumer():
    def __init__(self, fromBucket, storageType, storageName):
        self.bucketFromName = fromBucket
        self.storageType = storageType
        self.storageName = storageName

        self.doer = ActionDoer(self.storageType, self.storageName)
        self.getter = ObjectGetter(fromBucket)

    #the main loop that constantly tries to get an object,
    # then process the object
    def main(self):
        logging.basicConfig(filename='consumerLogger.log',level=logging.INFO)
        while(True):
            widgetRequest = self.getter.popAndMakeObject()
            resultString = ""

            if(widgetRequest=="fail"):
                time.sleep(100)
                #add log saying fail to get widget
                resultString = "fail"
                print("fail")
            else:
                result = self.doer.do(widgetRequest)
                resultString = "In "+ result["storageType"] + ": " + result['storageName'] + ", at time: " + (str)(datetime.fromtimestamp(time.time())) + ", " + result["action"] + "d widget:" + result['widget']['widgetId']
                print(resultString)

            logging.info(resultString)

