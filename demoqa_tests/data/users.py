import dataclasses
import enum


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    mobile: str
    day: str
    month: str
    year: str
    subject: str
    hobby: enum
    file: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name,
                 user_email, gender, mobile, day, month, year, subject, hobby, file, address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.gender = gender
        self.mobile = mobile
        self.day = day
        self.month = month
        self.year = year
        self.subject = subject
        self.hobby = hobby
        self.file = file
        self.address = address
        self.state = state
        self.city = city
