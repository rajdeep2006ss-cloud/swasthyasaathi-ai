from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from assistant import (
    search_knowledge_base,
    generate_doctor_checklist,
    sanitize_user_input,
)

app = FastAPI(
    title="SwasthyaSaathi AI API",
    description="Healthcare education API for the SwasthyaSaathi frontend",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class HealthQuery(BaseModel):
    query: str = Field(min_length=1, max_length=1000)
    language: str = Field(default="en", pattern="^(en|hi|kn)$")
    reading_level: str = Field(default="simple", pattern="^(simple|standard)$")


class DoctorPrepRequest(BaseModel):
    topic: str = Field(default="", max_length=300)
    symptoms: str = Field(default="", max_length=1000)
    duration: str = Field(default="", max_length=200)
    language: str = Field(default="en", pattern="^(en|hi|kn)$")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "SwasthyaSaathi AI API"}


@app.post("/api/health/search")
def search_health(request: HealthQuery):
    clean_query = sanitize_user_input(request.query)
    return search_knowledge_base(
        clean_query,
        reading_level=request.reading_level,
        language=request.language,
    )


@app.post("/api/doctor-prep")
def doctor_prep(request: DoctorPrepRequest):
    return generate_doctor_checklist(
        topic=sanitize_user_input(request.topic),
        symptoms=sanitize_user_input(request.symptoms),
        duration=sanitize_user_input(request.duration),
        language=request.language,
    )
