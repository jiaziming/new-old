#!/usr/bin/python
# -*-coding:utf-8-*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

#声明一个queue
channel.queue_declare(queue='hello')


#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Word')
print("[x] Sent 'Hello Word ")
connection.close()