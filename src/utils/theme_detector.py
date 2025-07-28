import winreg

def is_light_mode():
    """Devuelve True si el sistema está en modo claro, False si está en modo oscuro."""
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    try:
        key = winreg.OpenKey(registry, key_path)
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 1
    except FileNotFoundError:
        return True 
