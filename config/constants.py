# OwlTeam Opti - Constants

# Application Info
APP_NAME = "OwlTeam Opti"
APP_VERSION = "1.0.0"
APP_AUTHOR = "OwlTeam"

# UI Colors
PRIMARY_COLOR = "#FFFFFF"
SECONDARY_COLOR = "#F5F5F5"
ACCENT_COLOR = "#2E7D32"
DARK_TEXT = "#1A1A1A"
LIGHT_TEXT = "#CCCCCC"
ERROR_COLOR = "#D32F2F"
WARNING_COLOR = "#F57F17"
SUCCESS_COLOR = "#388E3C"

# Window Size
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 800

# Games Presets
GAME_PRESETS = {
    "Apex Legends": {
        "gpu_power": 100,
        "cpu_boost": 95,
        "ram_optimize": True,
        "network_priority": True,
        "resolution_scale": 1.0
    },
    "CS2": {
        "gpu_power": 100,
        "cpu_boost": 100,
        "ram_optimize": True,
        "network_priority": True,
        "resolution_scale": 1.0
    },
    "PUBG": {
        "gpu_power": 95,
        "cpu_boost": 90,
        "ram_optimize": True,
        "network_priority": True,
        "resolution_scale": 0.95
    },
    "Rust": {
        "gpu_power": 90,
        "cpu_boost": 85,
        "ram_optimize": True,
        "network_priority": False,
        "resolution_scale": 0.9
    },
    "GTA V": {
        "gpu_power": 90,
        "cpu_boost": 80,
        "ram_optimize": True,
        "network_priority": False,
        "resolution_scale": 0.85
    }
}

# License Settings
LICENSE_DURATION_DAYS = {
    "7_days": 7,
    "30_days": 30,
    "90_days": 90,
    "365_days": 365,
    "lifetime": 99999
}

# Cleanup Paths
CLEANUP_PATHS = {
    "temp": ["C:\\Windows\\Temp", "C:\\Users\\*\\AppData\\Local\\Temp"],
    "prefetch": ["C:\\Windows\\Prefetch"],
    "cache": ["C:\\Users\\*\\AppData\\Local\\Cache"],
    "recycle": ["C:\\$Recycle.bin"]
}

# Performance Modes
PERFORMANCE_MODES = {
    "Balanced": {"cpu_power": 50,
                 "gpu_power": 50,
                 "ram_aggressive": False},
    "Performance": {
        "cpu_power": 80,
        "gpu_power": 80,
        "ram_aggressive": True
    },
    "BOOST": {
        "cpu_power": 100,
        "gpu_power": 100,
        "ram_aggressive": True,
        "disable_animations": True,
        "disable_background_apps": True
    }
}