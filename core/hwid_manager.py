import hashlib
import uuid
import subprocess
import re
from pathlib import Path

class HWIDManager:
    def __init__(self):
        self.hwid_file = Path.home() / ".owlteam_opti" / "hwid.txt"
    
    def get_hwid(self):
        """Generate or retrieve HWID based on hardware"""
        if self.hwid_file.exists():
            with open(self.hwid_file, 'r') as f:
                return f.read().strip()
        
        hwid = self._generate_hwid()
        self.hwid_file.parent.mkdir(exist_ok=True)
        with open(self.hwid_file, 'w') as f:
            f.write(hwid)
        return hwid
    
    def _generate_hwid(self):
        """Generate HWID from hardware components"""
        try:
            # Get CPU ID
            cpu_id = self._get_cpu_id()
            # Get Motherboard Serial
            mb_serial = self._get_motherboard_serial()
            # Get Disk Serial
            disk_serial = self._get_disk_serial()
            
            # Combine and hash
            combined = f"{cpu_id}{mb_serial}{disk_serial}"
            hwid = hashlib.sha256(combined.encode()).hexdigest()[:32].upper()
            return hwid
        except:
            return str(uuid.uuid4()).replace('-', '')[:32].upper()
    
    def _get_cpu_id(self):
        try:
            result = subprocess.check_output(
                "wmic cpu get ProcessorId",
                shell=True,
                stderr=subprocess.DEVNULL
            )
            return result.decode().split('\n')[1].strip()
        except:
            return "CPU_UNKNOWN"
    
    def _get_motherboard_serial(self):
        try:
            result = subprocess.check_output(
                "wmic baseboard get serialnumber",
                shell=True,
                stderr=subprocess.DEVNULL
            )
            return result.decode().split('\n')[1].strip()
        except:
            return "MB_UNKNOWN"
    
    def _get_disk_serial(self):
        try:
            result = subprocess.check_output(
                "wmic logicaldisk get VolumeSerialNumber",
                shell=True,
                stderr=subprocess.DEVNULL
            )
            lines = result.decode().split('\n')
            return lines[1].strip() if len(lines) > 1 else "DISK_UNKNOWN"
        except:
            return "DISK_UNKNOWN"
