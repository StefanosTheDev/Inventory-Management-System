from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)  # Simplified for auto-increment
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  # Consider hashing the password!
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(50), nullable=False)

    def __init__(self, username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def user_object(self):
         return {
        'User_Information': {
            'user_id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email
            #'blogs': [blog.json() for blog in self.blog_id]
        },
        
    }
