#!/usr/bin/env python3
#coding:utf-8

import pika
import chardet
from datetime import datetime
import sys


def callback(ch,method,properties,body):
    print(' %s >>>>>>>>consumer>>>>>>> %r : %r' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),method.routing_key, body.decode("utf-8")))

# credentials = pika.PlainCredentials('test', 'test')
#step 1 建立连接
# connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#step 2 创建channel
channel = connection.channel()

#step 3 创建queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

print('declare queue name:%s' % queue_name)

binding_keys = sys.argv[1:]
if not binding_keys:
    print("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_test',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
