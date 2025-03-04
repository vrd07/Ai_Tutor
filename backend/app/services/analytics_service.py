from sqlalchemy.orm import Session
from sqlalchemy import func
import pandas as pd
from typing import List, Dict, Any

from ..models import models

class AnalyticsService:
    @staticmethod
    def get_performance_summary(db: Session, student_id: int) -> Dict[str, Any]:
        # Get all completed sessions with quizzes
        quiz_results = (
            db.query(
                models.Session.topic,
                models.Progress.quiz_score
            )
            .join(models.Progress)
            .filter(
                models.Session.student_id == student_id,
                models.Progress.quiz_score.isnot(None)
            )
            .all()
        )
        
        if not quiz_results:
            return {
                "total_sessions": 0,
                "average_score": 0,
                "topics": []
            }
        
        # Convert to pandas for analysis
        df = pd.DataFrame(quiz_results, columns=["topic", "score"])
        
        # Get topic performance
        topic_performance = (
            df.groupby("topic")
            .agg(
                average_score=("score", "mean"),
                sessions=("score", "count")
            )
            .reset_index()
            .to_dict(orient="records")
        )
        
        return {
            "total_sessions": len(df),
            "average_score": df["score"].mean(),
            "topics": topic_performance
        }
    
    @staticmethod
    def get_learning_trends(db: Session, student_id: int) -> Dict[str, Any]:
        # Get sessions in chronological order with scores
        sessions = (
            db.query(
                models.Session.start_time,
                models.Progress.quiz_score
            )
            .join(models.Progress)
            .filter(
                models.Session.student_id == student_id,
                models.Progress.quiz_score.isnot(None)
            )
            .order_by(models.Session.start_time)
            .all()
        )
        
        if not sessions:
            return {
                "trend": "No data",
                "timeline": []
            }
            
        # Convert to pandas for analysis
        df = pd.DataFrame(sessions, columns=["date", "score"])
        df["date"] = pd.to_datetime(df["date"]).dt.date
        
        # Get trend line
        if len(df) >= 2:
            import numpy as np
            from scipy import stats
            
            x = np.arange(len(df))
            slope, intercept, r_value, p_value, std_err = stats.linregress(x, df["score"])
            
            trend = "improving" if slope > 0.01 else "stable" if abs(slope) <= 0.01 else "declining"
        else:
            trend = "insufficient data"
            
        # Format timeline data
        timeline = (
            df.groupby("date")
            .agg(average_score=("score", "mean"))
            .reset_index()
            .to_dict(orient="records")
        )
        
        return {
            "trend": trend,
            "timeline": timeline
        }