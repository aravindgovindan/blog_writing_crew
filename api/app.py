from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BlogRequest(BaseModel):
    topic: str

@app.get("/")
def root():
    return {"message": "Welcome to the Blog Writing Crew API!"}

@app.post("/generate")
def generate_blog(request: BlogRequest):
    return {
        topic: request.topic,
        "message": f"Blog generation for topic '{request.topic}' has been initiated."
    }

