from decorators import input_error
from records import Record
from fields import Phone, Birthday
from exceptions import RecordAlreadyExistsError, PhoneValidationError, RecordNotFoundError, BirthdayValidationError

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
    name, *details = args   
    
    try:
        book.find(name)
        raise RecordAlreadyExistsError(f"Contact '{name}' already exists.")
    except RecordNotFoundError:
        pass

    record = Record(name)
    
    for index, detail in enumerate(details, start=2):
        try:
            phone_obj = Phone(detail)
            record.add_phone(phone_obj.value)
            continue
        except PhoneValidationError:
            pass

        try:
            birthday_obj = Birthday(detail)
            record.add_birthday(birthday_obj.value)
        except BirthdayValidationError:
            return (f"Argument {index}: '{detail}' is not a valid phone number or date of birth.")

    book.add_record(record)
    message = "Contact added."
    return message
    
@input_error
def change_phone(args, book):
    try:
        name, old_phone, new_phone = args
        record = book.find(name)
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for {name} updated."
    except RecordNotFoundError:
        return "Contact not found."
    except PhoneValidationError:
        return f"Invalid phone number format: '{new_phone}'."
    except Exception as e:
        return str(e)

@input_error
def show_phone(args, book):    
    name, *_ = args
    try: 
        record = book.find(name)
        phone_numbers = [str(phone) for phone in record.phones]
        return f"Phone numbers for {name}: " + ", ".join(phone_numbers)
    except RecordNotFoundError:
        return "Contact not found."

@input_error
def show_all_contacts(book):    
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(birthday)
    book.add_birthday(name, birthday)
    return f"Birthday for {name} added successfully."

@input_error
def show_birthday(args, book):
    name, *_ = args
    try:
        record = book.find(name)
        if record.birthday and str(record.birthday) != "No birthday set.":
            return f"{name}'s birthday is on {record.birthday}."
        return f"No birthday set for {name}."
    except RecordNotFoundError:
        return "Contact not found."

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        return "Upcoming birthdays: " + ", ".join(upcoming)
    return "No upcoming birthdays."