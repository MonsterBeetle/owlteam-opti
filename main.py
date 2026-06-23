import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from config.constants import APP_NAME, APP_VERSION

def main():
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
