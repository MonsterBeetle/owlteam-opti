#!/usr/bin/env python3
"""
🔐 OwlTeam Opti - Advanced License Key Generator
Senior-level security with embedded key data.
No external database needed - everything is in the key!
"""

import json
from datetime import datetime
from pathlib import Path
from core.advanced_key_system import AdvancedKeyGenerator

class AdvancedKeyGeneratorCLI:
    def __init__(self):
        self.key_gen = AdvancedKeyGenerator()
        self.output_dir = Path("generated_keys")
        self.output_dir.mkdir(exist_ok=True)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*70)
        print(f"{'🔐 OwlTeam Opti - Advanced License Key Generator':^70}")
        print("="*70)
        print("\n[1] Generate single key")
        print("[2] Generate batch of keys")
        print("[3] View key info")
        print("[4] Exit\n")
    
    def generate_single(self):
        """Generate a single key"""
        print("\n📝 Single Key Generation\n")
        
        print("Select duration:")
        durations = {
            "1": (7, "7_days"),
            "2": (30, "30_days"),
            "3": (90, "90_days"),
            "4": (365, "365_days"),
            "5": (99999, "lifetime")
        }
        
        for key, (days, label) in durations.items():
            print(f"[{key}] {label} ({days} days)")
        
        choice = input("\nChoice: ").strip()
        
        if choice not in durations:
            print("❌ Invalid choice")
            return None
        
        days, label = durations[choice]
        
        try:
            key_data = self.key_gen.generate_key(days)
            
            print(f"\n✅ Key Generated Successfully!\n")
            print(f"Key: {key_data['key']}")
            print(f"Duration: {label}")
            print(f"Created: {key_data['created']}")
            print(f"Expires: {key_data['expires']}")
            print(f"\n📋 Copy this key and share with user!\n")
            
            return key_data
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def generate_batch(self):
        """Generate batch of keys"""
        print("\n📦 Batch Key Generation\n")
        
        try:
            count = int(input("Number of keys to generate: "))
            
            if count < 1 or count > 10000:
                print("❌ Count must be between 1 and 10000")
                return None
            
            print("\nSelect duration:")
            durations = {
                "1": (7, "7_days"),
                "2": (30, "30_days"),
                "3": (90, "90_days"),
                "4": (365, "365_days"),
                "5": (99999, "lifetime")
            }
            
            for key, (days, label) in durations.items():
                print(f"[{key}] {label}")
            
            choice = input("\nChoice: ").strip()
            
            if choice not in durations:
                print("❌ Invalid choice")
                return None
            
            days, duration_label = durations[choice]
            
            print(f"\n⏳ Generating {count} keys for {duration_label}...\n")
            
            keys = []
            for i in range(count):
                key_data = self.key_gen.generate_key(days)
                keys.append(key_data)
                
                # Progress indicator
                if (i + 1) % 10 == 0:
                    print(f"   Generated {i + 1}/{count} keys...")
            
            print(f"\n✅ Generated {len(keys)} keys!\n")
            print("-" * 70)
            
            for idx, key_info in enumerate(keys[:10], 1):
                print(f"{idx}. {key_info['key']}")
            
            if len(keys) > 10:
                print(f"... and {len(keys) - 10} more keys")
            
            print("-" * 70)
            
            # Save to file
            save = input("\nSave to file? (y/n): ").lower() == 'y'
            if save:
                self.save_keys_to_file(keys, duration_label)
            
            return keys
        
        except ValueError:
            print("❌ Invalid input")
            return None
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def save_keys_to_file(self, keys, duration):
        """Save keys to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"keys_{duration}_{timestamp}.json"
        
        data = {
            "generated_at": datetime.now().isoformat(),
            "duration": duration,
            "count": len(keys),
            "keys": keys,
            "note": "Each key contains all necessary data embedded. No database required!",
            "security_info": {
                "encryption": "AES-128 (Fernet)",
                "signature": "HMAC-SHA256",
                "hwid_binding": "SHA256 hash",
                "tampering_detection": "Enabled",
                "data_embedded_in_key": True
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Keys saved to: {filename}")
        print(f"\n📋 You can now:")
        print(f"   1. Copy keys from this file")
        print(f"   2. Share with users via email/telegram/discord")
        print(f"   3. Users activate in the app (License Manager → Validate)")
        print(f"   4. Done! No manual database operations needed!\n")
    
    def show_key_info(self):
        """Show information about key system"""
        print("\n" + "="*70)
        print("🔐 OwlTeam Opti Advanced Key System")
        print("="*70)
        print("""
🎯 Key Features:
   ✓ All data embedded in the key itself
   ✓ Encrypted with AES-128 (Fernet)
   ✓ Signed with HMAC-SHA256
   ✓ HWID binding prevents sharing
   ✓ Tampering detection
   ✓ Auto-expiration
   ✓ Zero database needed
   ✓ Works completely offline

📝 Key Format:
   OWL-[RANDOM_ID]-[ENCRYPTED_DATA]-[SIGNATURE]
   Example: OWL-ABCD1234EFGH5678-A1B2C3D4E5F6-X9Y8Z7W6V5

⏰ Duration Options:
   • 7_days - Testing/trial period
   • 30_days - Monthly subscription
   • 90_days - Quarterly subscription  
   • 365_days - Annual subscription
   • lifetime - Permanent access (VIP)

🔒 Security Layers:
   1. Encryption: All sensitive data encrypted in key
   2. Signature: HMAC prevents key modification
   3. HWID Binding: Locks key to specific PC
   4. Checksum: Detects tampering
   5. Expiration: Auto-expires keys

📊 How It Works:
   1. You generate key: python advanced_key_generator_cli.py
   2. Share key with user
   3. User enters in License Manager
   4. App validates (no internet needed!)
   5. App binds to user's HWID
   6. App stores locally
   7. Key auto-expires after duration

✅ No Setup Required:
   • No database to maintain
   • No server needed
   • No internet requirement
   • No external storage
   • Everything self-contained!
        """)
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.generate_single()
            
            elif choice == '2':
                self.generate_batch()
            
            elif choice == '3':
                self.show_key_info()
            
            elif choice == '4':
                print("\n👋 Goodbye!\n")
                break
            
            else:
                print("\n❌ Invalid choice")
            
            if choice in ['1', '2']:
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = AdvancedKeyGeneratorCLI()
    app.run()
