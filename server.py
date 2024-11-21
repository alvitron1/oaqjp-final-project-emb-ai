"""Server Pyton File"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Function to return string that describes dominant emotion"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!"
    return f"""For the given statement, the system response is 'anger': {response['anger']},
     'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy':{response['joy']} and
     'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    """Function to Render Main Page"""

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
