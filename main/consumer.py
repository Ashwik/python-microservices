import pika, json

from main import Product, db

def consume():
    try:
        params = pika.URLParameters('amqps://epoqlvqk:gx0FRVyJ0F6moivMc4uQ-wvidfLTvzuE@fish.rmq.cloudamqp.com/epoqlvqk')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='main')

        def callback(ch, method, properties, body):
            print('Received in main')
            data = body
            print(data)

            if properties.content_type == 'product_created':
                product = Product(id=data['id'], title=data['title'], image=data['image'])
                db.session.add(product)
                db.session.commit()
                print("Product created")

            elif properties.content_type == 'product_updated':
                product = Product.query.get(data['id'])
                product.title = data['title']
                product.image = data['image']
                db.session.commit()
                print("Product updated")

            elif properties.content_type == 'product_deleted':
                product_id = int(data)
                product = Product.query.get(product_id)
                db.session.delete(product)
                db.session.commit()
                print("Product deleted")

        channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
        print('start consuming')
        channel.start_consuming()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        channel.close()


print('consuming')
consume()