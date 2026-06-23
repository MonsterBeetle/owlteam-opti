import secrets
import string
from datetime import datetime

class KeyGenerator:
    def __init__(self):
        self.prefix = "OWL"
    
    def generate_key(self, length=20):
        """Generate random license key"""
        characters = string.ascii_uppercase + string.digits
        key_part = ''.join(secrets.choice(characters) for _ in range(length))
        full_key = f"{self.prefix}-{key_part[:5]}-{key_part[5:10]}-{key_part[10:15]}-{key_part[15:]}"
        return full_key
    
    def generate_batch(self, count=10, duration="30_days"):
        """Generate batch of license keys"""
        keys = []
        for _ in range(count):
            key = self.generate_key()
            keys.append({
                "key": key,
                "duration": duration,
                "created_at": datetime.now().isoformat()
            })
        return keys
    
    def validate_key_format(self, key):
        """Validate if key has correct format"""
        parts = key.split('-')
        if len(parts) != 5:
            return False
        if parts[0] != self.prefix:
            return False
        return True
