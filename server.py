from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detect(text_to_analyse):
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    return "For the given statement the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}".format(
        response['anger'],
        response['disgust'],
        response['fear'],
        response['joy'],
        response['sadness'],
        response['dominant_emotion']
    )
