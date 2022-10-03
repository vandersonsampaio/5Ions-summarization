import logging
import pika


def consumer(host, user, password):
    logging.info('Connecting to server...')
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()


def callback(ch, method, body):
    logging.info("Consume %s" % body.decode())
    print(" Received %s" % body.decode())
    print(" Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    consumer('localhost', 'rabbitmq', 'rabbitmq')
