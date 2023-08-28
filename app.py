from Database.db_setup import setup_db, Session
from UserComponent.UserModel import UserModel
from AdminComponent.AdminService import AdminService

def main():
    print("Setting up the database...")
    setup_db()

    print("Welcome to the console version of this Inventory Management System.")
    print("Here is the key for the application")
    print("If you are an Admin type 'Admin', if you are an employee type 'Employee'. To exit, type 'Exit'.")

    while True:  # Main loop for role selection
        print("To Enter Admin Portal Type (Admin):")
        print("To Enter Employee Portal Type (Employee):")
        print("To Exit type (exit)")
        choice = input("To Enter Admin Portal Type (Admin): ")

        if choice == "Admin":
            print("Welcome to the Admin Portal. Please Login to verify credentials")

            # Placeholder for credential validation
            is_valid = True  

            if is_valid:
                while True:  # Nested loop for CRUD operations inside Admin block
                   
                    print("\nAdmin Options:")
                    print("1. Create User")
                    print("2. Display Users")
                    print("3. Find by Id")
                    print("4. Exit Admin Protal")

                    next_choice = input("Choose an option: ")

                    if next_choice == "1":
                        AdminService.create_user()
                    elif next_choice == "2":
                        AdminService.display_users()
                    elif next_choice == "3":
                        AdminService.return_user_by_Id()
                    elif next_choice == "4":
                        print("Exiting Admin Portal...")
                        break  # Exit the nested CRUD loop to go back to main loop
                    else:
                        print("Invalid choice. Please select again.")

        elif choice == "Employee":
            # Handle employee actions here
            pass

        elif choice.lower() == "exit":
            print("Exiting program...")
            break  # Exit the main loop

        else:
            print("Invalid choice. Please select again. #")

if __name__ == "__main__":
    main()
