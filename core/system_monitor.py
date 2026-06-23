import psutil
import threading
from collections import deque
from datetime import datetime

class SystemMonitor:
    def __init__(self, history_size=60):
        self.history_size = history_size
        self.cpu_history = deque(maxlen=history_size)
        self.ram_history = deque(maxlen=history_size)
        self.gpu_history = deque(maxlen=history_size)
        self.temp_history = deque(maxlen=history_size)
        self.running = False
    
    def get_cpu_usage(self):
        """Get current CPU usage percentage"""
        return psutil.cpu_percent(interval=0.1)
    
    def get_ram_usage(self):
        """Get RAM usage info"""
        mem = psutil.virtual_memory()
        return {
            "used": mem.used / (1024**3),
            "total": mem.total / (1024**3),
            "percent": mem.percent
        }
    
    def get_disk_usage(self):
        """Get disk usage for main drive"""
        disk = psutil.disk_usage('C:\\')
        return {
            "used": disk.used / (1024**3),
            "total": disk.total / (1024**3),
            "percent": disk.percent
        }
    
    def get_temperatures(self):
        """Get system temperatures"""
        try:
            temps = psutil.sensors_temperatures()
            result = {}
            for name, entries in temps.items():
                for entry in entries:
                    result[entry.label or name] = entry.current
            return result
        except:
            return {}
    
    def get_network_stats(self):
        """Get network statistics"""
        net = psutil.net_io_counters()
        return {
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv,
            "packets_sent": net.packets_sent,
            "packets_recv": net.packets_recv
        }
    
    def get_process_count(self):
        """Get number of running processes"""
        return len(psutil.pids())
    
    def update_history(self):
        """Update history with current values"""
        self.cpu_history.append(self.get_cpu_usage())
        self.ram_history.append(self.get_ram_usage()["percent"])
        self.temp_history.append(self.get_temperatures())
    
    def get_system_info(self):
        """Get complete system information"""
        return {
            "cpu_count": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq().current if psutil.cpu_freq() else 0,
            "boot_time": datetime.fromtimestamp(psutil.boot_time()),
            "uptime_seconds": datetime.now().timestamp() - psutil.boot_time()
        }
