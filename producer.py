#!/usr/bin/env python3
#coding=utf-8

import pika

from datetime import datetime

def getMessage():
    message = input('please input publish data:')
    return message

if __name__ == '__main__':
    # credentials = pika.PlainCredentials('test', 'test')
    #step 1 建立连接
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    # connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
    # pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"／",credentials))
    # step 2 创建channel
    channel = connection.channel()

    #创建queue
    channel.queue_declare(queue='queue_name1')
    channel.queue_declare(queue='queue_name2')

    # send message
    message = getMessage()
    while message:
        channel.basic_publish(exchange='',routing_key='queue_name1',body=message)
        print('%s >>>>>>>>>>> producer message:%s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),message))
        message = getMessage()
    connection.close()
