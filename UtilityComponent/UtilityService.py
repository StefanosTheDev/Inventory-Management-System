class UtilityService:
    def removeAllSpaces(value):
        filteredVariable = "".join(value.split())
        return filteredVariable
    
    def validate_input_for_Id(request_id):
        while True:
            if not request_id:
                print('Request Id is null')
                continue  # Go back to the start of the loop
            if request_id.lower() == 'exit':
                    break  # Exit the loop
            parsedID = UtilityService.removeAllSpaces(request_id)  # Check for spaces. ID coming in
            try:
                parsedID = int(parsedID)  # This will raise a ValueError if conversion fails
            except ValueError: 
                print(f"'{parsedID}' is not a valid integer ID.")
                continue  # Go back to the start of the loop
        return
