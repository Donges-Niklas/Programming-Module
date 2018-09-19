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
        self.day_of_birth, self.month_of_birth, self.year_of_birth = self.date_of_birth.split('-')

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
