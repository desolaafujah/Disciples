from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pymongo import MongoClient
from datetime import date


class registrationForm():
    maxDate = date.today()

    # form fields and validators 
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #for church, i could actually just make a dropdown menu for the user to choose from ->so SelectField would be used
    church = SelectField('Church', validators=[DataRequired()], choices = [
        # ('value', 'label') -> format
        #value is to be submitted with the form
        #label is what the user sees in the dropdown menu 
        ('ABQ ICC', 'Albuquerque'),
        ('ATL ICC', 'Atlanta'),
        ('AUB ICC', 'Auburn'),
        ('BR ICC', 'Baton Rouge'),
        ('BOI ICC', 'Boise'),
        ('BOS ICC', 'Boston'),
        ('BZN ICC', 'Bozeman'),
        ('BRK ICC', 'Brookings'),
        ('BUR ICC', 'Burlington'),
        ('CB ICC', 'Casco Bay'),
        ('CHI ICC', 'Chicago'),
        ('COA ICC', 'City of Angels'),
        ('COL ICC', 'Columbus'),
        ('DFW ICC', 'Dallas/Ft. Worth'),
        ('DB ICC', 'Daytona Beach'),
        ('DEL ICC', 'Delaware')
        ('DEN ICC', 'Denver'),
        ('DET ICC', 'Detroit'),
        ('EUG ICC', 'Eugene'),
        ('FYT ICC', 'Fayetteville')
        ('FRE ICC', 'Fresno'),
        ('GNV ICC', 'Gainesville'),
        ('HFD ICC', 'Hartford'),
        ('HLO ICC', 'Hilo'),
        ('HNL ICC', 'Honolulu'),
        ('HOU ICC', 'Houston'),
        ('IND ICC', 'Indianapolis'),
        ('IOW ICC', 'Iowa City'),
        ('KC ICC', 'Kansas City'),
        ('KNO ICC', 'Knoxville'),
        ('KON ICC', 'Kona'),
        ('LAR ICC', 'Laramie'),
        ('LV ICC', 'Las Vegas'),
        ('LIN ICC', 'Lincoln'),
        ('LOU ICC', 'Louisville'),
        ('MCH ICC', 'Manchester'),
        ('MIA ICC', 'Miami / Ft. Lauderdale'),
        ('MIL ICC', 'Milwaukee'),
        ('MSP ICC', 'Minneapolis / St. Paul'),
        ('NYC ICC', 'New York City'),
        ('OKC ICC', 'Oklahoma'),
        ('ORL ICC', 'Orlando'),
        ('PHL ICC', 'Philadelphia'),
        ('PHX ICC', 'Phoenix'),
        ('PDX ICC', 'Portland'),
        ('PRO ICC', 'Providence'),
        ('SAC ICC', 'Sacramento City'),
        ('SLC ICC', 'Salt Lake City'),
        ('SD ICC', 'San Diego'),
        ('SFB ICC', 'San Francisco Bay'),
        ('SEA ICC', 'Seattle'),
        ('STL ICC', 'St. Louis'),
        ('SYC ICC', 'Syracuse'),
        ('TPA ICC', 'Tampa Bay'),
        ('TTL ICC', 'Thomasville & Tallahassee'),
        ('TUS ICC', 'Tucson'),
        ('TUSC ICC', 'Tuscaloosa'),
        ('DC ICC', 'Washington D.C.')
    ])

    # raises an error if date selected is in the future
    def validSpirthday(form):
        if form.spirthday.data > date.today():
            raise ValidationError('Spirthday cannot be in the future lol')

    spirthday = DateField('Spirthday', validators=[DataRequired(), validSpirthday])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    #checks is a user already exists
    def registerCheck(username):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["disciples"]
        usersCollection = db["users"]

        user = usersCollection.find_one({"username":username})

        if user:
            return False #username exists 
        else:
            return True
        


    # cretae function for returning users -> login page

    # def login(username):

        

        
#right now, my logic is to set up the table in the routes.py file while this file
#will only check if the user already exists.
#how will i collect the other info such as church, password, spirthday to be inserted into the database?
