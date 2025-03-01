from flask import Flask, request
import EmotionDetection

app = Flask("emotionDetector")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector():
    text = request.args.get('text_to_analyze')
    return EmotionDetection.emotion_detection.emotion_detector(text)
