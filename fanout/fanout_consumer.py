#!/usr/bin/env python3
#coding:utf-8

import pika
import chardet
from datetime import datetime


def callback(ch,method,properties,body):
    # print(type(body))
    print(' %s >>>>>>>> Received %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),body.decode("utf-8")))

credentials = pika.PlainCredentials('test', 'test')
#step 1 建立连接
# connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#step 2 创建channel
channel = connection.channel()

#step 3 创建queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

print('declare queue name:%s' % queue_name)

#step 4 将exchange与queue绑定
channel.queue_bind(exchange='fanount_test',queue=queue_name)

channel.basic_consume(callback,queue=queue_name,no_ack=True)

print(' <<<<<<<<<<< Waiting for fanout messages. To exit press CTRL+C')

channel.start_consuming()
