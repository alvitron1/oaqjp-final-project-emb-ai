import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, headers=Headers, json=json)
    
    data = response.json()['text']
    dominant_emotion = max(data, key=data.get)

    return_dict = {
        'anger': data['anger'],
        'disgust': data['disgust'],
        'fear': data['fear'],
        'joy': data['joy'],
        'sadness': data['sadness'],
        'dominant_emotion': dominant_emotion
    }

print(emotion_detector("I love this new technology."))
