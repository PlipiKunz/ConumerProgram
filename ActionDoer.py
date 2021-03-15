import boto3
import json

class ActionDoer():
    def __init__(self, storageType, storageName):
        self.storageType = storageType
        self.storageName = storageName

    #processes the widget

    # return type: {"action":"create"|"delete"|"update",
    #               "widget":widget, "storageType":self.storageType, "storageName":self.storageName }
    def do(self, Widget):
        result = "fail"
        if(self.storageType=="bucket"):
            result = self.doBucket(Widget)
        elif(self.storageType=="DDB"):
            result = self.doDDB(Widget)
        else:
            return "fail"

        return {"result":result, "action":Widget["type"], "widget":Widget, "storageType":self.storageType, "storageName":self.storageName}

    #DynamoDB widget processor
    def doDDB(self,Widget):
        ddb = boto3.resource('dynamodb')
        widgetTable = ddb.Table(self.storageName)
        action = Widget["type"]

        Widget["widget_id"] = Widget["widgetId"]

        if(action=="create"):
            for dict in Widget["otherAttributes"]:
                newDict = {dict["name"]: dict["value"]}
                Widget.update(newDict)
            widgetTable.put_item(Item=Widget)
            return True
        else:
            return False

    #Bucket widget processor
    def doBucket(self, Widget):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.storageName)
        action = Widget["type"]
        widgetKey = ("widgets/" + Widget["owner"].replace(" ", "-") + "/" + Widget["widgetId"])

        if(action=="create"):
            bucket.put_object(Key=widgetKey,Body=json.dumps(Widget))
            return True
        else:
            return False