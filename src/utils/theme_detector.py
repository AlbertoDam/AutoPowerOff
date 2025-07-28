import winreg

def is_light_mode():
    """Returns True if the system is in light mode, False if it is in dark mode."""
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    try:
        key = winreg.OpenKey(registry, key_path)
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 1
    except OSError:
        return True 
