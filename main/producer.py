import pika, json


def publish(method, body):
    try:
        params = pika.URLParameters('amqps://epoqlvqk:gx0FRVyJ0F6moivMc4uQ-wvidfLTvzuE@fish.rmq.cloudamqp.com/epoqlvqk')
        connection = pika.BlockingConnection(params)
        properties = pika.BasicProperties(method)

        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        channel.close()