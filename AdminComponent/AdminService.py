from UserComponent.UserModel import UserModel
from Database.db_setup import Session  # Assuming Session is exposed from db_setup.py

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
        
    def delete_user_by_Id():
        pass