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

        objects = boto3.client('s3').list_objects_v2(Bucket=bucket.name, MaxKeys=1)


        if("Contents" in objects.keys()):
            objects = objects["Contents"]

            for item in objects:
                object = s3.Object(self.bucketName, item['Key']).get()
                jsonPrimitive = object["Body"].read()
                jsonAsDict = json.loads(jsonPrimitive)
                bucket.delete_objects(Delete={'Objects':[{"Key":item['Key']}]})
                return (jsonAsDict)

        return "fail"

