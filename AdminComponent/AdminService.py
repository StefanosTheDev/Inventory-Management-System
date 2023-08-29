from UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py
from sqlalchemy.orm.exc import NoResultFound
from UtilityComponent.UtilityService import UtilityService
from sqlalchemy.exc import SQLAlchemyError
from validate_email import validate_email
class AdminService:
    #**TODO Lets handle some casing. 
    #**TODO for this feature:
    
    
    #**TODO  (Username Features)
    def create_user_validation(username, password, email, role):
        if len(username) > 5 and len(username) < 12:
            print(f"{username} fits the length requirement")
        upper_lower_list = [letter for letter in username if letter.isupper() or letter.islower()]
        if upper_lower_list:
            print("this is valid")
        else: 
            print("this is not valid")
    
    #  5-12 charachters
    # - 1 Upper Case One LowerCase Letter
    # - Restrict Special Charachters
    # - No Spaces
    # - Uniquness. in the database
    # Make sure words like admin / support / owner are not able to be usernames
    
    
    
    #**TODO (Password Features)
    # 8 Charachters Special minimum . Max 15
    # 1 Upper Case 1 Lower Case
    # 1 Special Charachters
    # No Spaces
    
    #**TODO (Email Features)
    #
    #
    #
    #
    
    
    
    
    #**Password -> 8 charachters special.  (encrypt this )
    #** Email -> Make sure its a valid email
        #- Maybe it will take the Username, and generate a unique identifier for the Email. 
        # 
    #** Role Give an option to chose existing roles. if you just want to add to that hot key.
    #   - Maybe in this have a dictionary Key so they can see whats going on. 
    def create_user():
        session = Session()
        username = input("Username:")
        
        
        
        
        
        
        password = input("Password:")
        email = input("Email:")
        role = input("Role:")

        new_user = UserModel(username=username, password=password, email=email, role=role)
        session.add(new_user)
        session.commit()
        session.close()
        
        
        
        
    def display_users():
        session = Session()
        try: 
            all_users = session.query(UserModel).all()
            if not all_users:
                raise f"No users were found in the database"
            for user in all_users:
                  print(user.id, user.username, user.email, user.role)
        except Exception as error:
            print(error)
        print(all_users)
    def handle_user_input():
        request_id = input("Enter ID to search for (or type 'exit' to quit): ")  # Gets ID
        if not request_id:
                raise ValueError('Request Id is null')
        if request_id.lower() == 'exit':
            print('Exiting Program')
            exit()  # Leave Program
        parsedID = UtilityService.removeAllSpaces(request_id)  # Check for spaces. ID coming in
        try:
            return int(parsedID)  # This will raise a ValueError if conversion fails
        except ValueError:
            print("Invalid ID format. Please enter a numeric ID.")
            # Continues to the next iteration of the loop to prompt user again        
    def return_user_by_Id():
        while True:
            session = Session()
            try:
                parsedID = AdminService.handle_user_input()
                if parsedID is None:  # User wants to exit
                    break
                user = session.query(UserModel).filter_by(id=parsedID).first()  # database query
                if not user:
                    raise NoResultFound(f"No user found with the id {parsedID}")
                else:
                    print(user.user_object())
                    break  # Exit the loop

            except (NoResultFound, ValueError) as e:
                print(f"Error Message: {e}")
            except SQLAlchemyError as e:  # catch any SQLAlchemy related errors
                print(f"Database Error: {e}")
            finally:
                session.close()  # close the session
    
    
    