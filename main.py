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
    try:
        if request.method == 'POST':
            # Get user input from form
            user_input = request.form['user_input']
            logging.debug("User input line 21")
            # Call OpenAI API to generate response
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                temperature=0.5,
                max_tokens=4000,
                n=1,
                stop=None,
                timeout=10,
            )
            logging.debug("Response line 32")
            # Extract response text from API response
            response_text = response.choices[0].text.strip()
            logging.debug("response text line 35")
            # Return response text to template
            return render_template('home.html', response_text=response_text)
        else:
            logging.debug("User input line 39")
            return render_template('home.html')
            
    except: 
            logging.error("Failed to Run")
        

#if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 80))
    #app.run(debug=True, port=port)

