class AddressBookException(Exception):
    pass

class PhoneValidationError(AddressBookException):
    def __init__(self, message="Invalid phone number. It must contain exactly 10 digits."):
        self.message = message
        super().__init__(self.message)

class RecordNotFoundError(AddressBookException):
    def __init__(self, message="Record not found."):
        self.message = message
        super().__init__(self.message)

class BirthdayValidationError(AddressBookException):
    def __init__(self, message="Invalid date format. Use DD.MM.YYYY"):
        self.message = message
        super().__init__(self.message)

class RecordAlreadyExistsError(AddressBookException):
    def __init__(self, message="Record already exists in the address book."):
        self.message = message
        super().__init__(self.message)