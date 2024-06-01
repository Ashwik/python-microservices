import pika


def consume():
    try:
        params = pika.URLParameters('amqps://epoqlvqk:gx0FRVyJ0F6moivMc4uQ-wvidfLTvzuE@fish.rmq.cloudamqp.com/epoqlvqk')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='main')

        def callback(ch, method, properties, body):
            print('Received in main')
            print(body)

        channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
        print('start consuming')
        channel.start_consuming()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        channel.close()


print('consuming')
consume()