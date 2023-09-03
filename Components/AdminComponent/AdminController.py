from flask import Blueprint
from Components.AdminComponent.AdminService import AdminService

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin_home', methods=['GET'])
def admin_home_page():
    pass

def admin_employee_page():
    pass
@admin_blueprint.route('/user/admin/employees')
def admin_get_employees():
    return AdminService.display_users()
@admin_blueprint.route('/user/admin/<string:username>/<string:password>/<string:email>/<string:role>')
def admin_create_employee(username, password, email, role):
    return AdminService.create_user(username, password, email, role)

def admin_update_employee():
    pass

def admin_delete_employee():
    pass

def admin_create_inventory_table():
    pass

def admin_delete_inventory_table():
    pass

def admin_update_inventory_table():
    pass

