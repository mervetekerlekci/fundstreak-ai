import requests
from config import Config


class AIServiceError(Exception):
    pass


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.business_context = Config.BUSINESS_CONTEXT
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "openai/gpt-oss-20b"

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return "Demo modu: Groq API anahtarı tanımlı değil, bu yüzden gerçek bir yanıt üretemiyorum."

        messages = [{"role": "system", "content": self.business_context}]

        if gecmis:
            messages.extend(gecmis)

        messages.append({"role": "user", "content": mesaj})

        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": messages,
                },
                timeout=15,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            raise AIServiceError(f"Yapay zeka servisine ulaşılamadı: {e}")
        except (KeyError, IndexError) as e:
            raise AIServiceError(f"Yapay zeka yanıtı beklenmeyen formatta: {e}")


ai_service = AIService()