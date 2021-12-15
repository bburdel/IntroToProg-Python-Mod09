# ------------------------------------------------------------------------ #
# Title: Processing Classes Module
# Description: This module contains classes that work with data
# ChangeLog (Who,When,What):
# TODO: complete this header and ensure the content in the change log correct
# RRoot,1.1.2030,Created script
# RRoot,1.1.2030,Added pseudo-code
# BBurdelsky,12.12.21,Modified code to complete assignment 09
# ------------------------------------------------------------------------ #

class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BBurdelsky,12.12.2021,Used class code to create a module
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            # file = open(file_name, "r")  # this block of greyed out code, resulted in
            # for line in file:            # too many characters to strip and errors for me
            #     row = line.split(",")    # I used code that worked the previous week instead
            #     list_of_rows.append(row)
            # file.close()
            with open(file_name, "r") as file:
                lst_objs = file.read().splitlines()  # reads data from file into a list
                return lst_objs
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows


