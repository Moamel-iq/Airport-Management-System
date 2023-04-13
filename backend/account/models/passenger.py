from backend.account.models import User


class Passenger(User):
    class Meta:
        db_table = 'passenger'

    def __str__(self):
        return self.email
