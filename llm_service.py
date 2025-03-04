from fastapi import Depends
import httpx
from .template_service import SubjectTemplateService
from .cache_service import CacheService

class LLMService:
    def __init__(self, base_url="http://localhost:11434/api"):
        self.base_url = base_url
        self.cache = CacheService()
        
    async def generate(self, prompt, model="mixtral"):
        # Check cache first
        cached_response = await self.cache.get_cached_response(f"llm:{model}", prompt)
        if cached_response:
            return cached_response
        
        # If not in cache, generate response
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            result = response.json()["response"]
            
            # Cache the result
            await self.cache.cache_response(f"llm:{model}", prompt, result)
            
            return result
       
    async def generate_lesson(self, topic, student_level, subject="general"):
    # Base prompt
        prompt = f"""Create an educational lesson about {topic} for a student at {student_level} level.
                    Include an introduction, main content with key concepts, and a summary."""
                
    # Apply subject-specific template
        prompt = SubjectTemplateService.apply_template(prompt, subject)
    
        return await self.generate(prompt)
        
    async def generate_quiz(self, lesson_content):
        prompt = f"""Based on this lesson: {lesson_content}
                    Generate 5 multiple-choice questions with 4 options each.
                    For each question, indicate the correct answer."""
        return await self.generate(prompt)
        
    async def provide_feedback(self, lesson, student_answers, correct_answers):
        prompt = f"""Lesson: {lesson}
                    Student answers: {student_answers}
                    Correct answers: {correct_answers}
                    Provide personalized feedback on the student's performance."""
        return await self.generate(prompt)