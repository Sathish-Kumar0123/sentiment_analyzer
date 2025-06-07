from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        confidence = round(abs(polarity) * 100, 2)
        return render_template('index.html', text=text, sentiment=sentiment, confidence=confidence)
    
    # On GET request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
