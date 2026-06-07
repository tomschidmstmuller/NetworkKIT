#!/bin/bash

# USMI ASCII Banner
c6='\033[36m'
c7='\033[37m'
reset='\033[0m'

echo -e "${c6}"
echo "   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"
echo "  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█"
echo "  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██"
echo "  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀"
echo "  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█"
echo "  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██"
echo "  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░"
echo -e "${c7}  UNIVERSAL SPACE MARINE INTELLIGENT${reset}"
echo

# ASCII Map NPM Runner for Ubuntu
# This script installs and runs a terminal-based ASCII map

set -e  # Exit on error

echo "🎨 Setting up ASCII Map for Ubuntu..."

# Update package list
echo "📦 Updating package list..."
sudo apt update

# Install Node.js and npm if not already installed
if ! command -v node &> /dev/null; then
    echo "📦 Installing Node.js and npm..."
    sudo apt install -y nodejs npm
else
    echo "✅ Node.js is already installed"
fi

# Choose which ASCII map package to use
echo ""
echo "Select an ASCII map package to install:"
echo "1) mapscii (terminal-based world map)"
echo "2) ttymap (interactive console map)"
echo "3) ascii-map (simple ASCII map viewer)"
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "🌍 Installing mapscii..."
        sudo npm install -g mapscii
        echo "🚀 Running mapscii..."
        mapscii
        ;;
    2)
        echo "🗺️ Installing ttymap..."
        sudo npm install -g ttymap
        echo "🚀 Running ttymap..."
        ttymap
        ;;
    3)
        echo "📐 Installing ascii-map..."
        npm install ascii-map
        echo "🚀 Running ascii-map..."
        # Create a simple demo script
        cat > /tmp/ascii-map-demo.js << 'EOF'
const asciiMap = require('ascii-map');
console.log(asciiMap.createWorldMap());
EOF
        node /tmp/ascii-map-demo.js
        ;;
    *)
        echo "❌ Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "✨ ASCII map closed. Have a great day!"
