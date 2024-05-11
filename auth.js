const express = require('express'); //imports express.js framework to create web server and define routes
const router = express.Router(); //creates an instance of the express router to define routes and middleware separately and apply to main app
const bcrypt = require('bcrypt'); //imports bcrypt library used for hashing passwords securely
const jwt = require('jsonwebtoken'); //imports the jsonwebtoken library used for JSON Web Tokens for authentication
const User = require('../models/User'); //TODO: define a user schema and model using Mongoose (mongodb object modeling tool)

import React from 'react';
// this will be file for authentication
//handle form submission using axios


// this is a function component 
const Authenticate = ()=> {
    return (
        <div>
            <h2>Authenticate</h2>
            
            {/** */}
        </div>
    );
};

export default Authenticate;