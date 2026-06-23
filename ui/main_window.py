from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QFrame
)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QIcon, QPixmap, QColor
from ui.pages.dashboard import DashboardPage
from ui.pages.games import GamesPage
from ui.pages.cleanup import CleanupPage
from ui.pages.tweaks import TweaksPage
from ui.pages.license_manager import LicenseManagerPage
from ui.pages.settings import SettingsPage
from config.constants import *
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.setStyleSheet(self.get_stylesheet())
        
        # Main container
        container = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        layout.addWidget(sidebar, 1)
        
        # Content area
        content_area = self.create_content_area()
        layout.addWidget(content_area, 4)
        
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-right: 1px solid #E0E0E0;")
        sidebar.setMaximumWidth(250)
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 20, 15, 20)
        
        # Logo
        logo_label = QLabel("🦇 OWLTEAM")
        logo_font = QFont("Segoe UI", 14, QFont.Weight.Bold)
        logo_label.setFont(logo_font)
        logo_label.setStyleSheet(f"color: {ACCENT_COLOR}; margin-bottom: 30px;")
        layout.addWidget(logo_label)
        
        # Navigation buttons
        self.pages_info = [
            ("📊 Dashboard", "dashboard"),
            ("🎮 Games", "games"),
            ("🧹 Cleanup", "cleanup"),
            ("⚙️ Tweaks", "tweaks"),
            ("🔐 License", "license"),
            ("⚡ BOOST Mode", "boost"),
            ("⚙️ Settings", "settings")
        ]
        
        self.nav_buttons = {}
        for label, page_id in self.pages_info:
            btn = self.create_nav_button(label, page_id)
            layout.addWidget(btn)
            self.nav_buttons[page_id] = btn
        
        layout.addStretch()
        
        # Version label
        version_label = QLabel(f"v{APP_VERSION}")
        version_label.setStyleSheet(f"color: #999999; font-size: 10px;")
        layout.addWidget(version_label)
        
        sidebar.setLayout(layout)
        return sidebar
    
    def create_nav_button(self, label, page_id):
        btn = QPushButton(label)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {DARK_TEXT};
                border: none;
                padding: 12px;
                text-align: left;
                font-size: 12px;
                font-weight: 600;
                border-radius: 5px;
                margin: 5px 0;
            }}
            QPushButton:hover {{
                background-color: #E8E8E8;
            }}
            QPushButton:pressed {{
                background-color: {ACCENT_COLOR};
                color: white;
            }}
        """)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.clicked.connect(lambda: self.switch_page(page_id))
        return btn
    
    def create_content_area(self):
        self.stacked_widget = QStackedWidget()
        
        # Add pages
        self.dashboard_page = DashboardPage()
        self.games_page = GamesPage()
        self.cleanup_page = CleanupPage()
        self.tweaks_page = TweaksPage()
        self.license_page = LicenseManagerPage()
        self.settings_page = SettingsPage()
        
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.games_page)
        self.stacked_widget.addWidget(self.cleanup_page)
        self.stacked_widget.addWidget(self.tweaks_page)
        self.stacked_widget.addWidget(self.license_page)
        self.stacked_widget.addWidget(self.settings_page)
        
        return self.stacked_widget
    
    def switch_page(self, page_id):
        page_map = {
            "dashboard": 0,
            "games": 1,
            "cleanup": 2,
            "tweaks": 3,
            "license": 4,
            "settings": 5
        }
        
        if page_id in page_map:
            self.stacked_widget.setCurrentIndex(page_map[page_id])
            
            # Update button styles
            for btn_id, btn in self.nav_buttons.items():
                if btn_id == page_id:
                    btn.setStyleSheet(btn.styleSheet().replace(
                        "background-color: transparent;",
                        f"background-color: {ACCENT_COLOR};"
                    ).replace(
                        f"color: {DARK_TEXT};",
                        "color: white;"
                    ))
                else:
                    btn.setStyleSheet(btn.styleSheet().replace(
                        f"background-color: {ACCENT_COLOR};",
                        "background-color: transparent;"
                    ).replace(
                        "color: white;",
                        f"color: {DARK_TEXT};"
                    ))
    
    def get_stylesheet(self):
        return f"""
            QMainWindow {{
                background-color: {PRIMARY_COLOR};
                color: {DARK_TEXT};
            }}
            QWidget {{
                background-color: {PRIMARY_COLOR};
            }}
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
            QLabel {{
                color: {DARK_TEXT};
            }}
            QLineEdit, QTextEdit {{
                background-color: {SECONDARY_COLOR};
                border: 1px solid #D0D0D0;
                padding: 8px;
                border-radius: 4px;
                color: {DARK_TEXT};
            }}
        """
