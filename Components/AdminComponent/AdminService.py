from Components.UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py
from sqlalchemy.orm.exc import NoResultFound
from Components.UtilityComponent.UtilityService import UtilityService
from sqlalchemy.exc import SQLAlchemyError
from validate_email import validate_email
class AdminService:
    
    def create_user():
        try:
            session = Session()
            
            username = input("Enter Employee Name:") 
            password = input("Enter Employee Password:")
            email = input("Enter Employee Email:")
            role = input("Enter Employee Role:")
            validated_username = UtilityService.check_username(username)
            validated_pass = UtilityService.check_password(password)
            validated_email = UtilityService.check_email_exist(email)
            
            new_user = UserModel(username=validated_username, password=validated_pass, email=validated_email, role=role)
            session.add(new_user)
            session.commit()
            session.close()
            return new_user
    
        except Exception as e:
            print(f" Could not add this user: {new_user.username} to the database")

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
        
    def return_employee_by_Id():
        while True:
            session = Session()
            try:
                request_id = input("Please enter a valid ID")
                parsedID = UtilityService.Id_Req_Validation(request_id)
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
    
    def update_user():
        pass
    
    
    