import joblib
import os
from sentence_transformers import SentenceTransformer

# 1. Path Safety: Use os.path.join for cross-platform compatibility
model_path = os.path.join("models", "trained_bert_model.joblib")

# 2. Loading with error handling
try:
    model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
    model_classification = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    model_classification = None

def classify_with_bert(log_message):
    # 3. Guard Clause: Check for empty input
    if not log_message or not isinstance(log_message, str) or len(log_message.strip()) == 0:
        return "Unclassified"
    
    if model_classification is None:
        return "Model not loaded"

    try:
        # Encode and Predict
        embeddings = model_embedding.encode([log_message])
        probabilities = model_classification.predict_proba(embeddings)[0]
        
        # Confidence threshold check
        if max(probabilities) < 0.5:
            return "Unclassified"
            
        predicted_label = model_classification.predict(embeddings)[0]
        return predicted_label
    except Exception as e:
        print(f"Classification error: {e}")
        return "Unclassified"

if __name__ == "__main__":
    # Test logs
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "System crashed due to drivers errors when restarting the server"
    ]
    for log in logs:
        print(f"{log} -> {classify_with_bert(log)}")