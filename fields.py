import re
from datetime import datetime
from exceptions import PhoneValidationError, BirthdayValidationError

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


class Birthday:
    def __init__(self, value):
        self._value = None  
        self.value = value  

    @property
    def value(self):
        return self._value.strftime("%d.%m.%Y") if self._value else "No birthday set."
    
    @value.setter
    def value(self, value):
        try:            
            self._value = datetime.strptime(value, "%d.%m.%Y")            
        except ValueError:
            raise BirthdayValidationError("Invalid date format. Use DD.MM.YYYY")    

    def __str__(self):
        return self.value