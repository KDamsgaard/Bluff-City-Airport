import json
from datetime import datetime, time

import pika


class FlightRequestHandler:
    def __init__(self, airline_name):
        self.airline_name = airline_name
        self.exchange_name = 'flight_requests'
        self.params = pika.ConnectionParameters(heartbeat=1, blocked_connection_timeout=1, host='localhost')
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()

    def setup(self):
        self.channel.queue_declare(queue=self.airline_name)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.airline_name, routing_key=self.airline_name)
        print(f'Set up airline \"{self.airline_name}\"')

    def request_flight(self, number: int, destination: str, departure_time: datetime, check_in_time: time,
                       check_in_status: bool = 0):

        flight = json.dumps({
            'airline': self.airline_name,
            'flight_number': self.airline_name + str(number),
            'destination': destination,
            'departure_time': departure_time.strftime("%d/%m/%Y, %H:%M:%S"),
            'check_in_time': check_in_time.strftime("%H:%M:%S"),
            'check_in_status': check_in_status,
        })

        self.channel.basic_publish(exchange=self.exchange_name, routing_key='request', body=flight)
        print(f'Sent {flight}')

    def consume(self):
        self.channel.basic_consume(queue=self.airline_name, on_message_callback=self.handle_response, auto_ack=True)
        print(f'{self.airline_name} is listening for messages...')
        self.channel.start_consuming()

    def handle_response(self, channel, method, properties, body):
        print(f'{self.airline_name} received {body}')
