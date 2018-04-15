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
    # connection = pika.BlockingConnection(pika.ConnectionParameters('59.110.237.162',5672,"test",credentials))
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # step 2 创建channel
    channel = connection.channel()

    # step 3 创建exchange，指定faount类型
    channel.exchange_declare(exchange='fanount_test',exchange_type='fanout')

    # send message
    message = getMessage()
    while message:
        channel.basic_publish(exchange='fanount_test',routing_key='',body=message)
        print('%s >>>>>>>>>>> producer fanout message:%s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),message))
        message = getMessage()
    connection.close()
