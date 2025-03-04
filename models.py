from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    sessions = relationship("Session", back_populates="student")

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    topic = Column(String)
    start_time = Column(DateTime, default=datetime.now(timezone.utc))
    end_time = Column(DateTime, nullable=True)
    
    student = relationship("Student", back_populates="sessions")
    progress = relationship("Progress", back_populates="session")
    messages = relationship("Message", back_populates="session")

class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    quiz_score = Column(Float, nullable=True)
    feedback = Column(Text, nullable=True)
    
    session = relationship("Session", back_populates="progress")

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    content = Column(Text)
    is_from_student = Column(Boolean, default=True)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    
    session = relationship("Session", back_populates="messages")