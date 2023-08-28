class UtilityService:
    def removeAllSpaces(value):
        filteredVariable = "".join(value.split())
        return filteredVariable
    
    def can_be_integer(x):
        try:
            int(x)
            return True
        except ValueError:
            return False
            
    
    