from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from routes.event import event_router 
from routes.registration import registration_router 
from routes.speaker import speaker_router
from routes.user import user_router 
from schemas.speaker import Speaker, speakers 

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not speakers:
        speakers.extend([
            Speaker(id=1, name="Marketing Guru", topic="Marketing in the modern age"),
            Speaker(id=2, name="Elon Musk", topic="Space Exploration"),
            Speaker(id=3, name="Prof. Ben Codes", topic="The Future of Programming")
        ])
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(event_router, tags=["Events"], prefix="/events")
app.include_router(registration_router, tags=["Registrations"], prefix="/registrations")
app.include_router(speaker_router, tags=["Speakers"], prefix="/speakers")


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello from the Event Management API"}