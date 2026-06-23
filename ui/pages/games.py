from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from core.optimizer import SystemOptimizer
from config.constants import GAME_PRESETS, ACCENT_COLOR, SECONDARY_COLOR

class GamesPage(QWidget):
    def __init__(self):
        super().__init__()
        self.optimizer = SystemOptimizer()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("Game Optimization Presets")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Description
        desc = QLabel("Select your game for automatic optimization")
        desc.setStyleSheet("color: #666666; font-size: 12px;")
        layout.addWidget(desc)
        
        # Game buttons
        games_layout = QHBoxLayout()
        
        for game_name in GAME_PRESETS.keys():
            btn = self.create_game_button(game_name)
            games_layout.addWidget(btn)
        
        layout.addLayout(games_layout)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def create_game_button(self, game_name):
        frame = QFrame()
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {SECONDARY_COLOR};
                border-radius: 10px;
                border: 2px solid #E0E0E0;
            }}
        """)
        frame.setMinimumHeight(150)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Game name
        name_label = QLabel(game_name)
        name_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        layout.addWidget(name_label)
        
        # Optimize button
        btn = QPushButton("Optimize")
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #1E5A1F;
            }}
        """)
        btn.clicked.connect(lambda: self.optimize_game(game_name))
        layout.addStretch()
        layout.addWidget(btn)
        
        frame.setLayout(layout)
        return frame
    
    def optimize_game(self, game_name):
        preset = GAME_PRESETS.get(game_name)
        if preset:
            self.optimizer.apply_performance_mode("Performance")
            print(f"Optimized for {game_name}")
