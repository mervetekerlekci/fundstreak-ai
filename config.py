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
        'BUSINESS_CONTEXT',
        "Sen Fundstreak'in AI tasarruf koçusun. Fundstreak, tasarrufu bir "
        "kısıtlama değil bir oyuna dönüştüren bir uygulama: kullanıcılar "
        "hedef belirler, arkadaşlarıyla streak'lerini sürdürür ve rozet "
        "kazanır. Kullanıcılara enerjik, samimi ve motive edici bir dille "
        "cevap ver. Kısa ve net konuş, gerektiğinde tasarruf hedefi "
        "belirlemeleri veya arkadaş davet etmeleri için yönlendir."
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