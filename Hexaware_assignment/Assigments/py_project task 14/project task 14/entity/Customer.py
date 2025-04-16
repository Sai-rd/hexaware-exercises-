import re

class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email if self._validate_email(email) else "Invalid"
        self.phone = phone if self._validate_phone(phone) else "Invalid"
        self.address = address

    def _validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def _validate_phone(self, phone):
        return re.fullmatch(r"\d{10}", phone)

    def __str__(self):
        return (f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\nPhone: {self.phone}\nAddress: {self.address}")
