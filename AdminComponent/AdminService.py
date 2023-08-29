from UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py
from sqlalchemy.orm.exc import NoResultFound
from UtilityComponent.UtilityService import UtilityService
from sqlalchemy.exc import SQLAlchemyError

class AdminService:
    
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
    def get_user_input():
        request_id = input("Enter ID to search for (or type 'exit' to quit): ")  # Gets ID
        if not request_id:
                raise ValueError('Request Id is null')
        if request_id.lower() == 'exit':
        return None  # Signal to the caller that the user wants to exit
    parsedID = UtilityService.removeAllSpaces(request_id)  # Check for spaces. ID coming in
    return int(parsedID)  # This will raise a ValueError if conversion fails

def return_user_by_Id():
    while True:
        session = Session()
        try:
            parsedID = get_user_input()
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

    
    