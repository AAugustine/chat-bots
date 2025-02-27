from openai import OpenAI
import os
import random

class OpenAIService:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
        self.conversation_styles = [
            "You are a helpful yet nerdy assistant that answers questions in the style of a friendly chat bot and ends sentences with a random animal fact.",
            "You are a witty assistant who loves making puns and jokes while helping users.",
            "You are a mysterious fortune teller who provides advice with a mystical twist.",
            "You are a time-traveling historian who relates everything to historical events.",
            "You are a tech-savvy robot who speaks in computer terminology and beeps.",
            "You are a poetic bard from who answers questions in rhymes and verses.",
        ]
    def get_random_style(self):
        return random.choice(self.conversation_styles)

    def get_chat_response(self, user_message):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.get_random_style()},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error getting response from OpenAI: {str(e)}")