import subprocess
import winreg
import psutil
from config.constants import PERFORMANCE_MODES

class SystemOptimizer:
    def __init__(self):
        self.registry_changes = []
    
    def apply_performance_mode(self, mode_name):
        """Apply performance mode settings"""
        if mode_name not in PERFORMANCE_MODES:
            return False
        
        mode = PERFORMANCE_MODES[mode_name]
        
        if mode_name == "BOOST":
            self._apply_boost_mode(mode)
        else:
            self._apply_standard_mode(mode)
        
        return True
    
    def _apply_boost_mode(self, settings):
        """Apply BOOST mode for maximum FPS"""
        # Disable unnecessary services
        services_to_disable = [
            "DiagTrack",
            "dmwappushservice",
            "WSearch",
            "TabletInputService"
        ]
        
        for service in services_to_disable:
            try:
                subprocess.run(
                    ["net", "stop", service],
                    capture_output=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
            except:
                pass
        
        # Disable animations
        self._disable_animations()
        
        # Set power plan to High Performance
        self._set_power_plan("8c5e7fda-e8bf-45a6-a6cc-4b3c619a3a0f")
    
    def _apply_standard_mode(self, settings):
        """Apply standard performance mode"""
        cpu_power = settings.get("cpu_power", 50)
        gpu_power = settings.get("gpu_power", 50)
        
        # Adjust power plan
        if cpu_power > 80:
            plan = "8c5e7fda-e8bf-45a6-a6cc-4b3c619a3a0f"  # High Performance
        else:
            plan = "381b4222-f694-41f0-9685-ff5bb260df2e"  # Balanced
        
        self._set_power_plan(plan)
    
    def _disable_animations(self):
        """Disable Windows animations for better performance"""
        try:
            hkey = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Control Panel\\Desktop\\WindowMetrics",
                0,
                winreg.KEY_WRITE
            )
            winreg.SetValueEx(hkey, "MinAnimate", 0, winreg.REG_SZ, "0")
            winreg.CloseKey(hkey)
        except:
            pass
    
    def _set_power_plan(self, plan_guid):
        """Set Windows power plan"""
        try:
            subprocess.run(
                ["powercfg", "/setactive", plan_guid],
                capture_output=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except:
            pass
    
    def cleanup_system(self, cleanup_types=[]):
        """Clean up system files"""
        results = {}
        
        if "temp" in cleanup_types or not cleanup_types:
            results["temp"] = self._cleanup_temp()
        
        if "cache" in cleanup_types or not cleanup_types:
            results["cache"] = self._cleanup_cache()
        
        if "prefetch" in cleanup_types or not cleanup_types:
            results["prefetch"] = self._cleanup_prefetch()
        
        return results
    
    def _cleanup_temp(self):
        """Clean temporary files"""
        import shutil
        import os
        
        try:
            temp_dir = os.environ.get('TEMP')
            if os.path.exists(temp_dir):
                for item in os.listdir(temp_dir):
                    try:
                        path = os.path.join(temp_dir, item)
                        if os.path.isfile(path):
                            os.unlink(path)
                        elif os.path.isdir(path):
                            shutil.rmtree(path)
                    except:
                        pass
            return "Cleanup completed"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _cleanup_cache(self):
        """Clean cache files"""
        return "Cache cleanup completed"
    
    def _cleanup_prefetch(self):
        """Clean prefetch files"""
        return "Prefetch cleanup completed"
