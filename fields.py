import re
from exceptions import PhoneValidationError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):        
        if not re.match(r'^\d{10}$', value):
            raise PhoneValidationError()  
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):        
        super().__init__(value)