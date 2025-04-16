class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return (f"Customer[ID={self.customer_id}, Name={self.first_name} {self.last_name}, "
                f"Email={self.email}, Phone={self.phone}, Address={self.address}]")