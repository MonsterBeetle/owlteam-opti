from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QCheckBox, QProgressBar
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont
from core.optimizer import SystemOptimizer
from config.constants import ACCENT_COLOR, SUCCESS_COLOR

class CleanupWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(dict)
    
    def __init__(self, cleanup_types):
        super().__init__()
        self.cleanup_types = cleanup_types
        self.optimizer = SystemOptimizer()
    
    def run(self):
        results = self.optimizer.cleanup_system(self.cleanup_types)
        self.finished.emit(results)

class CleanupPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("System Cleanup")
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Checkboxes
        self.temp_checkbox = QCheckBox("Clean Temporary Files")
        self.temp_checkbox.setChecked(True)
        layout.addWidget(self.temp_checkbox)
        
        self.cache_checkbox = QCheckBox("Clean Cache")
        self.cache_checkbox.setChecked(True)
        layout.addWidget(self.cache_checkbox)
        
        self.prefetch_checkbox = QCheckBox("Clean Prefetch")
        self.prefetch_checkbox.setChecked(False)
        layout.addWidget(self.prefetch_checkbox)
        
        layout.addSpacing(20)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Start button
        start_btn = QPushButton("Start Cleanup")
        start_btn.setMinimumHeight(50)
        start_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        start_btn.setStyleSheet(f"""
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
        start_btn.clicked.connect(self.start_cleanup)
        layout.addWidget(start_btn)
        
        # Results label
        self.results_label = QLabel("")
        self.results_label.setStyleSheet(f"color: {SUCCESS_COLOR}; font-weight: 600;")
        layout.addWidget(self.results_label)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def start_cleanup(self):
        cleanup_types = []
        if self.temp_checkbox.isChecked():
            cleanup_types.append("temp")
        if self.cache_checkbox.isChecked():
            cleanup_types.append("cache")
        if self.prefetch_checkbox.isChecked():
            cleanup_types.append("prefetch")
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        self.worker = CleanupWorker(cleanup_types)
        self.worker.finished.connect(self.cleanup_finished)
        self.worker.start()
    
    def cleanup_finished(self, results):
        self.progress_bar.setValue(100)
        self.results_label.setText("✓ Cleanup completed successfully!")
