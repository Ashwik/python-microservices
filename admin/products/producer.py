import pika


def publish():
    try:
        params = pika.URLParameters('amqps://epoqlvqk:gx0FRVyJ0F6moivMc4uQ-wvidfLTvzuE@fish.rmq.cloudamqp.com/epoqlvqk')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key='main', body='hello')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        channel.close()