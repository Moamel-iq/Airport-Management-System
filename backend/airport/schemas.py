from typing import List
from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from pydantic import UUID4
from backend.account.schemas import AccountOut
from backend.airport.models import *


class AirPortOut(Schema):
    id: UUID4
    name: str
    description: str = None
    code: str
    city: str
    airport_plane_capacity: int


class AirportDataOut(Schema):
    total_count: int = None
    per_page: int = None
    from_record: int = None
    to_record: int = None
    previous_page: int = None
    next_page: int = None
    current_page: int = None
    page_count: int = None
    data: List[AirPortOut]


class PlaneOut(Schema):
    id: UUID4
    code: str
    plane_code: str
    capacity: int
    airport: List[Airport]


class FlightOut(Schema):
    code: str
    plane: List[PlaneOut]
    departure_airport: PlaneOut
    destination_airport: PlaneOut
    starting_time: str
    reaching_time: str


class TicketOut(Schema):
    flight: List[FlightOut]
    passenger: AccountOut
    type: str
    price: List['PriceTicketOut']


class PriceTicketOut(Schema):
    flight: List[FlightOut]
    type: str
    price: int


class Luggage(Schema):
    passenger: AccountOut
    flight: FlightOut
