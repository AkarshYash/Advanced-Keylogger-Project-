from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pickle
import os

class BehaviorAnalyzer:
    def __init__(self, model_path="models/behavior_model.pkl"):
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')
        self.model = KMeans(n_clusters=5)
        self.model_path = model_path
        self.load_model()
        
    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                data = pickle.load(f)
                self.vectorizer = data['vectorizer']
                self.model = data['model']
                
    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump({
                'vectorizer': self.vectorizer,
                'model': self.model
            }, f)
            
    def analyze_text(self, text):
        try:
            vec = self.vectorizer.transform([text])
            cluster = self.model.predict(vec)[0]
            return f"Behavior pattern {cluster}"
        except Exception as e:
            print(f"[ANALYSIS ERROR] {str(e)}")
            return None
