import json
import random

import pika


class FlightRequestHandler:
    def __init__(self):
        self.queue_name = 'information_center'
        self.exchange_name = 'flight_requests'
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def setup(self):
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(exchange='flight_requests', queue=self.queue_name, routing_key='request')
        print(f'Set up \"{self.queue_name}\"')

    def consume(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.handle_flight_request, auto_ack=True)
        print(f'{self.queue_name} is listening for messages...')
        self.channel.start_consuming()

    def handle_flight_request(self, channel, method, properties, body):
        print(f'Received {body}')
        response = json.loads(body)
        requester = response['airline']

        response['expected'] = 'To be late...'
        random.seed()
        response['gate'] = random.randint(1, 20)
        response['status'] = random.randint(0, 3)
        response = json.dumps(response)
        self.channel.basic_publish(exchange=self.exchange_name, routing_key=requester, body=response)

