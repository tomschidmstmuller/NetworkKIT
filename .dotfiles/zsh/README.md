# Wello this is for your own good, make sure you read the documentary markdowns before doing anytime 

## 🧪 `ZSH` Dotfiles Setup

> ⚠️ This repo and the `zsh/` folder can be cloned **anywhere**.
> But you'll probably want to remove it after installation to keep things clean.
> *Temporary, like your last situationship.*

---

### 📦 Install Dependencies

Before installing, **search** for the packages:

```bash
# Pacman users
sudo pacman -Ss zsh git

# AUR / yay users
yay -Ss zsh git
```

> This helps verify the package versions before pulling anything onto your machine.

Now install them:

```bash
# Pacman (official)
sudo pacman -S zsh git

# Yay (AUR and auto-version sync)
yay -Sy zsh git  # the -Sy updates before installing
```

---

### 🎨 Theme Setup (Default: powerlevel10k)

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/dotfiles/zsh/powerlevel10k
cd ~/dotfiles/zsh/powerlevel10k
./install.sh  # or source instructions from README
```

> Feel free to change the theme! Just replace the theme source path in `.zshrc` (or `.zshc` if you source it there).
> *Theme your shell like it's your bedroom.*

---

### 🧱 Your Dotfiles Layout

```
~/dotfiles/
├── zsh/
│   ├── .zshc           # Main zsh config
│   ├── aliases.zsh     # Custom aliases
│   ├── powerlevel10k/  # Cloned theme folder
│   └── plugins/        # (Optional) External plugins
└── install.sh          # Optional full setup script
```


---

### 🖋️ Font Requirements (or your shell will look jank 💀)

> For everything to look clean, iconic, and aligned properly, **Nerd Fonts are essential**.

Recommended fonts (install **all** if you're indecisive like me):

```bash
# JetBrains Mono Nerd Font
yay -S nerd-fonts-jetbrains-mono

# FiraCode Nerd Font
yay -S nerd-fonts-fira-code

# Meslo LG M Nerd Font (Powerlevel10k recommends this)
yay -S nerd-fonts-meslo-lg

# (Optional) Hack Nerd Font, SourceCodePro, etc
yay -Ss nerd-fonts | less
```

Make sure to:

* Set your **terminal font** to one of the above in your terminal emulator settings (Kitty, Alacritty, GNOME Terminal, etc.)
* For best compatibility with Powerlevel10k, use **MesloLGS NF**.

---

Let me know if you want to:

* Add plugin manager (like `zinit`, `antidote`, or `oh-my-zsh-lite`)
* Auto-symlink `.zshrc` from `.zshc`
* Include common plugins (like autosuggestions, syntax highlighting, etc.)
* Bundle a `p10k.zsh` config to skip the wizard

