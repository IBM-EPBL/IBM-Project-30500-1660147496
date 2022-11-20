import pickle

#importing the inputScript file used to analyze the URL import inputScript
import inputScript
import numpy as np
import sklearn

from flask import Flask, jsonify, render_template, request

#load model 
app = Flask(__name__) 
model = pickle.load(open('Phishing_website.pkl', 'rb'))

@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/flask/register', methods =['GET', 'POST'])
def register():
    
    return render_template('register.html')

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


