from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


pages_bp = Blueprint("pages", __name__)


api_bp = Blueprint("api", __name__)




@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json(silent=True) or {}

    mesaj = data.get("mesaj")
    gecmis = data.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alanı zorunludur."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine şu anda ulaşılamıyor."
        }), 503


@api_bp.route("/leads", methods=["POST"])
def lead_kaydet():
    data = request.get_json(silent=True) or {}

    isim = data.get("isim")
    telefon = data.get("telefon")
    mesaj = data.get("mesaj")

    # Zorunlu alan kontrolü
    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon alanları zorunludur."
        }), 400

    # Telefon numarası kontrolü
    if not telefon.isdigit() or len(telefon) != 11:
        return jsonify({
            "basari": False,
            "hata": "Telefon numarası 11 haneli ve yalnızca rakamlardan oluşmalıdır."
        }), 400

    try:
        lead_ekle(isim, telefon, mesaj)

        return jsonify({
            "basari": True,
            "mesaj": "Kayıt başarıyla oluşturuldu."
        }), 201

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayıt oluşturulurken bir hata oluştu."
        }), 500

@api_bp.route("/leads", methods=["GET"])
def leadleri_getir():
    try:
        leadler = tum_leadler()

        return jsonify({
            "basari": True,
            "leadler": leadler
        })

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayıtlar alınırken bir hata oluştu."
        }), 500