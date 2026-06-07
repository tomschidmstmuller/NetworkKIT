# Nerd Fonts – Meslo LG

Hey there, fellow font nerd 👀
This folder contains an archived patched version of **Meslo LG Nerd Font** (v1.21), ready for terminal awesomeness (not by me ofc)

---

## About Nerd Fonts 

Nerd Fonts patches developer-friendly monospace fonts with **icons and glyphs** so your terminal, Powerlevel10k, Starship, or other prompt looks 🔥.

Original release: [Nerd Fonts v3.4.0](https://github.com/ryanoasis/nerd-fonts/releases/latest)
Main repo: [https://github.com/ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts)

---

## About Meslo LG

* Meslo LG is a **customized version of Apple’s Menlo-Regular**, itself based on Bitstream Vera Sans Mono.
* This version is patched by [opeik](https://github.com/opeik) for Nerd Fonts icons.
* Upstream: [Meslo-Font](https://github.com/andreberg/Meslo-Font)

**Version:** 1.21

---

## Which Font Should I Pick?

### Quick TL;DR

* **Monospaced terminal-friendly:** choose `Nerd Font Mono` (NFM)
* **Bigger icons (\~1.5x letter width):** pick `Nerd Font` (NF)
* **GUI/proportional contexts:** pick `Nerd Font Propo` (NFP)

### Ligatures

* Ligatures are preserved in patched fonts (v2.1.0+).
* If your terminal supports ligatures and you don’t want them, disable them in your terminal settings.

---

## How to Install Fonts (User-Wide)

We’ve made this **easy-peasy** 😎 with `install.sh` — just drop it in the same folder as the `.ttf` files and run:

```bash
chmod +x install.sh
./install.sh
```

This script will:

1. Copy all `.ttf` files into your personal font folder: `~/.local/share/fonts`
2. Refresh your font cache automatically (`fc-cache -fv`)
3. Make Meslo Nerd Font available to your terminal or GUI apps

**Optional:** if you want system-wide installs, move the `.ttf` files into `/usr/share/fonts/` with `sudo`, then refresh the cache.

---

### How to Use in Your Terminal

1. Open your terminal → Preferences → Profile → Text → Custom Font
2. Pick `MesloLGS NF` as the font family
3. Restart the terminal for Starship / Powerlevel10k icons to show correctly

---

## Advanced Notes

### Option 1 – Download Already Patched

* Grab the latest release from [Nerd Fonts Releases](https://github.com/ryanoasis/nerd-fonts/releases)

### Option 2 – Patch Your Own

* Use the Nerd Fonts patcher for custom symbol sets or smaller sizes

FAQ & Troubleshooting: [Nerd Fonts Wiki](https://github.com/ryanoasis/nerd-fonts/wiki/FAQ-and-Troubleshooting#which-font)

---

## License

* [SIL Reserved Font Name (RFN)](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web_fonts_and_RFNs#14cbfd4a)

