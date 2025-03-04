class SubjectTemplateService:
    templates = {
        "mathematics": {
            "lesson_structure": """
            1. Concept Introduction: Explain the mathematical concept clearly
            2. Definitions and Formulas: List any important definitions and formulas
            3. Step-by-Step Examples: Show worked examples with detailed steps
            4. Common Mistakes: Point out typical errors students make
            5. Practice Problems: Provide progressively challenging problems
            """,
            "quiz_format": "Include numerical problems requiring calculation, as well as conceptual questions."
        },
        "science": {
            "lesson_structure": """
            1. Scientific Background: Explain the scientific principles
            2. Key Terminology: Define important scientific terms
            3. Experimental Evidence: Discuss relevant experiments or studies
            4. Real-World Applications: Connect to everyday phenomena
            5. Current Research: Mention recent developments if appropriate
            """,
            "quiz_format": "Include both factual recall questions and application scenarios."
        },
        "language": {
            "lesson_structure": """
            1. Language Rules: Explain the grammar or vocabulary rules
            2. Usage Examples: Show how the language is used in context
            3. Practice Dialogs or Texts: Provide authentic language samples
            4. Cultural Notes: Include relevant cultural information
            5. Common Errors: Highlight typical mistakes to avoid
            """,
            "quiz_format": "Include translation, fill-in-the-blank, and contextual usage questions."
        },
        "history": {
            "lesson_structure": """
            1. Historical Context: Set the time period and background
            2. Key Events: Outline major events in chronological order
            3. Important Figures: Discuss significant historical figures
            4. Analysis: Examine causes and effects
            5. Legacy: Explain the historical significance and modern relevance
            """,
            "quiz_format": "Include factual questions about events and dates, as well as analytical questions about causes and effects."
        },
        "programming": {
            "lesson_structure": """
            1. Concept Explanation: Explain the programming concept
            2. Syntax Guide: Show the correct syntax with examples
            3. Code Examples: Provide working code samples
            4. Common Bugs: Highlight typical errors and debugging tips
            5. Practice Exercises: Suggest coding challenges to try
            """,
            "quiz_format": "Include code snippets with questions about output, error identification, and concept application."
        }
    }
    
    @classmethod
    def get_template(cls, subject):
        # Default to general template if subject not found
        return cls.templates.get(subject.lower(), {
            "lesson_structure": """
            1. Introduction: Engage the student and set context
            2. Key Concepts: Explain the main ideas
            3. Examples: Provide illustrative examples
            4. Practice: Include opportunities for application
            5. Summary: Recap important points
            """,
            "quiz_format": "Include a mix of recall, understanding, and application questions."
        })
    
    @classmethod
    def apply_template(cls, prompt, subject):
        template = cls.get_template(subject)
        return f"{prompt}\n\nFollowing this structure:\n{template['lesson_structure']}\n\nFor the quiz: {template['quiz_format']}"