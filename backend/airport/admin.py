from django.contrib import admin

from .models import *

admin.site.register(Airport)
admin.site.register(Plane)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(PriceTicket)
