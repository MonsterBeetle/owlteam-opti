from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QFrame
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from core.system_monitor import SystemMonitor
from config.constants import *
import psutil

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.monitor = SystemMonitor()
        self.init_ui()
        self.setup_timer()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("System Dashboard")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # System stats
        stats_layout = QHBoxLayout()
        
        self.cpu_widget = self.create_stat_widget("CPU Usage", "0%")
        self.ram_widget = self.create_stat_widget("RAM Usage", "0%")
        self.disk_widget = self.create_stat_widget("Disk Usage", "0%")
        self.temp_widget = self.create_stat_widget("Temp", "0°C")
        
        stats_layout.addWidget(self.cpu_widget)
        stats_layout.addWidget(self.ram_widget)
        stats_layout.addWidget(self.disk_widget)
        stats_layout.addWidget(self.temp_widget)
        
        layout.addLayout(stats_layout)
        
        # Details
        details_layout = QHBoxLayout()
        self.cpu_bar = self.create_progress_bar("CPU")
        self.ram_bar = self.create_progress_bar("RAM")
        details_layout.addWidget(self.cpu_bar)
        details_layout.addWidget(self.ram_bar)
        layout.addLayout(details_layout)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def create_stat_widget(self, title, value):
        frame = QFrame()
        frame.setStyleSheet(f"background-color: {SECONDARY_COLOR}; border-radius: 10px; border: 1px solid #E0E0E0;")
        frame.setMinimumHeight(120)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        title_label.setStyleSheet(f"color: #666666;")
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        value_label.setStyleSheet(f"color: {ACCENT_COLOR};")
        
        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(value_label)
        
        frame.setLayout(layout)
        
        # Store reference for updates
        frame.value_label = value_label
        
        return frame
    
    def create_progress_bar(self, label):
        frame = QFrame()
        frame.setStyleSheet(f"background-color: transparent;")
        
        layout = QVBoxLayout()
        
        title = QLabel(label)
        title.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        layout.addWidget(title)
        
        progress = QProgressBar()
        progress.setStyleSheet(f"""
            QProgressBar {{
                background-color: {SECONDARY_COLOR};
                border: none;
                border-radius: 5px;
                height: 20px;
            }}
            QProgressBar::chunk {{
                background-color: {ACCENT_COLOR};
                border-radius: 5px;
            }}
        """)
        layout.addWidget(progress)
        
        frame.setLayout(layout)
        frame.progress = progress
        
        return frame
    
    def setup_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)  # Update every second
    
    def update_stats(self):
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_widget.value_label.setText(f"{cpu_percent}%")
        self.cpu_bar.progress.setValue(int(cpu_percent))
        
        # RAM
        ram_info = self.monitor.get_ram_usage()
        self.ram_widget.value_label.setText(f"{ram_info['percent']}%")
        self.ram_bar.progress.setValue(int(ram_info['percent']))
        
        # Disk
        disk_info = self.monitor.get_disk_usage()
        self.disk_widget.value_label.setText(f"{disk_info['percent']}%")
        
        # Temp
        temps = self.monitor.get_temperatures()
        if temps:
            avg_temp = sum(temps.values()) / len(temps)
            self.temp_widget.value_label.setText(f"{avg_temp:.1f}°C")
