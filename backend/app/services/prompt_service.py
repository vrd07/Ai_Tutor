class PromptService:
    @staticmethod
    def create_lesson_prompt(topic, student_level):
        return f"""
        You are an expert tutor creating a lesson on {topic} for a {student_level}-level student.
        
        Structure your response as follows:
        1. Introduction: Briefly explain what {topic} is and why it's important.
        2. Main Content: Explain 3-5 key concepts about {topic}, with examples.
        3. Summary: Recap the main points of the lesson.
        
        Use language appropriate for a {student_level} student. Keep explanations clear and concise.
        """
    
    @staticmethod
    def create_quiz_prompt(lesson_content):
        return f"""
        Based on the following lesson content, create 5 multiple-choice questions:
        
        {lesson_content}
        
        Format each question as follows:
        Q1: [Question text]
        A) [Option A]
        B) [Option B]
        C) [Option C]
        D) [Option D]
        Correct Answer: [Letter of correct option]
        
        Ensure questions cover key concepts from the lesson and vary in difficulty.
        """
    
    @staticmethod
    def create_feedback_prompt(lesson_content, student_answers, correct_answers):
        return f"""
        Lesson content: {lesson_content}
        
        Student's answers: {student_answers}
        
        Correct answers: {correct_answers}
        
        As a supportive tutor, provide personalized feedback to the student:
        1. Start with positive reinforcement on what they did well.
        2. Identify misconceptions or errors gently, explaining why they might have occurred.
        3. Provide targeted explanations for concepts they seem to struggle with.
        4. Suggest specific strategies to improve understanding.
        5. End with encouragement.
        
        Keep your tone supportive and encouraging throughout.
        """