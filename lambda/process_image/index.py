import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')
BUCKET = 'image-upload-<ACCOUNT-ID>'  # Replace or parameterize

def handler(event, context):
    body = base64.b64decode(event['body'])
    file_name = f"uploads/{str(uuid.uuid4())}.jpg"
    s3.put_object(Bucket=BUCKET, Key=file_name, Body=body)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Uploaded', 'file': file_name})
    }
