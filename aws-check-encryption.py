import boto3
from pprint import pprint

# Setup session using local credentials
session = boto3.Session(profile_name='')
s3 = session.resource('s3')
client = session.client('s3')

# Determine encryption by checking encryption at the bucket level
Bucket = s3.buckets.all()

# Iterate over the response to print out the bucket name and if it's encrypted or not
for x in Bucket:
	y = x.name
	response = client.get_bucket_encryption(Bucket=y)
	#pprint(response)
	#print(response)
	for meta, rules in response.items():
		#print("\nMeta: ", meta)
		for key, val in rules.items():
			print(y)
			print(val)
