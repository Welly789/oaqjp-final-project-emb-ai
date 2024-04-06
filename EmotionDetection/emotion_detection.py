import json
import requests

def emotion_detector(text_to_analyze):
    # get response from emotion prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=header)

    # format response into a dictionary
    formatted_response = json.loads(response.text)

    # incorporate error handling
    if response.status_code == 200:
        # extract just the emotions from the dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # find the emotion with the maximum value in the dictionary
        dominant_emotion = max(emotions, key=emotions.get)
        # add a key/value pair to the emotions dictionary to show the dominant emotion
        emotions['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotions = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
    # return the emotions dictionary in the requested format
    return emotions 
