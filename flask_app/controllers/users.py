from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import (
    User,
)  # use the import path  from pagackage.folder.file <import whats in the file>

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user", methods=["POST"])
def create_user():

    User.create(request.form)
    return redirect("/users")

@app.route('/users/<int:user_id>')
def user_details(user_id):
    """ this route displays one user """
    user = User.find_by_id(user_id)
    return render_template("user.html", user=user)


@app.route("/users")
def get_all():
    users = User.get_all()

    return render_template("results.html", all_users=users)


@app.route("/users/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    print ("IN THE USER UPDATE")
    user_id = request.form['user_id']
    User.update_user(request.form)
    return redirect(f'/users/{user_id}')


@app.route("/user_edit/<int:user_id>")
def edit_user(user_id):

    user = User.find_by_id(user_id)
    if user == None:
        return "Cannon find User."
    return render_template("edit_user.html", user=user)


@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    """ this route deletes user"""
    User.delete_user(user_id)
    return redirect('/users')
