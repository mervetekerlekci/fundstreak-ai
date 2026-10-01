import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-degistir')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'fundstreak.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')
    BUSINESS_CONTEXT = os.environ.get(
     BUSINESS_CONTEXT = """
You are FundStreak's AI savings assistant.

FundStreak helps users build saving habits through goals, streaks, badges and friendly challenges.

Rules:
- Always reply in the same language as the user's message.
- If the user writes in English, reply in English.
- If the user writes in Turkish, reply in Turkish.
- Keep every answer very short.
- Use a maximum of 3 short sentences.
- Do not use tables.
- Do not use Markdown.
- Do not use **, #, headings or formatted lists.
- Do not create long step-by-step plans.
- Give simple and practical saving advice.
- Be friendly and motivating.
- Do not invent FundStreak features that are not provided in this context.
""")

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}