"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT

Package installer backend with multi-distro support
"""

import subprocess
import sys
import platform
from typing import List, Optional

class PackageInstaller:
    def __init__(self):
        self.distro = self._detect_distro()
        self.has_nala = self._check_nala()
        
    def _detect_distro(self) -> str:
        """Detect Linux distribution"""
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = {}
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        os_info[key] = value.strip('"')
                if 'arch' in os_info.get('ID', '').lower():
                    return 'arch'
                elif 'ubuntu' in os_info.get('ID', '').lower() or 'debian' in os_info.get('ID', '').lower():
                    return 'debian'
                else:
                    return 'other'
        except:
            return 'other'
    
    def _check_nala(self) -> bool:
        """Check if nala is installed"""
        try:
            subprocess.run(['nala', '--version'], 
                          capture_output=True, check=True)
            return True
        except:
            return False
    
    def _run_command(self, cmd: List[str], progress_callback=None) -> bool:
        """Run a shell command with real-time output"""
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in process.stdout:
            if progress_callback:
                progress_callback(line.strip())
        
        process.wait()
        return process.returncode == 0
    
    def update_system(self, progress_callback=None) -> bool:
        """Update package lists"""
        if self.distro == 'arch':
            return self._run_command(['sudo', 'pacman', '-Sy'], progress_callback)
        else:
            if self.has_nala:
                return self._run_command(['sudo', 'nala', 'update'], progress_callback)
            else:
                return self._run_command(['sudo', 'apt', 'update'], progress_callback)
    
    def install_package(self, package_name: str, package_manager: str, 
                       progress_callback=None) -> bool:
        """Install a package using the appropriate package manager"""
        
        if package_manager == 'apt':
            if self.has_nala:
                cmd = ['sudo', 'nala', 'install', '-y', package_name]
            else:
                cmd = ['sudo', 'apt', 'install', '-y', package_name]
        elif package_manager == 'pacman':
            cmd = ['sudo', 'pacman', '-S', '--noconfirm', package_name]
        elif package_manager == 'aur':
            cmd = ['yay', '-S', '--noconfirm', package_name]
        else:
            return False
        
        if progress_callback:
            progress_callback(f"Installing {package_name}...")
        
        return self._run_command(cmd, progress_callback)
    
    def is_installed(self, package_name: str, package_manager: str) -> bool:
        """Check if a package is installed"""
        try:
            if package_manager in ['apt', 'debian']:
                result = subprocess.run(['dpkg', '-l', package_name], 
                                      capture_output=True, text=True)
                return result.returncode == 0 and 'ii' in result.stdout
            elif package_manager == 'pacman':
                result = subprocess.run(['pacman', '-Q', package_name],
                                      capture_output=True)
                return result.returncode == 0
            elif package_manager == 'aur':
                result = subprocess.run(['pacman', '-Q', package_name],
                                      capture_output=True)
                return result.returncode == 0
        except:
            pass
        return False
    
    def get_available_package_managers(self) -> List[str]:
        """Return list of available package managers for current distro"""
        managers = []
        if self.distro == 'debian':
            managers.append('apt')
        elif self.distro == 'arch':
            managers.append('pacman')
            try:
                subprocess.run(['yay', '--version'], capture_output=True, check=True)
                managers.append('aur')
            except:
                pass
        return managers
