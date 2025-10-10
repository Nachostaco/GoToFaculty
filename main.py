from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

model_api = None
controller = None

async def startup_event():
    global model_api, controller
    from models import ModelApi
    from controller import PredictionController

    model_api = ModelApi('models\\model.joblib', 'models\\tokenizer')
    controller = PredictionController(model_api)
    print("Application startup complete.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_event()
    yield

app = FastAPI(title='GoToFacultyApi', lifespan=lifespan)

app.mount('/static', StaticFiles(directory='view/static'), name='static')
templates = Jinja2Templates(directory='view/templates')

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/result')
async def result_page(request: Request):
    return templates.TemplateResponse('result.html', {'request': request})

@app.post('/api/predict')
async def predict_endpoint(request: Request):
    from controller.pred_controller import PredictionRequest
    data = await request.json()
    request_data = PredictionRequest(**data)
    print(f"{request_data} main")
    result = await controller.get_prediction(request_data)
    return result

@app.get('/api/health')
async def health_endpoint():
    return await controller.health_check()


