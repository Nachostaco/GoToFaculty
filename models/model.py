import joblib
from transformers import (AutoTokenizer, AutoModel)
import torch


class ModelApi:
    def __init__(self, model_path, tokenizer_path, embedding_path):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.embedding_path = embedding_path
        self.knn = self.load_model()
        self.tokenizer = self.load_tokenizer()
        self.embedding_model = self.load_embedding_model()

    def load_model(self):
        try:
            # Load and return the model from the model_path
            model = joblib.load(self.model_path)
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def load_tokenizer(self):
        try:
            # Load and return the tokenizer from the tokenizer_path
            tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path)
            return tokenizer
        except Exception as e:
            print(f"Error loading tokenizer: {e}")
            return None
        
    def load_embedding_model(self):
        try:
            # Load and return the embedding model
            embedding_model = AutoModel.from_pretrained('allegro/herbert-base-cased')
            return embedding_model
        except Exception as e:
            print(f"Error loading embedding model: {e}")
            return None
        
    def predict(self, input_data):
        try:
            # Tokenize the input data
            inputs = self.tokenizer(input_data, return_tensors="pt", padding=True, truncation=True)
            # Get embeddings
            with torch.no_grad():
                embeddings = self.embedding_model(**inputs).last_hidden_state.mean(dim=1).squeeze().numpy()
                # Use KNN for prediction
                outputs = self.knn.predict(embeddings.reshape(1,-1))
                # Process and return the outputs as needed
                return outputs
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None
