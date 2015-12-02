import urllib2
import boto

response = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key")

key = response.read()
access_key = key[0:20]
secret_key = key[22:60]


print(access_key)
print(secret_key)
print(boto.Version)
