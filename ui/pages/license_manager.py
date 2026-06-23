from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from core.license_manager import LicenseManager
from core.hwid_manager import HWIDManager
from tools.key_generator import KeyGenerator
from config.constants import ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR, ERROR_COLOR, LICENSE_DURATION_DAYS

class LicenseManagerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.license_manager = LicenseManager()
        self.hwid_manager = HWIDManager()
        self.key_generator = KeyGenerator()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("License Manager")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Tabs
        tab_layout = QHBoxLayout()
        
        generate_btn = QPushButton("Generate Keys")
        validate_btn = QPushButton("Validate License")
        
        for btn in [generate_btn, validate_btn]:
            btn.setMinimumHeight(40)
            btn.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border: 1px solid #E0E0E0; border-radius: 5px;")
            tab_layout.addWidget(btn)
        
        layout.addLayout(tab_layout)
        
        # Content area
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        self.content_layout = QVBoxLayout()
        self.content_frame.setLayout(self.content_layout)
        
        layout.addWidget(self.content_frame)
        
        # Show generate by default
        self.show_generate()
        
        generate_btn.clicked.connect(self.show_generate)
        validate_btn.clicked.connect(self.show_validate)
        
        self.setLayout(layout)
    
    def clear_content(self):
        while self.content_layout.count():
            self.content_layout.takeAt(0).widget().deleteLater()
    
    def show_generate(self):
        self.clear_content()
        
        label = QLabel("Generate License Keys")
        label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.content_layout.addWidget(label)
        
        # Count input
        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("Number of keys:"))
        count_input = QLineEdit()
        count_input.setText("1")
        count_input.setMaximumWidth(100)
        count_layout.addWidget(count_input)
        count_layout.addStretch()
        self.content_layout.addLayout(count_layout)
        
        # Duration dropdown
        duration_layout = QHBoxLayout()
        duration_layout.addWidget(QLabel("Duration:"))
        duration_combo = QComboBox()
        for duration in LICENSE_DURATION_DAYS.keys():
            duration_combo.addItem(duration)
        duration_layout.addWidget(duration_combo)
        duration_layout.addStretch()
        self.content_layout.addLayout(duration_layout)
        
        # Generate button
        gen_btn = QPushButton("Generate")
        gen_btn.setMinimumHeight(40)
        gen_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: white; border: none; border-radius: 5px; font-weight: 600;")
        gen_btn.clicked.connect(lambda: self.generate_keys(
            int(count_input.text() or 1),
            duration_combo.currentText()
        ))
        self.content_layout.addWidget(gen_btn)
        
        # Output
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setMaximumHeight(300)
        self.content_layout.addWidget(self.output_text)
        
        self.content_layout.addStretch()
    
    def show_validate(self):
        self.clear_content()
        
        label = QLabel("Validate License Key")
        label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.content_layout.addWidget(label)
        
        # Current HWID
        hwid = self.hwid_manager.get_hwid()
        hwid_label = QLabel(f"Your HWID: {hwid}")
        hwid_label.setStyleSheet("color: #666666; font-size: 11px; word-wrap: true;")
        self.content_layout.addWidget(hwid_label)
        
        # Key input
        key_label = QLabel("Enter License Key:")
        key_input = QLineEdit()
        key_input.setPlaceholderText("OWL-XXXXX-XXXXX-XXXXX-XXXXX")
        self.content_layout.addWidget(key_label)
        self.content_layout.addWidget(key_input)
        
        # Validate button
        validate_btn = QPushButton("Validate")
        validate_btn.setMinimumHeight(40)
        validate_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: white; border: none; border-radius: 5px; font-weight: 600;")
        validate_btn.clicked.connect(lambda: self.validate_key(key_input.text()))
        self.content_layout.addWidget(validate_btn)
        
        # Status
        self.status_label = QLabel("")
        self.content_layout.addWidget(self.status_label)
        
        self.content_layout.addStretch()
    
    def generate_keys(self, count, duration):
        keys = self.key_generator.generate_batch(count, duration)
        output = "Generated License Keys:\n\n"
        for key_info in keys:
            output += f"Key: {key_info['key']}\n"
            output += f"Duration: {key_info['duration']}\n"
            output += f"Created: {key_info['created_at']}\n\n"
        
        self.output_text.setText(output)
    
    def validate_key(self, key):
        hwid = self.hwid_manager.get_hwid()
        valid, message = self.license_manager.validate_license(key, hwid)
        
        if valid:
            self.status_label.setText(f"✓ {message}")
            self.status_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600;")
        else:
            self.status_label.setText(f"✗ {message}")
            self.status_label.setStyleSheet(f"color: {ERROR_COLOR}; font-weight: 600;")
