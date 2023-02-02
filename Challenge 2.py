To query the metadata of an instance in AWS and provide a JSON formatted output, you can use one of the AWS SDKs like (Boto3) or the AWS CLI.


import boto3

client = boto3.client('ec2')
instance_id = client.meta.instance_id

instance = client.describe_instances(InstanceIds=[instance_id])
instance_data = instance['Reservations'][0]['Instances'][0]

result = {
    'InstanceId': instance_id,
    'InstanceType': instance_data['InstanceType'],
    'LaunchTime': instance_data['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S'),
    'PublicIpAddress': instance_data.get('PublicIpAddress', 'Not available'),
    'PrivateIpAddress': instance_data.get('PrivateIpAddress', 'Not available'),
    'VpcId': instance_data['VpcId']
}

import json
print(json.dumps(result, indent=4))



This code uses the Boto3 client to describe the instance and extract the relevant metadata, such as the instance ID, instance type, launch time, public IP address, private IP address, and VPC ID. 
The resulting metadata is then stored in a Python dictionary and formatted as JSON using the json library.

To retrieve a particular data key individually, you can do the below : 

def retrieve_data_key(key):
    if key in result:
        return result[key]
    else:
        return 'Key not found'

# Example usage:
print(retrieve_data_key('InstanceId'))


This code defines a function retrieve_data_key that takes a key as an argument and returns the value associated with that key in the result dictionary, 
or 'Key not found' if the key is not present in the dictionary.
