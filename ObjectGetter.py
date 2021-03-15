import boto3
import botocore
import json

class ObjectGetter():
    def __init__(self, bucketName):
        self.bucketName = bucketName


    #gets an object from the bucket, and then deletes it from the bucket
    def popAndMakeObject(self):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucketName)

        for item in bucket.objects.all():
            object = s3.Object(self.bucketName, item.key).get()
            jsonPrimitive = object["Body"].read()
            jsonAsDict = json.loads(jsonPrimitive)
            bucket.delete_objects(Delete={'Objects':[{"Key":item.key}]})
            return (jsonAsDict)

        return "fail"


# getter = ObjectGetter("usu-cs5260-bluemoon-requests")
# getter.popAndMakeObject()