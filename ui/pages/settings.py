from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QCheckBox, QComboBox, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from config.settings import Settings
from config.constants import ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("Settings")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # General section
        general_frame = QFrame()
        general_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        general_layout = QVBoxLayout()
        
        general_title = QLabel("General Settings")
        general_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        general_layout.addWidget(general_title)
        
        # Checkboxes
        self.startup_checkbox = QCheckBox("Run at startup")
        self.startup_checkbox.setChecked(self.settings.get("startup", False))
        general_layout.addWidget(self.startup_checkbox)
        
        self.notifications_checkbox = QCheckBox("Enable notifications")
        self.notifications_checkbox.setChecked(self.settings.get("notification_enabled", True))
        general_layout.addWidget(self.notifications_checkbox)
        
        self.auto_cleanup_checkbox = QCheckBox("Auto cleanup on startup")
        self.auto_cleanup_checkbox.setChecked(self.settings.get("auto_cleanup", False))
        general_layout.addWidget(self.auto_cleanup_checkbox)
        
        general_frame.setLayout(general_layout)
        layout.addWidget(general_frame)
        
        # Appearance section
        appearance_frame = QFrame()
        appearance_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        appearance_layout = QVBoxLayout()
        
        appearance_title = QLabel("Appearance")
        appearance_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        appearance_layout.addWidget(appearance_title)
        
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        self.theme_combo.setCurrentText(self.settings.get("theme", "light").capitalize())
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        appearance_layout.addLayout(theme_layout)
        
        appearance_frame.setLayout(appearance_layout)
        layout.addWidget(appearance_frame)
        
        # Save button
        save_btn = QPushButton("Save Settings")
        save_btn.setMinimumHeight(45)
        save_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        save_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: white; border: none; border-radius: 5px;")
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)
        
        # Status
        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600;")
        layout.addWidget(self.status_label)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def save_settings(self):
        self.settings.set("startup", self.startup_checkbox.isChecked())
        self.settings.set("notification_enabled", self.notifications_checkbox.isChecked())
        self.settings.set("auto_cleanup", self.auto_cleanup_checkbox.isChecked())
        self.settings.set("theme", self.theme_combo.currentText().lower())
        
        self.status_label.setText("✓ Settings saved successfully!")
