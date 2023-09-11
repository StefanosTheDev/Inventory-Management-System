from flask import Flask
from extension import db
from Components.AdminComponent.AdminController import admin_blueprint
from Components.InventoryComponent.InventoryController import inventory_blueprint
app = Flask(__name__, static_folder='static')  # Set the static folder

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress a warning message
app.secret_key = 'your_super_secret_key'  
# Initialize the database
db.init_app(app)

app.register_blueprint(admin_blueprint)
app.register_blueprint(inventory_blueprint)


@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
