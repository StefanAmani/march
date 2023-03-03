import openai
import os
from flask import Flask, render_template, request
import logging

DEBUG=True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Set OpenAI API key
openai.api_key = "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"

# Define home route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
            
  
        


