import re

class Customer:
    def __init__(self, customer_id="", first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def set_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.email = email
        else:
            raise ValueError("Invalid email address")

    def set_phone(self, phone):
        if re.fullmatch(r"\d{10}", phone):
            self.phone = phone
        else:
            raise ValueError("Invalid 10-digit phone number")

    def print_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
