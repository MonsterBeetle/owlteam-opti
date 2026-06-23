import sqlite3
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

class LicenseManager:
    def __init__(self):
        self.db_path = Path.home() / ".owlteam_opti" / "licenses.db"
        self.db_path.parent.mkdir(exist_ok=True)
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS licenses (
                id INTEGER PRIMARY KEY,
                key TEXT UNIQUE,
                hwid TEXT,
                activation_date TIMESTAMP,
                expiration_date TIMESTAMP,
                status TEXT,
                created_at TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def add_license(self, key, hwid, duration_days):
        """Add new license to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        now = datetime.now()
        expiration = now + timedelta(days=duration_days)
        
        try:
            cursor.execute('''
                INSERT INTO licenses (key, hwid, activation_date, expiration_date, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (key, hwid, now, expiration, 'active', now))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
    
    def validate_license(self, key, current_hwid):
        """Validate if license key is valid"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT hwid, expiration_date, status FROM licenses WHERE key = ?',
            (key,)
        )
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            return False, "License not found"
        
        hwid, expiration, status = result
        
        if hwid != current_hwid:
            return False, "HWID mismatch - License bound to different PC"
        
        if status != 'active':
            return False, f"License is {status}"
        
        expiration_dt = datetime.fromisoformat(expiration)
        if expiration_dt < datetime.now():
            self.revoke_license(key)
            return False, "License expired"
        
        return True, "License valid"
    
    def revoke_license(self, key):
        """Revoke a license"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE licenses SET status = ? WHERE key = ?',
            ('revoked', key)
        )
        conn.commit()
        conn.close()
    
    def get_license_info(self, key):
        """Get license information"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM licenses WHERE key = ?', (key,))
        result = cursor.fetchone()
        conn.close()
        return result
