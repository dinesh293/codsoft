class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

