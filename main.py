from ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

# Import all pages to register them
from ui.pages.dashboard import DashboardPage
from ui.pages.games import GamesPage
from ui.pages.cleanup import CleanupPage
from ui.pages.tweaks import TweaksPage
from ui.pages.license_manager import LicenseManagerPage
from ui.pages.bios_assistant import BIOSAssistantPage
from ui.pages.boost_mode import BoostModePage
from ui.pages.settings import SettingsPage

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
