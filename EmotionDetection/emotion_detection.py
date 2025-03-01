import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    jsonObj = requests.post(url, headers = headers, json = body).json()
    emotionObj = jsonObj['emotionPredictions'][0]['emotion']
    emotionObj['dominant_emotion'] = max(emotionObj, key=emotionObj.get)
    return emotionObj
