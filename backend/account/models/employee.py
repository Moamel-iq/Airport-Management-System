from backend.account.models import User


class Employee(User):
    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.email
