from flask import Flask, request
import EmotionDetection

app = Flask("emotionDetector")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector():
    text = request.args.get('text_to_analyze')
    response = EmotionDetection.emotion_detection.emotion_detector(text)
    if response['dominant_emotion'] is None:
        return {"message": "Invalid text! Please try again!."}, 400
    return response