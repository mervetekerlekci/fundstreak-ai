# Fundstreak AI

**SmartLead AI** proje yönergesine göre geliştirilen, ziyaretçilerle yapay
zekâ üzerinden sohbet eden ve iletişim bilgilerini (lead) toplayan bir
sistem. Bu proje, **Fundstreak** markası için özelleştirilmiştir —
kullanıcılara tasarruf ve bütçe yönetimi konusunda destek olan,
oyunlaştırılmış bir AI asistanı sunar.

## Proje Hakkında

Fundstreak, tasarrufu bir zorunluluk değil bir başarı/oyun deneyimine
dönüştüren bir fintech markasıdır. Sistem iki arayüzden oluşur:

- **Karşılama Sayfası (B2C):** Ziyaretçilerin yapay zekâ ile sohbet edip
  iletişim bilgisi bıraktığı sayfa.
- **Yönetim Paneli (B2B):** İşletme sahibinin toplanan lead kayıtlarını
  görüntülediği panel.

## Mimari

Proje, **Separation of Concerns** ilkesine göre
tasarlanmıştır — her dosyanın tek bir görevi vardır:
fundstreak_ai/
├── run.py # Sunucuyu başlatan giriş noktası
├── config.py # Ayarlar ve .env okuma
├── requirements.txt # Bağımlılık listesi
├── .env # Gizli anahtarlar (Git'e eklenmez)
├── .gitignore
└── app/
├── init.py # Uygulama fabrikası (create_app)
├── database.py # Veritabanı işlemleri (SADECE burada)
├── routes.py # HTTP rotaları (sadece yönlendirme)
├── templates/
│ ├── index.html # Karşılama sayfası
│ └── dashboard.html # Yönetim paneli
└── services/
└── ai_service.py

## Teknoloji Yığını

- **Backend:** Python, Flask
- **Veritabanı:** SQLite
- **Yapay Zekâ:** Groq API (llama-3.1-8b-instant)
- **Frontend:** Wix Velo
- **Yayınlama:** Render

## Kurulum

```bash
# Sanal ortamı oluştur ve aktive et
python -m venv venv
source venv/bin/activate

# Bağımlılıkları kur
pip install -r requirements.txt

# .env dosyasını oluştur ve GROQ_API_KEY'i ekle
```

## Durum
 **Geliştirme aşamasında** — Environment kurulumu  tamamlandı.
