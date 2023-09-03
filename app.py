from flask import Flask, render_template
from Components.AdminComponent.AdminController import admin_blueprint
from Components.HomeComponent.HomeController import home_blueprint

app = Flask(__name__, static_folder='static')  # Set the static folder

app.register_blueprint(admin_blueprint)
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
