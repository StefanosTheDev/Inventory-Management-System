
import pytest
from unittest import mock
from Components.UtilityComponent.UtilityService import UtilityService

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
    def test_check_username_min_length(self):
        with pytest.raises(ValueError, match="Error with length of username"):
            UtilityService.check_username('') 

    def test_check_username_max_length(self):
        with pytest.raises(ValueError, match="Error with length of username"):
            UtilityService.check_username('assdfsdfsdfsdff') 

    def test_check_upperCase_noLower(self):
        with pytest.raises(ValueError, match="Issue here with casing"):
            UtilityService.check_username("AAAAAAA")
        
    def test_check_lowerCase_noUpper(self):
        with pytest.raises(ValueError, match="Issue here with casing"):
            UtilityService.check_username("aaaaaaaa")        
        
    def test_check_username_sucess(self):
        result = UtilityService.check_username("Stefanos")
        assert result == True

#check_password()
class Test_Check_Password():
    def test_check_min_length(self):
        pass
    def test_check_max_length(self):
        pass
    def test_check_upperCase_noLower(self):
        pass
    def test_check_lowerCase_noUpper(self):
        pass
    def test_number_doesnt_exist(self):
        pass
    def test_no_special_charachter(self):
        pass
    def test_password_sucess_attempt(self):
        pass
    
