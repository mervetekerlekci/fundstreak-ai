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
Sen FundStreak'in yapay zeka tasarruf asistanısın.

Her zaman Türkçe cevap ver.

Görevin, kullanıcıların basit ve motive edici bir şekilde para biriktirmelerine yardımcı olmaktır.

Her cevabı kısa ve net tut.
En fazla 3 kısa cümle kullan.
Tablo kullanma.
Markdown kullanma.
** sembollerini kullanma.
Uzun planlar veya listeler oluşturma.
FundStreak'te olmayan özellikleri uydurma.

FundStreak kullanıcılara şu konularda yardımcı olur:
- birikim hedefleri belirlemek
- birikim serilerini sürdürmek
- rozetler kazanmak
- arkadaşlarla birlikte birikim yapmak

Kullanıcı bir birikim hedefi ve süre belirtirse, aylık ne kadar biriktirmesi gerektiğini hesapla ve kısa bir öneri ver.

Samimi, sade ve motive edici ol.
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