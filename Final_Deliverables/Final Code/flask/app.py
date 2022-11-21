import pickle
from flask import Flask, jsonify, render_template, request,redirect,url_for,request

#importing the inputScript file used to analyze the URL import inputScript
import inputScript
import numpy as np
import sklearn

from flask import Flask, render_template, request, redirect, url_for, session

from flask_mysqldb import MySQL

import MySQLdb.cursors

import re
 
 

app = Flask(__name__)
 
 

app.secret_key = 'web'
 

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = 'Suba@10'

app.config['MYSQL_DB'] = 'webdb'
 

mysql = MySQL(app)

#load model 
app = Flask(__name__)
model = pickle.load(open('Phishing_website.pkl', 'rb'))

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')




@app.route('/flask/reg', methods =['GET', 'POST'])

def register():
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :

        name = request.form['name']

        email = request.form['email']

        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM signup WHERE email = % s', (email, ))

        account = cursor.fetchone()

        if account:

            msg = 'Account already exists !'

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):

            msg = 'Invalid email address !'

        elif not re.match(r'[A-Za-z0-9]+', name):

            msg = 'Username must contain only characters and numbers !'

        elif not name or not password or not email:

            msg = 'Please fill out the for !'

        else:

            cursor.execute('INSERT INTO signup VALUES ( % s, % s, % s)', (name, email, password, ))

            mysql.connection.commit()

            msg = 'You have successfully registered !'

            return redirect(url_for('predictform'), msg = msg)

    elif request.method =='POST':
        return redirect(url_for('predictform'))

    return render_template('reg.html', msg = msg)
    


        
    

@app.route('/flask/predictform', methods =['GET', 'POST'])
def predictform():
    return render_template('predictform.html')

@app.route('/flask/about', methods =['GET', 'POST'])
def about():
    return render_template('about.html')



#Redirects to the page to give the user iput URL.
@app.route('/flask/result')
def result(): 
    return render_template('result.html') 
ans=""
bns=""

#Fetches the URL given by the URL and passes to inputScript
@app.route('/y_predict', methods=['POST'])
def y_predict():

    '''
    For rendering results on HTML GUI
    '''

    url = request.form['url']
    checkprediction = inputScript.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction [0]
    if(output==1):
        pred="Your are safe!! This is a Legitimate Website."
        return render_template('result.html',ans=pred)

    else:
        pred="You are on the wrong site. Be cautious!"
        return render_template('result.html',bns=pred)
    
    

#Takes the input parameters fetched from the URL by inputScript and returns the predictions 
@app.route('/predict_api', methods=['POST'])
  
def predict_api():

    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict ( [np.array(list(data.values()))])

    output = prediction[0]
    return jsonify (output)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)


