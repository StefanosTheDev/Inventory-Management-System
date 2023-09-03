from Components.UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py
from sqlalchemy.orm.exc import NoResultFound
from Components.UtilityComponent.UtilityService import UtilityService
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify
from validate_email import validate_email

class AdminService:
    
    from flask import jsonify

    def create_user(username, password, email, role):
        try:
            session = Session()
            validated_username = UtilityService.check_username(username)
            validated_pass = UtilityService.check_password(password)
            validated_email = UtilityService.check_email_exist(email)
        
            new_user = UserModel(username=validated_username, password=validated_pass, email=validated_email, role=role)
            session.add(new_user)
            session.commit()
            user_dict = new_user.user_object()  # Convert to dict within session's scope
            session.close()
            return jsonify(user_dict)
    
        except Exception as e:
            print(f"Could not add this user: {username} to the database", e)
            return jsonify({"error": "Unable to create user"}), 500  # Returning a 500 Internal Server Error with a message

    def display_users():
        session = Session()
        try: 
            all_users = session.query(UserModel).all()
            if not all_users:
                raise f"No users were found in the database"
            for user in all_users:
                  print(user.id, user.username, user.email, user.role)
            return jsonify(all_users)
        except Exception as error:
            print(error)
        print(all_users)
        
    def return_employee_by_Id(id):
        while True:
            session = Session()
            try:
                parsedID = UtilityService.Id_Req_Validation(id)
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
    
    def update_user(id):
        session = Session()
        try:
            user = AdminService.return_employee_by_Id(id)
            print(user)
        except:
            pass
        
            
    
    
    
    