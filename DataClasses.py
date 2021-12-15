# ------------------------------------------------------------------------ #
# Title: Data Classes Module
# Description: This module contains classes that work with data
# ChangeLog (Who,When,What):
# TODO: complete this header and ensure the content in the change log correct
# RRoot,1.1.2030,Created script for Assignment 08
# RRoot,1.1.2030,Added pseudo-code for Assignment 08
# BBurdelsky,12.12.21,Modified code to complete assignment 09
# ------------------------------------------------------------------------ #

# statement that checks to see if code is being run in the main file
if __name__ == "__main__":
    raise Exception("This module is not meant to run by itself.")


class Person:
    """Stores data about a persons:

    properties:
        first_name: (string) with the persons's first name

        last_name: (string) with the persons's last name
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BBurdelsky,12.12.2021,Modified class to create module file
    """


    # Constructor
    def __init__(self, first_name, last_name):
        # Attributes
        self.first_name = first_name  # public attributes make them subject to validation code
        self.last_name = last_name

    # Properties
    @property  # gets the attribute value
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter  # sets the attribute value
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("The name cannot be numbers.")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("The name cannot be numbers.")

    # Methods
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ',' + self.last_name


class Employee(Person):  # Inherits from Person Class
    """Stores data about an Employee:

    properties:
        employee_id: (int) with the employees's ID

        first_name: (string) with the employees's first name

        last_name: (string) with the employees's last name

    methods:
        to_string() returns comma separated product data (alias for __str__())

    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        BBurdelsky,12.12.2021,Created Module file (DataClasses.py) using Class code
    """

    def __init__(self, employee_id, first_name, last_name):
        # Attributes
        # super().__init__(first_name, last_name)  # Suggested line added from PyCharm
        self.employee_id = employee_id  # public attributes make them subject to validation
        self.first_name = first_name
        self.last_name = last_name

    # --Properties--
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not str(value).isnumeric():
            raise Exception("IDs must be numbers")
        else:
            self.__employee_id = value

    # --Methods--
    def to_string(self):  # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()  # get data (first and last name) from parent(super) class
        return str(self.employee_id) + ',' + data

    def __str__(self):  # Overrides the original method (polymorphic)
        """ Implicitly returns field data """
        data = super().__str__()  # get data (first and last name) from parent(super) class
        return str(self.employee_id) + ',' + data
    # --End of Class --
