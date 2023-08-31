    
from email_validator import validate_email, EmailNotValidError
import warnings
class UtilityService:
    warnings.simplefilter(action='ignore', category=DeprecationWarning)
    
    def removeAllSpaces(value):
        filteredVariable = "".join(value.split())
        return filteredVariable
    
    def check_username(username):
        try:
            if 5 < len(username) > 12: #Checks Length Requirement
                raise ValueError("Error with length of username")
            check_user_casing = [letter.isupper() and letter.islower() for letter in username] #Checks Casing
            if not True in check_user_casing:
                raise ValueError("Issue here with casing")
            return True
        except Exception as e:
            print(f"Error", e)
    
    def check_password(password):
        try:
            SPECIAL_CHARACHTERS = "!@#$%^&*"
            if not 5 < len(password) > 15:
                raise ValueError('Length Issue')
        
            check_pass_casing = [letter.isupper() and letter.islower()for letter in password] #Checks Casing
            if not True in check_pass_casing:
                raise ValueError("whoa no casing matches")
        
            if not any(char.isdigit() for char in password):
                raise ValueError("no numbers")
        
            if not any(char in SPECIAL_CHARACHTERS for char in password):
                raise ValueError("no Character")
        
            return True #
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

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