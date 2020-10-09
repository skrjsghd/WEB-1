import sys
from PIL import ImageGrab
import time
import boto3
import configparser
from tendo import singleton

me = singleton.SingleInstance()

config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-16')

config = config['MAIN']
name = config['NAME']
access = config['ACCESS_KEY']
secret = config['SECRET_KEY']
bucket_name = config['BUCKET_NAME']

print(name,access,secret,bucket_name)


# aws credentials setting
client = boto3.client(
    's3',
    aws_access_key_id = access,
    aws_secret_access_key = secret
    )

print('서버에 접속되었습니다.')

print('캡쳐를 시작합니다.')

set_time= [00,10,20,30,40,50]


while True:
    now= time.gmtime(time.time())
    if now.tm_min in set_time and now.tm_sec == 0:
        img = ImageGrab.grab()
        filename="{}{}".format(name,'.png')
        img.save(filename)
        client.upload_file(filename, bucket_name, filename)
        print('success')
    
    
    
    








