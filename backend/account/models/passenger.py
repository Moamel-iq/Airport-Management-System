from backend.account.models import EmailAccount
from django.db import models


class Passenger(EmailAccount):
    class Meta:
        db_table = 'passenger'

    def __str__(self):
        return self.email


