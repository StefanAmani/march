from flask import Flask, render_template, request
import openai


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
# Set OpenAI API key
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/load", methods=['GET', 'POST'])
def load():
    if request.method != 'POST':
        return render_template("load.html")

    if request.method == 'POST':
    # Get user input from form
        user_input = request.form['user_input']
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
        # Extract response text from API response
        response_text = response.choices[0].text.strip()
        # Return response text to template
        return render_template("load.html", response_text=response_text)
   
if __name__ == "__main__":
    app.run(debug=True)