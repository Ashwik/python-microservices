import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

def consume():
    try:
        params = pika.URLParameters('amqps://epoqlvqk:gx0FRVyJ0F6moivMc4uQ-wvidfLTvzuE@fish.rmq.cloudamqp.com/epoqlvqk')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='admin')

        def callback(ch, method, properties, body):
            print('Received in admin')
            data = json.loads(body)
            print(data)
            product = Product.objects.get(id=data)
            product.likes = product.likes+1
            product.save()
            print('Product likes increased')

        channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
        print('start consuming')
        channel.start_consuming()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        channel.close()

consume()