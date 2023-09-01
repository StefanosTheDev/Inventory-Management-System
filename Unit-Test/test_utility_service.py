
import pytest
from unittest import mock
from Components.UtilityComponent.UtilityService import UtilityService
from email_validator import EmailNotValidError
#removeAllSpaces()
class Test_Remove_All_Spaces:
    def test_removeAllSpaces_simple_string(self):
        foo = " asdflkjsdf "
        result = UtilityService.removeAllSpaces(foo)
        assert result == "asdflkjsdf"

    def test_removeAllSpaces_no_spaces(self):
        foo = "asdflkjsdf"
        result = UtilityService.removeAllSpaces(foo)
        assert result == "asdflkjsdf"

    def test_removeAllSpaces_multiple_spaces(self):
        foo = "a s  d f lk j sd f"
        result = UtilityService.removeAllSpaces(foo)
        assert result == "asdflkjsdf"

    def test_removeAllSpaces_empty_string(self):
        foo = ""
        result = UtilityService.removeAllSpaces(foo)
        assert result == ""

#check_username()
class Test_Check_Username:
    def test_check_username_min(self):
        with pytest.raises(ValueError, match="Error with length of username"):
            UtilityService.check_username('') 
            
    def test_check_username_max(self):
        with pytest.raises(ValueError, match="Error with length of username"):
            UtilityService.check_username('assdfsdfsdfsdff') 
    
    def test_check_casing_upper_lower(self):
        with pytest.raises(ValueError, match="Issue here with casing"):
            UtilityService.check_username("AAAAAAA")
    def test_check_casing_lower(self):
         with pytest.raises(ValueError, match="Issue here with casing"):
            UtilityService.check_username("aaaaaaaa")   
    def test_check_username_sucess(self):
        result = UtilityService.check_username("Stefanos")
        assert result == True

#check_password()
class Test_Check_Password():
    def test_check_password_min_length(self):
        with pytest.raises(ValueError, match="Length Issue"):
            UtilityService.check_password('f')
            
    def test_check_password_max_length(self):
          with pytest.raises(ValueError, match="Length Issue"):
            UtilityService.check_password('fasdfasdfasdfsdfsdfsdfsdfsdfsdfsdf')
            
    def test_check_password_upperCase_noLower(self):
          with pytest.raises(ValueError, match="whoa no casing matches"):
            UtilityService.check_password('SSSSSSSSS')
            
    def test_check_password_lowerCase_noUpper(self):
         with pytest.raises(ValueError, match="whoa no casing matches"):
            UtilityService.check_password('sssssssss')
    
    def test_check_password_num_doesnt_exist(self):
         with pytest.raises(ValueError, match="no numbers"):
            UtilityService.check_password('Sssssfsf')
            
    def test_check_password_no_special_charachter(self):
         with pytest.raises(ValueError, match="no Character"):
            UtilityService.check_password('32Sfsfsfd')
            
    def test_check_password_sucess_attempt(self):
        result = UtilityService.check_password('!Stefanos329')
        assert result == True

class Test_check_email_exist():
    def test_check_email_exist(self):
        Email = UtilityService.check_email_exist('Stefanos26Sophocleous@gmail.com')
        assert Email == True
    def test_check_email_does_not_exist(self):
        with pytest.raises(EmailNotValidError):
            UtilityService.check_email_exist('invalid-email')
    
class Test_Id_Req_Validation():
    def test_Id_Req_Validation_Id_Null(self):
        with pytest.raises(ValueError, match="Request Id is null"):
            UtilityService.Id_Req_Validation(None)
            
    def test_Id_Req_Validation_Invalid_Format(self):
        with pytest.raises(ValueError, match="Invalid ID format. Please enter a numeric ID."):
            UtilityService.Id_Req_Validation('s3213')
            
        with pytest.raises(ValueError, match="Invalid ID format. Please enter a numeric ID."):
            UtilityService.Id_Req_Validation('!  f333 33')
            
    def test_Id_Req_Validation_Valid_Format(self):
        foo = "3"
        test_id = UtilityService.Id_Req_Validation(foo)
        assert type(test_id) == int
    
    
