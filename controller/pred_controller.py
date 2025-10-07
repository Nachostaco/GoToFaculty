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
    
class PredictionController:
    def __init__(self, model_api) -> None:
        self.model_api = model_api
        pass

    def concatenate_questions(self, request: PredictionRequest) -> str:
        text = f"{request.question1} {request.question2} {request.question3} {request.question4} {request.question5}"
        return text.strip()

    async def get_prediction(self, request: PredictionRequest) -> PredictionResponse:
        try:
            if not all([request.question1, request.question2, request.question3, request.question4, request.question5]):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="All questions must be provided")
            input = self.concatenate_questions(request)
            prediction = self.model_api.predict(input)
            if prediction is None:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed")
            return PredictionResponse(prediction=int(prediction[0]))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    async def health_check(self):
        return {"status": "ok"}
