import json
import os
from pathlib import Path

class Settings:
    def __init__(self):
        self.config_dir = Path.home() / ".owlteam_opti"
        self.config_dir.mkdir(exist_ok=True)
        self.settings_file = self.config_dir / "settings.json"
        self.load_settings()
    
    def load_settings(self):
        if self.settings_file.exists():
            with open(self.settings_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = self.get_default_settings()
            self.save_settings()
    
    def get_default_settings(self):
        return {
            "theme": "light",
            "auto_cleanup": False,
            "notification_enabled": True,
            "startup": False,
            "language": "en",
            "current_mode": "Balanced"
        }
    
    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get(self, key, default=None):
        return self.data.get(key, default)
    
    def set(self, key, value):
        self.data[key] = value
        self.save_settings()
