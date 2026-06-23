#!/bin/bash
# OwlTeam Opti - Build to EXE

echo "🔨 Building OwlTeam Opti..."
echo "============================="
echo ""

echo "1️⃣  Installing PyInstaller..."
pip install pyinstaller

echo ""
echo "2️⃣  Building application..."
python build.py

echo ""
echo "✅ Build complete!"
echo "📦 File: dist/OwlTeam-Opti"
