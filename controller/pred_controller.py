from fastapi import HTTPException, status
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str

class PredictionResponse(BaseModel):
    prediction: int
    faculty: str
    color: str

    
class PredictionController:
    def __init__(self, model_api) -> None:
        self.model_api = model_api
        pass


    def concatenate_questions(self, request: PredictionRequest) -> str:
        text = f"{request.question1} {request.question2} {request.question3} {request.question4} {request.question5}"
        return text.strip()

    async def get_prediction(self, request: PredictionRequest) -> PredictionResponse:
        print(f"{request} controller1")
        try:
            if not all([request.question1, request.question2, request.question3, request.question4, request.question5]):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="All questions must be provided")
            input = self.concatenate_questions(request)
            print(f"{input} controller2")
            prediction = self.model_api.predict(input)
            print(f"{prediction} controller3")
            if prediction is None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed")
            mapping = {}
            with open('data/mapping.json', 'r', encoding='utf-8') as f:
                import json
                mapping = json.load(f)
            colors = {
                "0": "#eb4034",  # Example color for faculty 0
                "1": "#1ba118",  # Example color for faculty 1
                "2": "#dade10",  # Example color for faculty 2
                "3": "#182af0",  # Example color for faculty 3
                "4": "#af18f0",  # Example color for faculty 4
                "5": "#F28C28"   # Example color for faculty 5
            }
            color = colors.get(str(prediction[0]), "#ffffff")
            return PredictionResponse(prediction=int(prediction[0]), faculty=mapping.get(str(prediction[0]), "Unknown"), color=color)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    async def health_check(self):
        return {"status": "ok"}
