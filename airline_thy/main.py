from datetime import datetime, time

from flight_request_handler import FlightRequestHandler

if __name__ == "__main__":
    thy_handler = FlightRequestHandler(airline_name='THY')
    thy_handler.setup()
    thy_handler.request_flight(
        number=1234,
        destination='Geita Mchauru Airport (GIT)',
        departure_time=datetime(year=2020, month=2, day=10, hour=10),
        check_in_time=time(hour=9),
        check_in_status=False
    )
    thy_handler.consume()
