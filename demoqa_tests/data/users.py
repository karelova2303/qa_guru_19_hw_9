import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    userEmail: str
    gender: str
    mobile: str
    day: str
    month: str
    year: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str
