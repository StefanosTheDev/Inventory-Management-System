from UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py
from sqlalchemy.orm.exc import NoResultFound
from UtilityComponent.UtilityService import UtilityService
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
    def return_user_by_Id():
        session = Session()
        try:
            request_id = input("Enter ID to search for") # Gets ID 
            UtilityService.removeAllSpaces(request_id) # Check for spaces. ID comming in
            #if request_id:
              #  convert_Id_To_Int = int(request_id) # I need to check if this could be converted
            print(f"Request ID {request_id}")
              #   int(x)
          #  return True
      #  except ValueError:
         #   return False
            
           # UtilityService.can_be_integer(request_id) # Make sure this can be an integer. 
            user = session.query(UserModel).filter_by(id=request_id).first()
            if not user: 
                raise NoResultFound(f"No user found with the id {request_id}")
            return print(user.user_object())
        except(NoResultFound) as e:
            print(f"Error Message: {e}")
        
    
    