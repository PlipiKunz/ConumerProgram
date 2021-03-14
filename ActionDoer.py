class ActionDoer():
    def __init__(self, storageType, storageName):
        self.storageType = storageType
        self.storageName = storageName

    def do(self, Widget):
        if(self.storageType=="bucket"):
            return self.doBucket(Widget)
        elif(self.storageType=="DDB"):
            return self.doDDB(Widget)
        else:
            return "fail"

    def doDDB(self,Widget):
        pass

    def doBucket(self, Widget):
        pass