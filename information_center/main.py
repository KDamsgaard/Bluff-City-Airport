from flight_request_handler import FlightRequestHandler

if __name__ == "__main__":
    handler = FlightRequestHandler()
    handler.setup()
    handler.consume()
