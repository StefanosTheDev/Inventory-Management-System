from flask import Blueprint, request, jsonify, session
from functools import wraps
from Components.AdminComponent.AdminService import AdminService

admin_blueprint = Blueprint('admin', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return jsonify({"error": "Access denied: You're not logged in!"}), 403
        return f(*args, **kwargs)
    return decorated_function

@admin_blueprint.route('/admin/employees', methods=['GET'])
@login_required
def admin_get_employees():
     return AdminService.display_users()

@admin_blueprint.route('/admin/update/<int:id>', methods=['PUT'])
def admin_update_employee(id):  # You need to include the 'id' parameter here.
    try:
        data = request.get_json()
        updatedUsername = data.get('username')
        updatedPass = data.get('password')
        updatedEmail = data.get('email')
        updatedRole = data.get('role')

        if not all([updatedUsername, updatedPass, updatedEmail, updatedRole]):
            return jsonify({"error": "All fields are required!"}), 400

        return AdminService.update_user(id, updatedUsername, updatedPass, updatedEmail, updatedRole)  # Pass all required parameters here.
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@admin_blueprint.route('/admin/create', methods=['POST'])
def admin_create_employee():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role')

        if not all([username, password, email, role]):
            return jsonify({"error": "All fields are required!"}), 400

        return AdminService.create_user(username, password, email, role), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@admin_blueprint.route('/admin/delete/<int:id>', methods=['DELETE'])
def admin_delete_employee_by_Id(id):
    return AdminService.delete_user_by_Id(id)

@admin_blueprint.route('/admin/login', methods=['POST'])
def admin_login():
    try: 
        data = request.get_json()

        if not data:
            return jsonify({"message": "No data provided"}), 400

        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"message": "Username and password are required!"}), 400

        return AdminService.login(username, password)
    except Exception as error:
        return jsonify({"Login Error": str(error)}), 500
    
@admin_blueprint.route('/admin/logout', methods=['POST'])
def admin_logout():
    return AdminService.logout()