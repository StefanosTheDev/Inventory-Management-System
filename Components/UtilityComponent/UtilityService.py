    
from email_validator import validate_email, EmailNotValidError
import warnings
class UtilityService:
    warnings.simplefilter(action='ignore', category=DeprecationWarning)
    
    def removeAllSpaces(value):
        filteredVariable = "".join(value.split())
        return filteredVariable
    
    def check_username(username):
        try:
            # If NOT between 6 and 12 Raise the error.
            if len(username) <= 5 or len(username) > 12:
                raise ValueError("Error with length of username") 
                
            has_upper = any(letter.isupper() for letter in username) # Returns True / False
            has_lower = any(letter.islower() for letter in username) # REturns True / False
            
            if not(has_upper and has_lower): 
                raise ValueError("Issue here with casing")
            return True
        except ValueError as e:
            print(e)
            raise # re-raises the caught ValueError Is this best practice?

    
    def check_password(password):
        try:
            SPECIAL_CHARACHTERS = "!@#$%^&*"
            if len(password) <= 5 or len(password) > 16:
                raise ValueError('Length Issue')
        
            has_upper = any(letter.isupper() for letter in password) # Returns True / False
            has_lower = any(letter.islower() for letter in password) # REturns True / False
            if not (has_upper and has_lower):
                raise ValueError("whoa no casing matches")
        
            if not any(char.isdigit() for char in password):
                raise ValueError("no numbers")
        
            if not any(char in SPECIAL_CHARACHTERS for char in password):
                raise ValueError("no Character")
        
            return True #
        except ValueError as e:
            print(e)
            raise 

    def check_email_exist(email):
        try:
      # validate and get info
            v = validate_email(email)
        # replace with normalized form
            email = v["email"] 
            print("True")
        except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
            print(str(f"{e} ERror"))
  
    def Id_Req_Validation(request_id):
        if not request_id:
                raise ValueError('Request Id is null')
        if request_id.lower() == 'exit':
            print('Exiting Program')
            exit()  # Leave Program
        parsedId = "".join(request_id.split())
        try:
            return int(parsedId)  # This will raise a ValueError if conversion fails
        except ValueError:
            print("Invalid ID format. Please enter a numeric ID.")
            # Continues to the next iteration of the loop to prompt user again      