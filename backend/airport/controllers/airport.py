from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4
from typing import List
from backend.utils import status
from backend.utils.permissions import AuthBearer
from backend.utils.schemas import MessageOut
from backend.airport.models import Airport
from backend.airport.schemas import *
from backend.utils.utils import response

User = get_user_model()

airport_controller = Router(tags=['airport'])


@airport_controller.get('/all', auth=None, response=
{
    200: AirportDataOut,
    404: MessageOut
})
def all_airport(request, search=None, per_page: int = 12, page: int = 1):
    if search:
        airport = Airport.objects.filter(
            Q(name__icontains=search)
        )
    else:
        airport = Airport.objects.all()
    if airport:
        return response(status.HTTP_200_OK, airport, paginated=True, per_page=per_page, page=page)
    return 404, {'message': 'No airport found'}


@airport_controller.get('/{pk}', auth=None, response={
    200: AirPortOut,
    404: MessageOut
})
def get_airport(request, pk: UUID4):
    airport = Airport.objects.get(id=pk)
    if airport:
        return 200, airport
    return 404, {'message': {'No airport found'}}
