from flask_app import app
import flask_app.controllers.users   # user the import flask_app.controllers to map the folder down the file at the end. 


if __name__ == "__main__":
    app.run(debug=True)
