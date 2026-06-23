from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from core.optimizer import SystemOptimizer
from config.constants import PERFORMANCE_MODES, ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR

class TweaksPage(QWidget):
    def __init__(self):
        super().__init__()
        self.optimizer = SystemOptimizer()
        self.current_mode = "Balanced"
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("Performance Tweaks & Modes")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Current mode
        mode_frame = QFrame()
        mode_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        mode_layout = QHBoxLayout()
        
        mode_label = QLabel("Current Mode:")
        mode_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        mode_layout.addWidget(mode_label)
        
        self.mode_value = QLabel(self.current_mode)
        self.mode_value.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.mode_value.setStyleSheet(f"color: {ACCENT_COLOR};")
        mode_layout.addWidget(self.mode_value)
        mode_layout.addStretch()
        
        mode_frame.setLayout(mode_layout)
        layout.addWidget(mode_frame)
        
        # Mode buttons
        modes_layout = QHBoxLayout()
        
        for mode_name in PERFORMANCE_MODES.keys():
            btn = QPushButton(mode_name)
            btn.setMinimumHeight(50)
            btn.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
            
            if mode_name == "BOOST":
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #FF6B6B;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }}
                    QPushButton:hover {{
                        background-color: #FF5252;
                    }}
                """)
            else:
                btn.setStyleSheet(f"""
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
            
            btn.clicked.connect(lambda checked, m=mode_name: self.apply_mode(m))
            modes_layout.addWidget(btn)
        
        layout.addLayout(modes_layout)
        
        # Status
        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600; margin-top: 20px;")
        layout.addWidget(self.status_label)
        
        # BOOST Mode description
        boost_desc = QLabel()
        boost_desc.setText(
            "🚀 BOOST Mode:\n"
            "• Disables unnecessary services\n"
            "• Removes animations\n"
            "• Maximizes CPU/GPU performance\n"
            "• Perfect for competitive gaming"
        )
        boost_desc.setStyleSheet("color: #666666; margin-top: 30px; background-color: #FFF8DC; padding: 15px; border-radius: 5px;")
        layout.addWidget(boost_desc)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def apply_mode(self, mode_name):
        success = self.optimizer.apply_performance_mode(mode_name)
        self.current_mode = mode_name
        self.mode_value.setText(mode_name)
        
        if success:
            self.status_label.setText(f"✓ {mode_name} mode activated successfully!")
        else:
            self.status_label.setText(f"✗ Failed to apply {mode_name} mode")
            self.status_label.setStyleSheet("color: #D32F2F; font-weight: 600;")
