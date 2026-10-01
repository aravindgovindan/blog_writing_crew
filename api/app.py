from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from blog_writing_crew.main import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BlogRequest(BaseModel):
    topic: str

@app.get("/")
def root():
    return {"message": "Welcome to the Blog Writing Crew API!"}

@app.post("/generate")
def generate_blog(request: BlogRequest):
    topic = request.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")

    try:
        run(topic)
        output_file = Path("output/blog_post.md")
        if not output_file.exists():
            raise HTTPException(status_code=500, detail="Blog post generation failed.")

        markdown = output_file.read_text("utf-8")
        return {
            "topic": request.topic,
            "markdown": markdown
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

