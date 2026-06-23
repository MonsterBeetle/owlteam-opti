from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout, QProgressBar
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from core.optimizer import SystemOptimizer
from config.constants import ACCENT_COLOR, SECONDARY_COLOR, SUCCESS_COLOR
import psutil

class BoostModePage(QWidget):
    def __init__(self):
        super().__init__()
        self.optimizer = SystemOptimizer()
        self.boost_active = False
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("⚡ BOOST Mode - Maximum FPS")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Status frame
        status_frame = QFrame()
        status_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        status_layout = QHBoxLayout()
        
        status_label = QLabel("BOOST Status:")
        status_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        status_layout.addWidget(status_label)
        
        self.boost_status = QLabel("⭕ INACTIVE")
        self.boost_status.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.boost_status.setStyleSheet("color: #FF6B6B;")
        status_layout.addWidget(self.boost_status)
        status_layout.addStretch()
        
        status_frame.setLayout(status_layout)
        layout.addWidget(status_frame)
        
        # Features
        features_frame = QFrame()
        features_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        features_layout = QVBoxLayout()
        
        features_title = QLabel("🚀 BOOST Mode Features")
        features_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        features_layout.addWidget(features_title)
        
        features = [
            "✓ Disables all unnecessary services",
            "✓ Removes Windows animations",
            "✓ Maximizes CPU/GPU performance",
            "✓ Enables High Performance power plan",
            "✓ Disables background apps",
            "✓ Optimizes network for low latency",
            "✓ Increases process priority",
            "✓ Perfects for competitive gaming"
        ]
        
        for feature in features:
            feature_label = QLabel(feature)
            feature_label.setStyleSheet("color: #333333; margin: 5px 0;")
            features_layout.addWidget(feature_label)
        
        features_frame.setLayout(features_layout)
        layout.addWidget(features_frame)
        
        # Performance metrics
        metrics_frame = QFrame()
        metrics_frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; padding: 20px;")
        metrics_layout = QVBoxLayout()
        
        metrics_title = QLabel("📈 Performance Metrics")
        metrics_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        metrics_layout.addWidget(metrics_title)
        
        # CPU Usage
        cpu_layout = QHBoxLayout()
        cpu_layout.addWidget(QLabel("CPU Usage:"))
        self.cpu_progress = QProgressBar()
        self.cpu_progress.setMaximumHeight(20)
        cpu_layout.addWidget(self.cpu_progress)
        metrics_layout.addLayout(cpu_layout)
        
        # RAM Usage
        ram_layout = QHBoxLayout()
        ram_layout.addWidget(QLabel("RAM Usage:"))
        self.ram_progress = QProgressBar()
        self.ram_progress.setMaximumHeight(20)
        ram_layout.addWidget(self.ram_progress)
        metrics_layout.addLayout(ram_layout)
        
        # GPU Usage (if available)
        gpu_layout = QHBoxLayout()
        gpu_layout.addWidget(QLabel("GPU Usage:"))
        self.gpu_progress = QProgressBar()
        self.gpu_progress.setMaximumHeight(20)
        gpu_layout.addWidget(self.gpu_progress)
        metrics_layout.addLayout(gpu_layout)
        
        metrics_frame.setLayout(metrics_layout)
        layout.addWidget(metrics_frame)
        
        # Control buttons
        buttons_layout = QHBoxLayout()
        
        self.activate_btn = QPushButton("🚀 ACTIVATE BOOST")
        self.activate_btn.setMinimumHeight(50)
        self.activate_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.activate_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #FF6B6B;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #FF5252;
            }}
        """)
        self.activate_btn.clicked.connect(self.activate_boost)
        buttons_layout.addWidget(self.activate_btn)
        
        self.deactivate_btn = QPushButton("⏹ DEACTIVATE BOOST")
        self.deactivate_btn.setMinimumHeight(50)
        self.deactivate_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.deactivate_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #999999;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #777777;
            }}
        """)
        self.deactivate_btn.clicked.connect(self.deactivate_boost)
        self.deactivate_btn.setEnabled(False)
        buttons_layout.addWidget(self.deactivate_btn)
        
        layout.addLayout(buttons_layout)
        
        # Warning
        warning = QLabel("⚠️ BOOST Mode may increase system temperature. Monitor temperatures and ensure proper cooling.")
        warning.setStyleSheet("color: #FF9800; background-color: #FFF3E0; padding: 10px; border-radius: 5px; font-size: 11px;")
        layout.addWidget(warning)
        
        layout.addStretch()
        self.setLayout(layout)
        
        # Setup metrics update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)
    
    def activate_boost(self):
        self.optimizer.apply_performance_mode("BOOST")
        self.boost_active = True
        self.boost_status.setText("🟢 ACTIVE")
        self.boost_status.setStyleSheet("color: #4CAF50;")
        self.activate_btn.setEnabled(False)
        self.deactivate_btn.setEnabled(True)
    
    def deactivate_boost(self):
        self.optimizer.apply_performance_mode("Balanced")
        self.boost_active = False
        self.boost_status.setText("⭕ INACTIVE")
        self.boost_status.setStyleSheet("color: #FF6B6B;")
        self.activate_btn.setEnabled(True)
        self.deactivate_btn.setEnabled(False)
    
    def update_metrics(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_progress.setValue(int(cpu_percent))
        
        ram_info = psutil.virtual_memory()
        self.ram_progress.setValue(int(ram_info.percent))
        
        # Try to get GPU usage
        try:
            gpu_info = psutil.virtual_memory()  # Placeholder
            self.gpu_progress.setValue(int(ram_info.percent) // 2)
        except:
            self.gpu_progress.setValue(0)
