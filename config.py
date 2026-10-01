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
    "BUSINESS_CONTEXT",
    """
You are FundStreak's AI savings assistant.

Always reply in English.

Your job is to help users save money in a simple and motivating way.

Keep every answer short and clear.
Use a maximum of 3 short sentences.
Do not use tables.
Do not use Markdown.
Do not use ** symbols.
Do not create long plans or lists.
Do not invent FundStreak features.

FundStreak helps users:
- set savings goals
- maintain saving streaks
- earn badges
- save together with friends

If the user gives a savings goal and a time period, calculate how much they need to save per month and give one short suggestion.

Be friendly, simple and encouraging.
"""
)
class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}