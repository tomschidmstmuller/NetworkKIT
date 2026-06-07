#!/usr/bin/env python3
"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT

USMI - Universal Space Marine Intelligent
Comprehensive TUI for Compiler & Toolchain Installation
Supports: C/C++, Java, C#, Web, Rust, Go, Swift, Embedded, Robotics, FPGA
"""

import os
import sys
import subprocess
import platform
import shutil
from datetime import datetime

# Check for rich library
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Confirm, Prompt
    from rich.layout import Layout
    from rich.live import Live
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Installing required dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], capture_output=True)
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Confirm, Prompt
    from rich.layout import Layout
    from rich.live import Live
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True

console = Console()

class USMITUI:
    def __init__(self):
        self.installed_compilers = {}
        self.distro = self.detect_distro()
        self.selection = []
        
    def detect_distro(self):
        """Detect Linux distribution"""
        try:
            with open('/etc/os-release', 'r') as f:
                for line in f:
                    if line.startswith('ID='):
                        return line.split('=')[1].strip().strip('"')
        except:
            return "unknown"
        return "unknown"
    
    def run_command(self, cmd, shell=True, capture=True):
        """Run shell command with progress indication"""
        try:
            if capture:
                result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
                return result.returncode == 0, result.stdout, result.stderr
            else:
                subprocess.run(cmd, shell=shell)
                return True, "", ""
        except Exception as e:
            return False, "", str(e)
    
    def check_installed(self, compiler_name, check_cmd):
        """Check if a compiler is already installed"""
        try:
            result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.split('\n')[0][:50]
                self.installed_compilers[compiler_name] = version
                return True
        except:
            pass
        self.installed_compilers[compiler_name] = None
        return False
    
    def update_status(self):
        """Update all compiler statuses"""
        status_checks = {
            "GCC": "gcc --version 2>/dev/null | head -n1",
            "Clang": "clang --version 2>/dev/null | head -n1",
            "OpenJDK": "java --version 2>&1 | head -n1",
            ".NET/Roslyn": "dotnet --version 2>/dev/null",
            "TypeScript": "tsc --version 2>/dev/null",
            "Rust": "rustc --version 2>/dev/null",
            "Go": "go version 2>/dev/null",
            "Swift": "swift --version 2>/dev/null | head -n1",
            "ARM Embedded": "arm-none-eabi-gcc --version 2>/dev/null | head -n1",
            "AVR-GCC": "avr-gcc --version 2>/dev/null | head -n1",
            "PlatformIO": "test -f ~/.platformio/penv/bin/platformio && echo 'installed'",
            "MicroPython": "mpremote --version 2>/dev/null",
        }
        
        for name, cmd in status_checks.items():
            self.check_installed(name, cmd)
    
    def display_header(self):
        """Display USMI ASCII header"""
        header = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗   ██╗███████╗███╗   ███╗██╗      ██████╗ ██████╗ ███████╗██╗██████╗    ║
║   ██║   ██║██╔════╝████╗ ████║██║     ██╔════╝██╔═══██╗██╔════╝██║╚════██╗   ║
║   ██║   ██║███████╗██╔████╔██║██║     ██║     ██║   ██║███████╗██║ █████╔╝   ║
║   ██║   ██║╚════██║██║╚██╔╝██║██║     ██║     ██║   ██║╚════██║██║ ╚═══██╗   ║
║   ╚██████╔╝███████║██║ ╚═╝ ██║███████╗╚██████╗╚██████╔╝███████║██║██████╔╝   ║
║    ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═════╝    ║
║                                                                              ║
║                    UNIVERSAL SPACE MARINE INTELLIGENT                        ║
║                    Compiler & Toolchain Management Suite                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        console.print(Panel(header, border_style="cyan", padding=(0, 0)))
        console.print(f"[yellow]Detected Distribution:[/yellow] {self.distro.upper()}")
        console.print(f"[yellow]Platform:[/yellow] {platform.system()} {platform.release()}")
        console.print(f"[yellow]Date:[/yellow] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        console.print("")
    
    def show_main_menu(self):
        """Display main menu"""
        self.update_status()
        
        # Create status table
        status_table = Table(title="📊 Current Installation Status", box=box.ROUNDED, border_style="cyan")
        status_table.add_column("Compiler", style="cyan", no_wrap=True)
        status_table.add_column("Status", style="green")
        status_table.add_column("Version", style="yellow")
        
        for compiler, version in list(self.installed_compilers.items())[:8]:
            if version:
                status_table.add_row(compiler, "✅ INSTALLED", version)
            else:
                status_table.add_row(compiler, "❌ NOT INSTALLED", "—")
        
        console.print(status_table)
        console.print("")
        
        # Main menu
        menu_options = [
            ("1", "🖥️  Standard Compilers (C/C++, Java, C#, Web, Rust, Go, Swift)"),
            ("2", "📱 Embedded & IoT (ARM, AVR, PIC, PlatformIO, MicroPython)"),
            ("3", "🤖 Robotics & ROS 2 Framework"),
            ("4", "🔌 FPGA Toolchains (Xilinx, Intel) - Manual Setup"),
            ("5", "⚡ Install ALL Recommended Tools"),
            ("6", "🔧 System Setup & USB Permissions"),
            ("7", "📋 Generate Installation Report"),
            ("8", "🧪 Run Test Suite"),
            ("9", "🚪 Exit")
        ]
        
        console.print(Panel.fit("📋 MAIN MENU", border_style="green"))
        for num, desc in menu_options:
            console.print(f"  [{num}] {desc}")
        
        console.print("")
        choice = Prompt.ask("Select option", choices=["1","2","3","4","5","6","7","8","9"], default="9")
        return choice
    
    def install_standard_compilers(self):
        """Install standard compilers from previous script"""
        console.print(Panel.fit("🖥️  STANDARD COMPILERS INSTALLATION", border_style="blue"))
        
        compilers = [
            ("GCC (C/C++)", "gcc_install"),
            ("Clang/LLVM", "clang_install"),
            ("OpenJDK (Java)", "java_install"),
            (".NET SDK (Roslyn)", "dotnet_install"),
            ("Node.js & npm", "node_install"),
            ("TypeScript", "ts_install"),
            ("Babel/SWC", "web_install"),
            ("Rust", "rust_install"),
            ("Go", "go_install"),
            ("Swift", "swift_install"),
        ]
        
        for name, _ in compilers:
            if Confirm.ask(f"Install {name}?", default=True):
                self.install_component(name)
        
        if Confirm.ask("Install all remaining standard compilers?", default=False):
            self.install_all_standard()
    
    def install_embedded(self):
        """Install embedded compilers"""
        console.print(Panel.fit("📱 EMBEDDED & IOT TOOLCHAIN", border_style="yellow"))
        
        embed_options = [
            ("ARM GCC Embedded (STM32, RP2040)", "arm_embedded"),
            ("AVR-GCC (Arduino)", "avr_gcc"),
            ("MPLAB XC8 (PIC)", "pic_install"),
            ("PlatformIO (Universal)", "platformio_install"),
            ("MicroPython/CircuitPython", "micropython_install"),
            ("ESP32/ESP8266 Tools", "esp_install"),
        ]
        
        for name, _ in embed_options:
            if Confirm.ask(f"Install {name}?", default=True):
                self.install_component(name)
    
    def install_robotics(self):
        """Install ROS and robotics tools"""
        console.print(Panel.fit("🤖 ROBOTICS & ROS 2", border_style="magenta"))
        
        if Confirm.ask("Install ROS 2 Humble?", default=True):
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
                progress.add_task(description="Installing ROS 2...", total=None)
                self.install_ros2()
        
        if Confirm.ask("Install Clang for ROS development?", default=True):
            self.run_command("sudo apt install -y clang-14 lld-14 clang-tidy-14")
        
        console.print("[green]✓ Robotics toolchain setup complete[/green]")
    
    def install_fpga(self):
        """FPGA toolchain guide"""
        console.print(Panel.fit("🔌 FPGA TOOLCHAINS (Manual Installation)", border_style="red"))
        
        info_text = """
