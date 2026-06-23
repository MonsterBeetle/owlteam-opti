import PyInstaller.__main__
import os
import shutil
from pathlib import Path

def build_exe():
    """Build OwlTeam Opti as standalone EXE"""
    
    print("🔨 Building OwlTeam Opti...")
    
    # Define build parameters
    spec_file = "owlteam.spec"
    
    # Create spec file
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['PyQt6', 'psutil', 'wmi', 'gputil'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OwlTeam-Opti',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/logo.ico',
)
'''
    
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    
    # Run PyInstaller
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--name=OwlTeam-Opti',
        '--icon=assets/logo.ico',
        '--add-data=assets:assets',
        '--hidden-import=PyQt6',
        '--hidden-import=psutil',
        '--hidden-import=wmi',
        '--hidden-import=gputil',
        '--specpath=build_temp',
        '--distpath=dist',
        '--buildpath=build_temp'
    ])
    
    print("✅ Build complete! EXE file is in dist/ folder")
    print("📦 File: dist/OwlTeam-Opti.exe")

if __name__ == '__main__':
    build_exe()
