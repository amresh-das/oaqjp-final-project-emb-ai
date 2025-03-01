import unittest
import EmotionDetection

class TestEmotionDetection(unittest.TestCase):

    def run_analysis_and_get_dominant_emotion(self, text_to_analyze):
        return EmotionDetection.emotion_detection.emotion_detector(text_to_analyze)['dominant_emotion']
    
    def test_joy(self):
        self.assertEqual('joy', self.run_analysis_and_get_dominant_emotion("I am glad this happened"))
    
    def test_anger(self):
        self.assertEqual('anger', self.run_analysis_and_get_dominant_emotion("I am really mad about this"))
    
    def test_disgust(self):
        self.assertEqual('disgust', self.run_analysis_and_get_dominant_emotion("I feel disgusted just hearing about this"))
    
    def test_sadness(self):
        self.assertEqual('sadness', self.run_analysis_and_get_dominant_emotion("I am so sad about this"))
    
    def test_fear(self):
        self.assertEqual('fear', self.run_analysis_and_get_dominant_emotion("I am really afraid that this will happen"))
