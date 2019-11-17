import pika
import time


connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='worker_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f"[x] Received {body}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(
    queue='worker_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
