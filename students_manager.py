import datetime

"""
final.py
This program allows the user to manage students of the CODE university of applied sciences.
@author Niklas Donges
@version 2018-09-19
"""


class People:
    num_of_people = 0

    # Constructor
    def __init__(self, first_name, last_name, date_of_birth, gender, nationality, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = '{} {}'.format(self.first_name, self.last_name)

        self.email = first_name.lower() + "." + last_name.lower() + "@code.berlin"

        self.date_of_birth = date_of_birth
        self.day_of_birth, self.month_of_birth, self.year_of_birth = self.date_of_birth.split('/')

        self.gender = gender
        self.nationality = nationality

        self.phone = phone

        People.num_of_people += 1

    # Accessor Methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_day_of_birth(self):
        return self.day_of_birth

    def get_month_of_birth(self):
        return self.month_of_birth

    def get_year_of_birth(self):
        return self.year_of_birth

    def get_gender(self):
        return self.gender

    def get_nationality(self):
        return self.nationality

    def get_phone(self):
        return self.phone

    # Mutator Methods
    def set_email(self, new_email):
        self.email = new_email

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_nationality(self, new_nationality):
        self.nationality = new_nationality

    def set_phone(self, new_phone_number):
        self.phone = new_phone_number

    # Functions from Object - overrides: print(friend_1)
    def __str__(self):
        return "Person: " + self.full_name + \
               ", Email: " + self.email + \
               ", Date of Birth: " + self.date_of_birth + \
               ", Gender: " + self.gender + \
               ", Nationality: " + self.nationality + \
               ", Phone: " + self.phone


def enter_person():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    date_of_birth = input("Enter Date of Birth: ")
    gender = input("Enter gender (male or female): ")
    nationality = input("Enter nationality: ")
    phone = input("Enter phone number: ")
    return People(first_name, last_name, date_of_birth, gender, nationality, phone)


def search_person(persons):
    found = False
    name = input("Enter a name to lookup: ")

    for person in persons:
        if name in person.get_full_name():
            print(person)
            found = True
    if not found:
        print("No students match that name.")


def show_all_persons(persons):
    print("Showing all persons: ")
    for person in persons:
        print(person)


def main():
    persons = []
    running = True
    while running:
        print("\nStudents Manager")
        print("1) new student \t 2) lookup")
        print("3) show all \t 4) end ")
        option = input(">")

        if option == "1":
            persons.append(enter_person())
        elif option == "2":
            search_person(persons)
        elif option == "3":
            show_all_persons(persons)
        elif option == "4":
            running = False
        else:
            print("Unrecognized input. Please try again.")
    print("Program ending.")
print("ujfjfjf")

if __name__ == "__main__":
    main()
