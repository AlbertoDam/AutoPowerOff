from utils.theme_detector import is_light_mode

def get_theme_colors():
    """Devuelve colores según modo del sistema"""
    if not is_light_mode():
        return {
            "bg": "#FFFFFF",
            "text": "#1C1C1C",
            "shutdown_btn_bg": "#E53935",
            "shutdown_btn_text": "#FFFFFF",
            "time_elements": "#1976D2",
            "entry_bg": "#FFFFFF",
            "entry_border": "#1C1C1C"
        }
    else:
        return {
            "bg": "#121212",
            "text": "#E0E0E0",
            "shutdown_btn_bg": "#E53935",
            "shutdown_btn_text": "#FFFFFF",
            "time_elements": "#64B5F6",
            "entry_bg": "#1E1E1E",
            "entry_border": "#E0E0E0"
        }
