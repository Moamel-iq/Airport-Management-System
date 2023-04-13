from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser, UserManager


class EmailAccountManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('user must have an email to register')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class UserTypeChoices(models.TextChoices):
        EMPLOYEE = 'EMPLOYEE', 'Employee'
        PASSENGER = 'PASSENGER', 'Passenger'

    id = models.AutoField(primary_key=True)
    username = models.NOT_PROVIDED
    email = models.EmailField('Email Address', unique=True)
    type = models.CharField(max_length=10, choices=UserTypeChoices.choices, default=UserTypeChoices.PASSENGER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmailAccountManager()

    def __str__(self):
        return self.email


class Employee(User):
    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.email


class Passenger(User):
    class Meta:
        db_table = 'passenger'

    def __str__(self):
        return self.email
