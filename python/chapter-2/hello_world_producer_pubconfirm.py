###############################################
# RabbitMQ in Action
# Chapter 1 - Hello World Producer
#             w/ Publisher Confirms
# 
# Requires: pika >= 0.9.6
# 
# Author: Jason J. W. Williams
# (C)2011
###############################################

import pika, sys

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("192.168.61.10",
                                        credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

# /(hwppc.2) Put channel in "confirm" mode
channel.confirm_delivery()

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(body=msg,
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola")  # /(hwppc.4) Publish the message

channel.close()
