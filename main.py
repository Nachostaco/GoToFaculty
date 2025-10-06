from models import ModelApi

def main():
    print("Hello from gotofaculty!")
    model_api = ModelApi("models\\model.joblib", "models\\tokenizer", "models\\model")
    sample_input = "Debil oraz automatyk"
    prediction = model_api.predict(sample_input)
    print("Prediction:", prediction)

if __name__ == "__main__":
    main()
