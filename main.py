import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes import router

app = FastAPI()
templates = Jinja2Templates(directory='templates')

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)