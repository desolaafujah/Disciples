#Account Display and User Database 
#use the WebSocket API for real-time updates
#user authentication to save user information into database 


from forms import registerCheck, registrationForm
from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo 
import pymongo
from bson import ObjectId
from pymongo import MongoClient
import bcrypt
import datetime 

# import smtplib -> used for sending emails

# db name is Disciples
client = MongoClient("mongodb://localhost:27017/Disciples")



app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Disciples'

# initializes PyMongo to Flask application
mongo = PyMongo(app)
db = client["Disciples"]



# route that handles user registration requests
@app.route('/register', methods=['POST'])
#function to register user and log information into the database
def register(username, password):
    if registerCheck(username):
        form = registrationForm()
        # add user info to the database
        usersCollections = db["users"]
        # Disciples is the database name 
        # users is the table name in the Disciples database
        discipleData = {

        }



    else:
        print("Username already exists")
        #could also do the flash message thing

# for login page, use GET for rendering pages
# POST is used to submit data to the server (Flask)



#DATABASE

# Disciples is the database name 
# users is the table name in the Disciples database

