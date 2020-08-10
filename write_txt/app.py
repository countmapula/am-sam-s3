import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    your_bucket_name = 'example-bucket' # update me 
    s3.meta.client.upload_file('hello_world.txt', your_bucket_name, 'hello.txt')