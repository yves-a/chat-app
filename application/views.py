from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .msg_database import Database
view = Blueprint("views", __name__)

# CONSTANTS DO NOT KNOW WHAT THEY DO
NAME_KEY = "name"


@view.route("/login", methods=["GET","POST"])
def login():
    '''
    Allows the user to setup a name to use in the chat room
    '''
    # Checks to see if the user has inputted a name
    if request.method == "POST":
        user_name = request.form["inputName"]
        print(user_name)
        if len(user_name) > 1:
            session["name"] = user_name
            print(session)
            flash("You have successfully logged in using the name: " +user_name)
            print(session)
            return redirect(url_for("views.home"))
        else:
            flash("Username needs to be longer than 1 character")
    
    return render_template("login.html", **{"session":session})

@view.route("/logout")
def logout():
    '''
    Removes the username from the session
    '''
    session.pop("username", None)
    flash("You have successfully logged out")
    return redirect(url_for("views.login"))

@view.route("/")
@view.route("/home")
def home():
    '''
    Shows the main page
    '''
    if "name" not in session:
        print("Hello?")
        return redirect(url_for("views.login"))
    print("hello")
    return render_template("index.html")

@view.route("/get_name")
def get_name():
    '''
    Gets the name of the user
    '''
    name_data = {"name":""}
    if "name" in session:
        name_data = {"name":session["name"]}

    print(name_data)    
    return name_data

@view.route("/get_messages")
def get_msg():
    '''
    gets all the messages from the database
    '''
    db = Database()
    messages = db.get_all_msg(2)
    messages = ""
    return jsonify(messages)