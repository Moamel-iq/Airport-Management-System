from ninja import Schema
from pydantic import EmailStr, UUID4

from backend.utils.schemas import Token


class AccountOut(Schema):
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str = None
    address: str = None


class AccountSignUpIn(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password1: str
    password2: str
    phone_number: str = None
    address: str = None


class AccountSignupOut(Schema):
    profile: AccountOut
    token: Token


class AccountUpdateIN(Schema):
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    address: str = None


class AccountSigninIN(Schema):
    email: EmailStr
    password: str


class PasswordChange(Schema):
    old_password: str
    new_password1: str
    new_password2: str


