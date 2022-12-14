import pickle

#importing the inputScript file used to analyze the URL import inputScript
import inputScript
import numpy as np
import sklearn

from flask import Flask, jsonify, render_template, request

#load model 
app = Flask(__name__) 
model = pickle.load(open('Phishing_website.pkl', 'rb'))


#Redirects to the page to give the user iput URL.
@app.route('/')
def predict(): 
    return render_template('prediction.html') 
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
        return render_template('prediction.html',ans=pred)

    else:
        pred="You are on the wrong site. Be cautious!"
        return render_template('prediction.html',bns=pred)
    
    

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


