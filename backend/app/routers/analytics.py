from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.services import LLMService
from ..services.queue_service import RequestQueue

from ..database import get_db
from ..models import models, schemas
from ..services.auth_service import get_current_user
from ..services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    dependencies=[Depends(get_current_user)]
)
request_queue = RequestQueue(max_concurrent=5)

@router.post("/lessons/")
async def create_lesson(
    lesson_request: schemas.LessonRequest,
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    # Queue the request to manage load
    result = await request_queue.enqueue(
        LLMService.generate_lesson,
        lesson_request.topic,
        lesson_request.student_level,
        lesson_request.subject
    )
    # Process result and return
    return {"content": result}
@router.get("/performance", response_model=schemas.PerformanceSummary)
def get_performance_summary(
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    return AnalyticsService.get_performance_summary(db, current_user.id)

@router.get("/trends", response_model=schemas.LearningTrends)
def get_learning_trends(
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    return AnalyticsService.get_learning_trends(db, current_user.id)