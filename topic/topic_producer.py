#!/usr/bin/env python3
#coding=utf-8

import pika
import sys
import os

from datetime import datetime

def getMessage():
    message = input('please input publish data:')
    return message

if __name__ == '__main__':
    routing_key = None

    if len(sys.argv)>=2:
        routing_key = sys.argv[1]
    else:
        print('please input routing key')
        os._exit(0)


    # credentials = pika.PlainCredentials('test', 'test')
    #step 1 建立连接
    # connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # step 2 创建channel
    channel = connection.channel()

    # step 3 创建exchange，指定topic类型
    channel.exchange_declare(exchange='topic_test',exchange_type='topic')

    # send message
    message = getMessage()
    while message:
        channel.basic_publish(exchange='topic_test',routing_key=routing_key,body=message)
        print('%s >>>>>>>>>>> producer topic message [%s]:%s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),routing_key,message))
        message = getMessage()
    connection.close()
