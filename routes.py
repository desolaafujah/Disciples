#Account Display and User Database 
#use the WebSocket API for real-time updates
#user authentication to save user information into database 


from forms import registrationForm
from flask import Flask, render_template, redirect, request, jsonify, flash
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
@app.route('/register', methods=['POST'])
#function to register user and log information into the database
def register(username, password):
    form = registrationForm(request.form)

    # check if the username already exists
    if form.validate_on_submit():
        if not form.registerCheck(form.username.data):
            return jsonify({'message': 'Username already exists'}), 400

    

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

