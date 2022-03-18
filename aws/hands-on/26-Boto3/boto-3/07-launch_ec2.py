import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-xxxxxxxxxxxxx',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='your keypair without .pem'
 )

#stop instance
import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('write-instance Id').stop()

#terminate instance
import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-03bf26c047835daab').terminate()