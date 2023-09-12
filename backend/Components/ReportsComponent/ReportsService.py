from Components.AdminComponent.AdminModel import UserModel
from Components.AdminComponent.AdminService import AdminService
from flask import jsonify, session
from extension import db



class ReportService:
    def employee_report_by_role():
        try: 
            users = AdminService.display_users()
            print(users)
        except:
            pass
        
    
    ## To get the employee information.
    ## I am going to maybe want to iterate through the users for the defined role
    ## I am going to add them to a reports list to pull the users.
    ## Ill add this data to a CSV file. to the local downloads folder. 
    