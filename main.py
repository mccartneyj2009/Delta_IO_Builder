import odbcConn as delta
import readCSV


def intro():
    while True:
        print("""
Please select one of the following options: \n
1) Create points from CSV file
2) View existing points in controller
3) Open the ODBC 32-bit Driver Manager\n
        """)
        try:
            user_input = int(input())
            if user_input == 1 or user_input == 2 or user_input == 3:
                return user_input
                break
            else:
                print("Invalid selection. Please select 1, 2, or 3\n")
        except:
            print("Can only accept numerical values.\n")

while True:
    operation = intro()
    if operation == 1:
        validSource = delta.verify_dsn_source()
        if validSource:
            delta.create_points()
        else:
            print("No valid datasource. Please ensure you are running Delta ODBC 4 and that it matches your workstation "
                  "version number.")
        input("Press 'Enter' to exit.")
        break
    elif operation == 2:
        delta.view_controller_points()
        input("Press 'Enter' to exit.")
        break
    elif operation == 3:
        delta.open_driver()
