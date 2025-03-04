from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import models, schemas
from ..services.auth_service import get_current_user

router = APIRouter(
    prefix="/progress",
    tags=["progress"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=schemas.Progress)
def create_progress(
    progress: schemas.ProgressCreate,
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    # Verify session belongs to current user
    session = db.query(models.Session).filter(models.Session.id == progress.session_id).first()
    if not session or session.student_id != current_user.id:
        raise HTTPException(status_code=404, detail="Session not found")
    
    db_progress = models.Progress(**progress.dict())
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress

@router.get("/session/{session_id}", response_model=schemas.Progress)
def read_progress_by_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    # Verify session belongs to current user
    session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if not session or session.student_id != current_user.id:
        raise HTTPException(status_code=404, detail="Session not found")
    
    progress = db.query(models.Progress).filter(models.Progress.session_id == session_id).first()
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress

@router.get("/", response_model=List[schemas.ProgressWithSession])
def read_all_progress(
    db: Session = Depends(get_db),
    current_user: models.Student = Depends(get_current_user)
):
    # Get all sessions for the user
    sessions = db.query(models.Session).filter(models.Session.student_id == current_user.id).all()
    session_ids = [session.id for session in sessions]
    
    # Get progress for those sessions
    progress = db.query(models.Progress).filter(models.Progress.session_id.in_(session_ids)).all()
    return progress