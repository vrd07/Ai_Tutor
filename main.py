# backend/app/main.py (update)
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from .database import engine, Base
from .routers import students, sessions, lessons, quizzes, progress, analytics
from .middleware.rate_limiter import RateLimiter
from .services.error_handler import http_exception_handler, general_exception_handler

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Personal Tutor API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Streamlit frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
app.add_exception_handler(RequestValidationError, http_exception_handler)

# Setup rate limiter
rate_limiter = RateLimiter(requests_per_minute=30)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    await rate_limiter(request)
    response = await call_next(request)
    return response

# Include all routers
app.include_router(students.router)
app.include_router(sessions.router)
app.include_router(lessons.router)
app.include_router(quizzes.router)
app.include_router(progress.router)
app.include_router(analytics.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Personal Tutor API"}