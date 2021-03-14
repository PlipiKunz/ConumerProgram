class ActionDoer():
    def __init__(self, storageType, storageName):
        self.storageType = storageType
        self.storageName = storageName

    #processes the widget
    def do(self, Widget):
        if(self.storageType=="bucket"):
            return self.doBucket(Widget)
        elif(self.storageType=="DDB"):
            return self.doDDB(Widget)
        else:
            return "fail"

    #DynamoDB widget processor
    def doDDB(self,Widget):
        pass

    #Bucket widget processor
    def doBucket(self, Widget):
        pass