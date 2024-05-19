#Account Display and User Database 
#use the WebSocket API for real-time updates
#user authentication to save user information into database 


from forms import RegistrationForm
from flask import Flask, render_template, redirect, request,url_for, jsonify, flash
from flask_pymongo import PyMongo 
import pymongo
from bson import ObjectId
from pymongo import MongoClient
import bcrypt
import datetime
from flask import request 

# import smtplib -> used for sending emails
app = Flask(__name__)
# add a secret key
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Disciples'

# db name is Disciples
client = MongoClient("mongodb://localhost:27017/Disciples")
db = client["Disciples"]
usersCollections = db["users"] #a table

# initializes PyMongo to Flask application
mongo = PyMongo(app)


# Disciples is the database name 
# users is the table name in the Disciples database



# route that handles user registration requests
# GET -> retrieves from server
# POST -> sends data to server to create or update a resource
@app.route('/register', methods=['GET','POST'])
#function to register user and log information into the database
def register(username, password):
    form = RegistrationForm()
    

    # checks if the form was submitted
    if form.validate_on_submit():
        # checks if the username already exists
        if not form.registerCheck():
            return jsonify({'message': 'Username already exists'}), 400

        if not form.validate_email(form.email.data):
            return jsonify({'message': 'Email already registered. Please use a different email address!'})
        

        # add user info to the database
        discipleData = {
            "firstName": form.firstName.data,
            "lastName": form.lastName.data,
            "userName" : form.username.data,
            "email" : form.email.data,
            "churchAffiliation" :form.church.data,
            "spiritualBirthday": form.spirthday.data.strftime('%Y-%m-%d'),
            "password": form.password.data
        }
            
        # how do i insert this data into the database?
        usersCollections.insert_one(discipleData)

        flash('Registered successfully!', 'success')
        # return redirect(url_for('home')) -> this would redirect to the home page when there is one

    
    flash('Invalid form data', 'danger')
    # return redirect(url_for('home'))

# for login page, use GET for rendering pages
# POST is used to submit data to the server (Flask)


@app.route('/')
def home():
    return render_template('home.html') #doesn't exist yet fr
#DATABASE

# Disciples is the database name 
# users is the table name in the Disciples database

