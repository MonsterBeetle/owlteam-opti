import requests
import json
from typing import Optional

class AIBIOSAssistant:
    """
    AI BIOS Assistant for system optimization recommendations
    Uses local logic with optional API integration
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.bios_profiles = self._load_bios_profiles()
    
    def _load_bios_profiles(self):
        """Load predefined BIOS optimization profiles"""
        return {
            "gaming": {
                "XMP_Enabled": True,
                "CPU_Performance_Mode": "Ultra",
                "CPU_C-States": "Disabled",
                "Intel_SpeedStep": "Disabled",
                "Hyperthreading": True,
                "Turbo_Boost": "Enabled",
                "LLC_Level": 5,
                "Power_Limit": "Unlimited",
                "CPU_Vcore": "Auto",
                "SATA_Mode": "AHCI",
                "IOMMU": "Disabled",
                "CSM": "Disabled",
                "Fast_Boot": "Enabled"
            },
            "productivity": {
                "XMP_Enabled": True,
                "CPU_Performance_Mode": "Standard",
                "CPU_C-States": "Enabled",
                "Intel_SpeedStep": "Enabled",
                "Hyperthreading": True,
                "Turbo_Boost": "Enabled",
                "LLC_Level": 3,
                "Power_Limit": "Default",
                "SATA_Mode": "AHCI",
                "Fast_Boot": "Enabled"
            },
            "energy_saving": {
                "XMP_Enabled": False,
                "CPU_Performance_Mode": "Standard",
                "CPU_C-States": "Enabled",
                "Intel_SpeedStep": "Enabled",
                "Hyperthreading": True,
                "Turbo_Boost": "Disabled",
                "LLC_Level": 1,
                "Power_Limit": "Limited",
                "SATA_Mode": "AHCI",
                "Fast_Boot": "Enabled"
            },
            "streaming": {
                "XMP_Enabled": True,
                "CPU_Performance_Mode": "Ultra",
                "CPU_C-States": "Disabled",
                "Hyperthreading": True,
                "Turbo_Boost": "Enabled",
                "LLC_Level": 4,
                "Power_Limit": "Unlimited",
                "SATA_Mode": "AHCI",
                "Fast_Boot": "Enabled"
            }
        }
    
    def get_recommendation(self, use_case: str, system_info: dict = None) -> dict:
        """
        Get AI recommendation for BIOS settings based on use case
        """
        use_case = use_case.lower()
        
        if use_case not in self.bios_profiles:
            use_case = "gaming"
        
        profile = self.bios_profiles[use_case]
        
        return {
            "use_case": use_case,
            "profile": profile,
            "description": self._get_description(use_case),
            "performance_boost": self._estimate_performance(use_case),
            "power_usage": self._estimate_power(use_case)
        }
    
    def _get_description(self, use_case: str) -> str:
        """Get description of the profile"""
        descriptions = {
            "gaming": "Optimized for maximum FPS and gaming performance. Disables power saving features.",
            "productivity": "Balanced settings for productivity work with good performance and power efficiency.",
            "energy_saving": "Energy-efficient settings that reduce power consumption while maintaining usability.",
            "streaming": "Optimized for streaming with balanced CPU/GPU performance and stability."
        }
        return descriptions.get(use_case, "Custom profile")
    
    def _estimate_performance(self, use_case: str) -> str:
        """Estimate performance improvement"""
        estimates = {
            "gaming": "15-25% FPS improvement",
            "productivity": "5-15% performance improvement",
            "energy_saving": "Minimal performance impact, 30-40% power reduction",
            "streaming": "10-20% improvement in stream stability"
        }
        return estimates.get(use_case, "Varies")
    
    def _estimate_power(self, use_case: str) -> str:
        """Estimate power usage"""
        estimates = {
            "gaming": "High (100-150W CPU)",
            "productivity": "Medium (50-80W CPU)",
            "energy_saving": "Low (20-40W CPU)",
            "streaming": "High (80-120W CPU)"
        }
        return estimates.get(use_case, "Unknown")
    
    def generate_guide(self, profile_name: str) -> str:
        """Generate step-by-step BIOS configuration guide"""
        if profile_name not in self.bios_profiles:
            return "Profile not found"
        
        profile = self.bios_profiles[profile_name]
        guide = f"BIOS Configuration Guide - {profile_name.upper()}\n"
        guide += "=" * 50 + "\n\n"
        
        for setting, value in profile.items():
            guide += f"{setting}: {value}\n"
        
        guide += "\n" + "=" * 50 + "\n"
        guide += "How to apply:\n"
        guide += "1. Restart your PC\n"
        guide += "2. Press DEL or F2 during boot to enter BIOS\n"
        guide += "3. Navigate to each setting and apply the recommended value\n"
        guide += "4. Save and exit (F10)\n"
        
        return guide
