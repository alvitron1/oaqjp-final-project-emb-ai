import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, headers=Headers, json=body)
    status_code = response.status_code

    if status_code == 400:
        return {
            "anger": 'None', 
            "disgust": 'None',
            "fear": 'None', 
            "joy": 'None', 
            "sadness": 'None',
            "dominant_emotion": 'None'
        }
    else:
        data = response.json()['emotionPredictions'][0]['emotion']
        data['dominant_emotion'] = max(data, key=data.get)

        return data
