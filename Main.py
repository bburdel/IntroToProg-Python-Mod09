# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# BBurdelsky,12.12.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    import ProcessingClasses as procC
    from IOClasses import EmployeeIO
else:
    raise Exception("This file was not created to be imported.")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# list_of_employees = []
strFileName = "EmployeeData.txt"

# Load data from file into a list of employee objects when script starts
list_of_employees = procC.FileProcessor.read_data_from_file(strFileName)
print(list_of_employees)

# Show user a menu of options
while True:
    EmployeeIO.print_menu_items()

# Get user's menu option choice
    menu_select = EmployeeIO.input_menu_options()

    # Show user current data in the list of employee objects
    if menu_select.strip() == '1':
        EmployeeIO.print_current_list_items(list_of_employees)

    # Let user add data to the list of employee objects
    elif menu_select.strip() == '2':
        EmployeeIO.input_employee_data(lst_of_employees=list_of_employees)

    # let user save current data to file
    elif menu_select.strip() == '3':
        procC.FileProcessor.save_data_to_file(strFileName, list_of_employees)

    # Let user exit program
    elif menu_select.strip() == '4':
        print("Good Bye!")
        break

# Main Body of Script  ---------------------------------------------------- #
