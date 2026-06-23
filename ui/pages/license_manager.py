from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from core.advanced_key_system import SecureLicenseManager
from core.optimizer import HWIDManager
from config.constants import ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR, ERROR_COLOR

class LicenseManagerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.license_manager = SecureLicenseManager()
        self.hwid_manager = HWIDManager()
        self.current_hwid = None
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("🔐 License Manager")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Get HWID
        self.current_hwid = self.hwid_manager.get_hwid()
        hwid_label = QLabel(f"Your HWID: {self.current_hwid}")
        hwid_label.setStyleSheet("color: #666666; font-size: 11px; word-wrap: true; background-color: #f5f5f5; padding: 10px; border-radius: 5px;")
        layout.addWidget(hwid_label)
        
        # Key input section
        key_label = QLabel("Enter License Key:")
        key_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        layout.addWidget(key_label)
        
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("OWL-XXXXXXXXXX-XXXXXXXX-XXXXXX")
        self.key_input.setMinimumHeight(40)
        layout.addWidget(self.key_input)
        
        # Activate button
        activate_btn = QPushButton("🔓 Activate License")
        activate_btn.setMinimumHeight(45)
        activate_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        activate_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: white;
                border: none;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #1E5A1F;
            }}
        """)
        activate_btn.clicked.connect(self.activate_license)
        layout.addWidget(activate_btn)
        
        # Status
        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600;")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        
        # Info section
        info_frame = QFrame()
        info_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 15px;")
        info_layout = QVBoxLayout()
        
        info_title = QLabel("📍 License Information")
        info_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        info_layout.addWidget(info_title)
        
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        self.info_text.setMaximumHeight(200)
        self.info_text.setText(
            """🔐 OwlTeam Opti Advanced License System

✓ Secure key validation with HWID binding
✓ All data embedded in the key
✓ Automatic expiration
✓ Tampering detection
✓ Works completely offline

📋 How to get a license:
1. Contact the developer
2. Receive a license key
3. Paste it above and click Activate
4. Your PC is automatically bound to this license
5. Enjoy premium features!

⏰ Key expires based on purchase duration
🔒 Each key is locked to your PC (HWID)""")
        info_layout.addWidget(self.info_text)
        
        info_frame.setLayout(info_layout)
        layout.addWidget(info_frame)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def activate_license(self):
        """Activate license key"""
        key = self.key_input.text().strip().upper()
        
        if not key:
            self.show_error("Please enter a license key")
            return
        
        # Try to activate
        result = self.license_manager.activate_key(key, self.current_hwid)
        
        if result["success"]:
            self.show_success(result["message"])
            self.key_input.clear()
            # Show license info
            info = self.license_manager.get_key_info(key)
            if info["exists"]:
                self.info_text.setText(
                    f"""✅ License Activated!

📌 License Details:
   Key: {key[:15]}...
   Activated: {info['activated']}
   Expires: {info['expires']}
   Duration: {info['duration_days']} days
   Status: Active
   HWID: {self.current_hwid}

✓ Your license is now active!
✓ Enjoy premium features!
✓ Your PC is bound to this license (cannot be shared)"""
                )
        else:
            self.show_error(result["message"])
    
    def show_success(self, message):
        """Show success message"""
        self.status_label.setText(f"✅ {message}")
        self.status_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600;")
    
    def show_error(self, message):
        """Show error message"""
        self.status_label.setText(f"❌ {message}")
        self.status_label.setStyleSheet(f"color: {ERROR_COLOR}; font-weight: 600;")
