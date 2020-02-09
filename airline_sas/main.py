from datetime import datetime, time

from flight_request_handler import FlightRequestHandler

if __name__ == "__main__":
    sas_handler = FlightRequestHandler(airline_name='SAS')
    sas_handler.setup()
    sas_handler.request_flight(
        number=9876,
        destination='Old Town Dewitt Field Municipal Airport (OLD)',
        departure_time=datetime(year=2020, month=2, day=10, hour=10),
        check_in_time=time(hour=9),
        check_in_status=False
    )
    sas_handler.consume()

