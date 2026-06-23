from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QFrame, QTextEdit, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from core.ai_assistant import AIBIOSAssistant
from config.constants import ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR

class BIOSAssistantPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ai_assistant = AIBIOSAssistant()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("🤖 AI BIOS Assistant")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Description
        desc = QLabel("Get AI-powered recommendations for your BIOS settings")
        desc.setStyleSheet("color: #666666; font-size: 12px;")
        layout.addWidget(desc)
        
        # Use case selection
        selection_layout = QHBoxLayout()
        selection_layout.addWidget(QLabel("Select your use case:"))
        
        self.use_case_combo = QComboBox()
        self.use_case_combo.addItems(["Gaming", "Productivity", "Energy Saving", "Streaming"])
        selection_layout.addWidget(self.use_case_combo)
        selection_layout.addStretch()
        
        layout.addLayout(selection_layout)
        
        # Recommendation button
        rec_btn = QPushButton("Get Recommendation")
        rec_btn.setMinimumHeight(40)
        rec_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #1E5A1F;
            }}
        """)
        rec_btn.clicked.connect(self.show_recommendation)
        layout.addWidget(rec_btn)
        
        # Content frame
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        self.content_layout = QVBoxLayout()
        self.content_frame.setLayout(self.content_layout)
        
        layout.addWidget(self.content_frame)
        
        # Output text
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("border: 1px solid #E0E0E0; border-radius: 5px;")
        self.content_layout.addWidget(self.output_text)
        
        # Guide button
        guide_btn = QPushButton("Generate Setup Guide")
        guide_btn.setMinimumHeight(35)
        guide_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: white; border: none; border-radius: 5px; font-weight: 600;")
        guide_btn.clicked.connect(self.generate_guide)
        self.content_layout.addWidget(guide_btn)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def show_recommendation(self):
        use_case = self.use_case_combo.currentText()
        recommendation = self.ai_assistant.get_recommendation(use_case)
        
        output = f"Use Case: {recommendation['use_case'].upper()}\n\n"
        output += f"📊 Performance Boost: {recommendation['performance_boost']}\n"
        output += f"⚡ Power Usage: {recommendation['power_usage']}\n\n"
        output += f"Description:\n{recommendation['description']}\n\n"
        output += "Recommended BIOS Settings:\n"
        output += "=" * 40 + "\n"
        
        for setting, value in recommendation['profile'].items():
            output += f"• {setting}: {value}\n"
        
        self.output_text.setText(output)
    
    def generate_guide(self):
        use_case = self.use_case_combo.currentText().lower()
        guide = self.ai_assistant.generate_guide(use_case)
        self.output_text.setText(guide)