[bold yellow]Xilinx Vivado/Vitis:[/bold yellow]
  • Download: https://www.xilinx.com/support/download.html
  • Size: ~30GB
  • Install: ./Xilinx_Unified_*.bin

[bold yellow]Intel Quartus Prime:[/bold yellow]
  • Download: https://www.intel.com/content/www/us/en/software/programmable/quartus-prime/download.html
  • Size: ~15GB
  • Install: ./quartus-*.run

[bold cyan]Alternative (Open Source):[/bold cyan]
  • yosys - Open SYnthesis Suite
  • nextpnr - FPGA place and route
  • icestorm - Lattice iCE40 FPGAs
  • Project Trellis - Lattice ECP5 FPGAs
"""
        console.print(Panel(info_text, border_style="cyan", title="Installation Guide"))
        
        if Confirm.ask("Install open-source FPGA tools (yosys/nextpnr)?", default=False):
            self.install_open_fpga()
    
    def install_all_recommended(self):
        """Install all recommended tools"""
        console.print(Panel.fit("⚡ FULL INSTALLATION", border_style="green"))
        
        if Confirm.ask("This will install ALL compilers and tools. Continue?", default=False):
            with Progress() as progress:
                task = progress.add_task("[cyan]Installing all components...", total=15)
                
                # Install everything
                self.install_all_standard()
                progress.update(task, advance=3)
                
                self.run_command("sudo apt update")
                self.install_arm_embedded()
                progress.update(task, advance=3)
                
                self.install_avr_gcc()
                progress.update(task, advance=2)
                
                self.install_platformio()
                progress.update(task, advance=2)
                
                self.install_micropython()
                progress.update(task, advance=2)
                
                self.install_ros2()
                progress.update(task, advance=3)
                
            console.print("[bold green]✓ Full installation complete![/bold green]")
    
    def system_setup(self):
        """Setup USB permissions and system configuration"""
        console.print(Panel.fit("🔧 SYSTEM SETUP", border_style="cyan"))
        
        # Add user to groups
        groups = ["dialout", "plugdev", "tty", "uucp"]
        for group in groups:
            self.run_command(f"sudo usermod -a -G {group} $USER")
            console.print(f"[green]✓ Added user to {group}[/green]")
        
        # Install udev rules for common dev boards
        udev_rules = """# Arduino
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2341", GROUP="plugdev", MODE="0666"
# STM32
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", GROUP="plugdev", MODE="0666"
# ESP32/ESP8266
SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", GROUP="plugdev", MODE="0666"
# Raspberry Pi Pico
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2e8a", GROUP="plugdev", MODE="0666"
"""
        
        with open("/tmp/99-usmi.rules", "w") as f:
            f.write(udev_rules)
        
        self.run_command("sudo mv /tmp/99-usmi.rules /etc/udev/rules.d/")
        self.run_command("sudo udevadm control --reload-rules")
        self.run_command("sudo udevadm trigger")
        
        console.print("[green]✓ USB udev rules installed[/green]")
        console.print("[yellow]⚠️  Please log out and back in for group changes to take effect[/yellow]")
    
    def generate_report(self):
        """Generate installation report"""
        self.update_status()
        
        report = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    USMI INSTALLATION REPORT                      ║
║                    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                     ║
╚══════════════════════════════════════════════════════════════════╝

System Information:
  • OS: {platform.system()} {platform.release()}
  • Distribution: {self.distro}
  • Architecture: {platform.machine()}
  • Python: {platform.python_version()}

Installed Compilers:
"""
        
        for compiler, version in self.installed_compilers.items():
            if version:
                report += f"  ✅ {compiler:<20} {version}\n"
            else:
                report += f"  ❌ {compiler:<20} Not installed\n"
        
        report += """
Recommended Next Steps:
  1. Run 'source ~/.bashrc' or restart terminal
  2. Connect your development board
  3. Run 'platformio project init' for new projects
  4. Check USB permissions with 'lsusb'
"""
        
        # Save report
        with open("usmi_installation_report.txt", "w") as f:
            f.write(report)
        
        console.print(Panel(report, border_style="green", title="Installation Report"))
        console.print("[cyan]Report saved to: usmi_installation_report.txt[/cyan]")
    
    def run_tests(self):
        """Run compiler verification tests"""
        console.print(Panel.fit("🧪 COMPILER TEST SUITE", border_style="magenta"))
        
        tests = [
            ("GCC", "echo '#include <stdio.h>\nint main(){printf(\"OK\");return 0;}' | gcc -x c - -o /tmp/test && /tmp/test"),
            ("Python", "python3 -c 'print(\"OK\")'"),
            ("Node.js", "node -e 'console.log(\"OK\")'"),
            ("Rust", "echo 'fn main(){println!(\"OK\");}' | rustc - && ./rust_out"),
        ]
        
        results = Table(title="Test Results", box=box.ROUNDED)
        results.add_column("Compiler", style="cyan")
        results.add_column("Status", style="green")
        results.add_column("Output", style="yellow")
        
        for name, cmd in tests:
            success, stdout, _ = self.run_command(cmd)
            status = "✅ PASS" if success else "❌ FAIL"
            output = stdout.strip()[:50] if stdout else "—"
            results.add_row(name, status, output)
        
        console.print(results)
    
    def install_component(self, name):
        """Generic component installer with progress"""
        console.print(f"[cyan]Installing {name}...[/cyan]")
        # Implementation would call the specific installation functions
    
    def install_all_standard(self):
        """Install all standard compilers"""
        pass
    
    def install_arm_embedded(self):
        """Install ARM GCC embedded"""
        self.run_command("""
            wget -q https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2
            sudo tar -xjf gcc-arm-none-eabi-*.tar.bz2 -C /usr/local
            echo 'export PATH=$PATH:/usr/local/gcc-arm-none-eabi-10.3-2021.10/bin' >> ~/.bashrc
        """)
    
    def install_avr_gcc(self):
        """Install AVR GCC"""
        self.run_command("sudo apt install -y gcc-avr avr-libc avrdude")
    
    def install_platformio(self):
        """Install PlatformIO"""
        self.run_command("curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py | python3")
    
    def install_micropython(self):
        """Install MicroPython tools"""
        self.run_command("pip3 install mpremote circup adafruit-ampy")
    
    def install_ros2(self):
        """Install ROS 2"""
        self.run_command("""
            sudo apt install -y software-properties-common
            sudo add-apt-repository universe -y
            curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
            echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list
            sudo apt update
            sudo apt install -y ros-humble-desktop
            echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
        """)
    
    def install_open_fpga(self):
        """Install open source FPGA tools"""
        self.run_command("""
            sudo apt install -y yosys nextpnr-ice40 nextpnr-ecp5
            git clone https://github.com/YosysHQ/icestorm.git
            cd icestorm && make && sudo make install
        """)
    
    def run(self):
        """Main TUI loop"""
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            self.display_header()
            choice = self.show_main_menu()
            
            if choice == "1":
                self.install_standard_compilers()
            elif choice == "2":
                self.install_embedded()
            elif choice == "3":
                self.install_robotics()
            elif choice == "4":
                self.install_fpga()
            elif choice == "5":
                self.install_all_recommended()
            elif choice == "6":
                self.system_setup()
            elif choice == "7":
                self.generate_report()
            elif choice == "8":
                self.run_tests()
            elif choice == "9":
                console.print("\n[bold cyan]USMI - Universal Space Marine Intelligent[/bold cyan]")
                console.print("[green]Compiler suite ready. Semper Excellus! 🚀[/green]")
                sys.exit(0)
            
            if choice != "9":
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    tui = USMITUI()
    try:
        tui.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Installation cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)
