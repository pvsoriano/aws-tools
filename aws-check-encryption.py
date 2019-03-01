import boto3

# Setup session using RAP credentials
session = boto3.Session(profile_name='ddpa-rap-poc')
s3 = session.resource('s3')
client = session.client('s3')

# Determining encrypting by checking object encryption within each bucket
#bucket = s3.Bucket('s3-ue2-agent-jar-delta')

#RAPBucket = s3.buckets.all()

#for bucket in RAPBucket:
#	for obj in bucket.objects.all():
#		key = s3.Object(bucket.name, obj.key)
#		if key.server_side_encryption == None:
#			print(obj.key, key.server_side_encryption)


# Determining encryption by checking encryption at the bucket level
RAPBucket = s3.buckets.all()

#response = client.get_bucket_encryption(Bucket='s3-ue2-agent-jar-delta')
#print(response)
for x in RAPBucket:
	y = x.name
	response = client.get_bucket_encryption(Bucket=y)
	print(response)
