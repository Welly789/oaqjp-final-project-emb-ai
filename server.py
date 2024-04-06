"""
Code to implement a flask server using IBM emotion 
detector to detect the emotion of a text input
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detect():
    """
    Function to call emotion detection method and send that to the /emotionDetector route
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is not None:
        output = f"For the given statement the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and \
        'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"
        return output
    return "Invalid text! Please try again!"

@app.route('/')
def index():
    """
    Function to render the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
