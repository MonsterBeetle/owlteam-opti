#!/usr/bin/env python3
"""
🔑 OwlTeam Opti - License Key Generator

Программа для генерации лицензионных ключей для OwlTeam Opti
Позволяет создавать пакеты ключей с разными сроками действия
"""

import json
import os
from datetime import datetime
from pathlib import Path
from tools.key_generator import KeyGenerator
from core.license_manager import LicenseManager
from config.constants import LICENSE_DURATION_DAYS

class KeyGeneratorApp:
    def __init__(self):
        self.key_gen = KeyGenerator()
        self.license_manager = LicenseManager()
        self.output_dir = Path("generated_keys")
        self.output_dir.mkdir(exist_ok=True)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print(f"{'🔑 OwlTeam Opti - License Key Generator':^60}")
        print("="*60)
        print("\n[1] Generate single key")
        print("[2] Generate batch of keys")
        print("[3] Export keys to file")
        print("[4] View key formats")
        print("[5] Exit\n")
    
    def generate_single(self):
        """Generate a single key"""
        print("\n📝 Single Key Generation\n")
        
        print("Select duration:")
        for idx, duration in enumerate(LICENSE_DURATION_DAYS.keys(), 1):
            print(f"[{idx}] {duration}")
        
        choice = input("\nChoice: ").strip()
        
        try:
            durations = list(LICENSE_DURATION_DAYS.keys())
            duration = durations[int(choice) - 1]
            
            key = self.key_gen.generate_key()
            
            print(f"\n✅ Key Generated Successfully!\n")
            print(f"Key: {key}")
            print(f"Duration: {duration}")
            print(f"Days: {LICENSE_DURATION_DAYS[duration]}")
            print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            return key, duration
        except:
            print("❌ Invalid choice")
            return None, None
    
    def generate_batch(self):
        """Generate batch of keys"""
        print("\n📦 Batch Key Generation\n")
        
        try:
            count = int(input("Number of keys to generate: "))
            
            print("\nSelect duration:")
            for idx, duration in enumerate(LICENSE_DURATION_DAYS.keys(), 1):
                print(f"[{idx}] {duration}")
            
            choice = input("\nChoice: ").strip()
            durations = list(LICENSE_DURATION_DAYS.keys())
            duration = durations[int(choice) - 1]
            
            print(f"\n⏳ Generating {count} keys...\n")
            
            keys = self.key_gen.generate_batch(count, duration)
            
            print(f"✅ Generated {len(keys)} keys!\n")
            print("-" * 60)
            
            for idx, key_info in enumerate(keys, 1):
                print(f"{idx}. {key_info['key']} ({duration})")
            
            print("-" * 60)
            
            # Save to file
            save = input("\nSave to file? (y/n): ").lower() == 'y'
            if save:
                self.save_keys_to_file(keys, duration)
            
            return keys
        except ValueError:
            print("❌ Invalid input")
            return None
    
    def save_keys_to_file(self, keys, duration):
        """Save keys to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"keys_{duration}_{timestamp}.json"
        
        data = {
            "generated_at": datetime.now().isoformat(),
            "duration": duration,
            "days": LICENSE_DURATION_DAYS[duration],
            "count": len(keys),
            "keys": keys
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Keys saved to: {filename}")
    
    def show_key_formats(self):
        """Show key format information"""
        print("\n" + "="*60)
        print("📋 Key Format Information")
        print("="*60)
        print("\nKey Format: OWL-XXXXX-XXXXX-XXXXX-XXXXX")
        print("\nExample keys:")
        for _ in range(5):
            print(f"  {self.key_gen.generate_key()}")
        
        print("\nKey Properties:")
        print("  ✓ Prefix: OWL (OwlTeam)")
        print("  ✓ Length: 29 characters total")
        print("  ✓ Format: [PREFIX]-[5][5][5][5]")
        print("  ✓ Characters: A-Z, 0-9")
        print("  ✓ Each key is unique and randomly generated")
        print("  ✓ HWID-bound (cannot be shared between PCs)")
        print("  ✓ Time-limited (1-365 days or lifetime)")
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("Select option: ").strip()
            
            if choice == '1':
                key, duration = self.generate_single()
                if key:
                    self.save_keys_to_file([{"key": key, "duration": duration, "created_at": datetime.now().isoformat()}], duration)
            
            elif choice == '2':
                self.generate_batch()
            
            elif choice == '3':
                # Already handled in generate_batch
                print("\n💡 Use 'Generate batch' and save option instead")
            
            elif choice == '4':
                self.show_key_formats()
            
            elif choice == '5':
                print("\n👋 Goodbye!\n")
                break
            
            else:
                print("\n❌ Invalid choice")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = KeyGeneratorApp()
    app.run()
