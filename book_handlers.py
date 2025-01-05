from decorators import input_error
from records import Record
from exceptions import RecordAlreadyExistsError

@input_error
def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args, book):
    name, phone, *_ = args    
    record = Record(name)
    record.add_phone(phone)
    message = "Contact added."    
    return message
    
@input_error
def change_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.change_phone(old_phone, new_phone)
    return f"Phone number for {name} updated."

@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return f"Phone numbers for {name}: " + ", ".join(record.phones)

@input_error
def show_all_contacts(args, book):
    for name, record in book.data.items():   
        return record

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(birthday)
    return f"Birthday for {name} added successfully."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."
    return f"No birthday set for {name}."

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        return "Upcoming birthdays: " + ", ".join(upcoming)
    return "No upcoming birthdays."