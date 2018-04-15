#!/usr/bin/env python3
#coding:utf-8

import pika
import chardet
from datetime import datetime


def callback(ch,method,properties,body):
    # print(type(body))
    print(' %s >>>>>>>> Received %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),body.decode("utf-8")))

# credentials = pika.PlainCredentials('test', 'test')
# #step 1 建立连接
# connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#step 2 创建channel
channel = connection.channel()

#step 3 创建queue
channel.queue_declare(queue='hello2')

# channel.basic_consume(callback,queue='queue_name1')
channel.basic_consume(callback,queue='queue_name1',no_ack=False)

print(' <<<<<<<<<<< Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
