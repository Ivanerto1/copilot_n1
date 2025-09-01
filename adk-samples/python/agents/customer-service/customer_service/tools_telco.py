from typing import Dict, Any

def get_site_kpis(site_id: str, last_hours: int = 3) -> Dict[str, Any]:
    """
    Devuelve KPIs RAN/Core (PRB, CQI, delay RLC, etc.) para un sitio en una ventana.
    Sustituye el cuerpo por llamadas reales a tu DWH/OSS (BigQuery/APIs internas).
    """
    # TODO: integrar con tus fuentes reales
    return {
        "status": "success",
        "site_id": site_id,
        "window_h": last_hours,
        "kpis": {
            "PRB_DL_pct": 54,
            "CQI_avg": 10,
            "RLC_delay_ms": 45,
            "N_ThpVol_DL_LastSlot": 1234
        }
    }

def check_alarmas(site_id: str) -> Dict[str, Any]:
    """
    Consulta alarmas activas en OSS/EMS para el sitio.
    """
    # TODO: integrar con tu gestor de alarmas
    return {
        "status": "success",
        "site_id": site_id,
        "alarmas": [
            {"id": "A123", "sev": "major", "ts": "2025-08-29T12:00:00Z",
             "text": "Backhaul con BER intermitente"}
        ]
    }

def trace_msisdn(msisdn: str) -> Dict[str, Any]:
    """
    Traza básico de conectividad para un MSISDN/IMSI.
    """
    # TODO: integrar con sonda/servicio E2E
    return {
        "status": "success",
        "msisdn": msisdn,
        "trace": {"rtt_ms": 82, "packet_loss_pct": 0.0, "apn": "internet"}
    }
