#!/usr/bin/env bash
set -e

echo "📥 Downloading Meslo Nerd Font..."
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts

# Grab latest MesloLGS Nerd Font zip from Nerd Fonts repo
curl -fLo "Meslo.zip" https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip

echo "📦 Extracting Meslo fonts..."
unzip -o Meslo.zip
rm Meslo.zip

echo "🔄 Updating font cache..."
fc-cache -fv

echo "✅ MesloLGS Nerd Font installed! You can now set it in your terminal."

