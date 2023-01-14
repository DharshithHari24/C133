#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is DH Learning"

#Define a function with different endpoint

@app.route("/flask_2")
def second_flask():
    return "DH is the online tution for all student's who need to learn cubing!"

#run using debug argument
app.run(debug=True)