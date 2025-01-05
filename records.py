from datetime import datetime
from fields import Name, Phone
from exceptions import PhoneValidationError, RecordNotFoundError, BirthdayValidationError

class Birthday:
    def __init__(self, value):
        self._value = None  
        self.value = value  

    
    def __set__(self, instance, value):
        try:
            
            self._value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise BirthdayValidationError("Invalid date format. Use DD.MM.YYYY")
    
    def __get__(self, instance, owner):
        return self._value.strftime("%d.%m.%Y") if self._value else "No birthday set."

    def __str__(self):
        return self.__get__(None, None)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise PhoneValidationError()
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        phone = next((p for p in self.phones if p.value == phone_number), None)
        if phone:
            self.phones.remove(phone)
        else:
            raise RecordNotFoundError("Phone number not found in this contact.")

    def edit_phone(self, old_phone_number, new_phone_number):
        phone = next((p for p in self.phones if p.value == old_phone_number), None)
        if phone:
            self.remove_phone(old_phone_number)
            self.add_phone(new_phone_number)
        else:
            raise RecordNotFoundError("Phone number not found.")

    def find_phone(self, phone_number):
        phone = next((p for p in self.phones if p.value == phone_number), None)
        if phone:
            return phone.value
        else:
            raise RecordNotFoundError("Phone number not found.")

    def add_birthday(self, birthday_str):
        try:
            self.birthday = Birthday(birthday_str)
        except ValueError:
            raise BirthdayValidationError()

    def get_birthday(self):
        if self.birthday:
            return str(self.birthday)
        return "No birthday set."

    def has_birthday(self):
        return self.birthday is not None

    def __str__(self):
        birthday_info = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_info}"