import os
import requests

NOTIFICATION_URL = os.environ.get("NOTIFICATION_URL", "https://api.notificaciones-legacy.com/send")
API_KEY = os.environ.get("NOTIFICATION_API_KEY", "REDACTED")

def enviar_confirmacion(usuario_id, total):
    payload = {
        "to": usuario_id,
        "message": f"Tu pedido por ${total} fue confirmado",
        "api_key": API_KEY
    }
    try:
        requests.post(NOTIFICATION_URL, json=payload, timeout=2)
    except Exception:
        pass
