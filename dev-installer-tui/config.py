"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT

Package categories and their respective package managers
"""

PACKAGES = {
    "Code Editors": {
        "Visual Studio Code": {"apt": "code", "pacman": "code", "aur": "visual-studio-code-bin"},
        "Vim": {"apt": "vim", "pacman": "vim", "aur": "vim"},
        "Neovim": {"apt": "neovim", "pacman": "neovim", "aur": "neovim"},
        "Sublime Text": {"apt": "sublime-text", "pacman": "sublime-text", "aur": "sublime-text-4"},
        "Emacs": {"apt": "emacs", "pacman": "emacs", "aur": "emacs"},
    },
    "Version Control": {
        "Git": {"apt": "git", "pacman": "git", "aur": "git"},
        "Git LFS": {"apt": "git-lfs", "pacman": "git-lfs", "aur": "git-lfs"},
        "Subversion": {"apt": "subversion", "pacman": "subversion", "aur": "subversion"},
        "Mercurial": {"apt": "mercurial", "pacman": "mercurial", "aur": "mercurial"},
    },
    "Programming Languages": {
        "Python": {"apt": "python3 python3-pip", "pacman": "python python-pip", "aur": "python python-pip"},
        "Node.js": {"apt": "nodejs npm", "pacman": "nodejs npm", "aur": "nodejs npm"},
        "Go": {"apt": "golang", "pacman": "go", "aur": "go"},
        "Rust": {"apt": "rustc cargo", "pacman": "rust", "aur": "rust"},
        "Java (OpenJDK)": {"apt": "openjdk-17-jdk", "pacman": "jdk17-openjdk", "aur": "jdk17-openjdk"},
        "Ruby": {"apt": "ruby-full", "pacman": "ruby", "aur": "ruby"},
    },
    "Build Tools": {
        "Make": {"apt": "make", "pacman": "make", "aur": "make"},
        "CMake": {"apt": "cmake", "pacman": "cmake", "aur": "cmake"},
        "GCC": {"apt": "gcc g++", "pacman": "gcc", "aur": "gcc"},
        "Clang": {"apt": "clang", "pacman": "clang", "aur": "clang"},
        "Ninja": {"apt": "ninja-build", "pacman": "ninja", "aur": "ninja"},
    },
    "Package Managers": {
        "pip": {"apt": "python3-pip", "pacman": "python-pip", "aur": "python-pip"},
        "npm": {"apt": "npm", "pacman": "npm", "aur": "npm"},
        "yarn": {"apt": "yarn", "pacman": "yarn", "aur": "yarn"},
        "pnpm": {"apt": "pnpm", "pacman": "pnpm", "aur": "pnpm"},
        "cargo": {"apt": "cargo", "pacman": "rust", "aur": "rust"},
    },
    "Containers & Virtualization": {
        "Docker": {"apt": "docker.io", "pacman": "docker", "aur": "docker"},
        "Docker Compose": {"apt": "docker-compose", "pacman": "docker-compose", "aur": "docker-compose"},
        "Podman": {"apt": "podman", "pacman": "podman", "aur": "podman"},
        "VirtualBox": {"apt": "virtualbox", "pacman": "virtualbox", "aur": "virtualbox-bin"},
    },
    "Database Tools": {
        "PostgreSQL": {"apt": "postgresql postgresql-contrib", "pacman": "postgresql", "aur": "postgresql"},
        "MySQL": {"apt": "mysql-server", "pacman": "mariadb", "aur": "mysql"},
        "MongoDB": {"apt": "mongodb", "pacman": "mongodb", "aur": "mongodb-bin"},
        "Redis": {"apt": "redis-server", "pacman": "redis", "aur": "redis"},
    },
}
