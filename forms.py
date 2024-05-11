from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import Flask, render_template, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


class registrationForm():
    # form fields and validators 
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #for church, i could actually just make a dropdown menu for the user to choose from ->so SelectField would be used
    church = SelectField('Church', validators=[DataRequired(), Length(min=3, max=20)])

    def registerCheck(username):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["disciples"]
        usersCollection = db["users"]

        user = usersCollection.find_one({"username":username})

        if user:
            return False #username exists 
        else:
            return True
        

        
#right now, my logic is to set up the table in the routes.py file while this file
#will only check if the user already exists.
#how will i collect the other info such as church, password, spirthday to be inserted into the database?
