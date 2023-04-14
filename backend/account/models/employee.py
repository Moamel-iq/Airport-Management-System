from backend.account.models import EmailAccount
from django.db import models


class Employee(EmailAccount):
    address = models.CharField(max_length=256, null=True, blank=True)
    salary = models.IntegerField( null=True, blank=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.email
