from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from textblob import TextBlob as tb
#import speech_recognition as sr


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict',methods=['POST'])

def predict():
    a= request.form.get('eng-input')
    blob=tb(a)
    rate= blob.translate(to='en')
    output=rate
    return render_template('app.html', prediction_text='TRANSLATED TEXT: {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    a= data.get('eng-input')
    blob=tb(a)
    rate= blob.translate(to='en')
    output=rate
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)