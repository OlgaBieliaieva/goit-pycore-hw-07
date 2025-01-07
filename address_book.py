from collections import UserDict
from datetime import datetime, timedelta
from exceptions import RecordNotFoundError, BirthdayValidationError
from records import Record
from fields import Name, Phone, Birthday

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        record = self.data.get(name)
    
        if record is None:
            raise RecordNotFoundError(f"Contact '{name}' not found.")
        return record
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise RecordNotFoundError(f"Contact '{name}' not found.")
    
    def add_birthday(self, name, birthday_str):
        try:
            
            record = self.find(name)
           
            birthday = Birthday(birthday_str)
            
            record.birthday = birthday
        except BirthdayValidationError as e:
            raise BirthdayValidationError(f"Error adding birthday to '{name}': {e}")
    
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()
        one_week_from_today = today + timedelta(days=7)
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday._value.date()
                upcoming_birthday_this_year = birthday.replace(year=today.year)
                if today <= upcoming_birthday_this_year <= one_week_from_today:
                    upcoming_birthdays.append(record.name.value)
        return upcoming_birthdays