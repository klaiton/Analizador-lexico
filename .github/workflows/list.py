import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('marketing-images-stg')
for obj in bucket.objects.all():
    if(obj.key[0:4] != ".git"):
        print('https://marketing-images-stg.s3.amazonaws.com/{}'.format(obj.key))
        
        
