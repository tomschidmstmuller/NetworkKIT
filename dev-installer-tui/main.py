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

Dev Installer TUI - Terminal UI for installing development tools
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import Header, Footer, Button, Static, DataTable, LoadingIndicator, Label, Checkbox
from textual.screen import Screen
from textual import events
from rich.text import Text
from rich.style import Style
from textual.reactive import reactive
from textual.message import Message
import asyncio

from config import PACKAGES
from installer import PackageInstaller

class ProgressScreen(Screen):
    """Screen showing installation progress"""
    
    def compose(self):
        yield Container(
            Label("Installation Progress", id="progress-title"),
            ScrollableContainer(
                Static(id="progress-output"),
                id="progress-scroll"
            ),
            LoadingIndicator(),
            Button("Back to Main", variant="default", id="back-btn"),
            id="progress-container"
        )
    
    def on_mount(self):
        self.query_one("#progress-output").update("Starting installation...\n")
    
    def append_output(self, text: str):
        current = self.query_one("#progress-output").renderable
        self.query_one("#progress-output").update(f"{current}{text}\n")
        scroll_container = self.query_one("#progress-scroll")
        scroll_container.scroll_end(animate=False)
    
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back-btn":
            self.app.pop_screen()

class InstallerApp(App):
    CSS = """
    Screen {
        background: #1a1b26;
    }
    
    #main-container {
        padding: 1;
        height: 100%;
    }
    
    #category-list {
        height: 100%;
        border: solid $primary;
        margin: 0 1;
    }
    
    #package-list {
        height: 100%;
        border: solid $primary;
        margin: 0 1;
    }
    
    #status-bar {
        height: 3;
        background: $surface;
        margin: 1;
        padding: 0 1;
    }
    
    #install-btn {
        background: $success;
        width: 20;
        margin: 1;
    }
    
    #update-btn {
        background: $warning;
        width: 20;
        margin: 1;
    }
    
    #refresh-btn {
        background: $primary;
        width: 20;
        margin: 1;
    }
    
    .category-button {
        width: 100%;
        margin: 0;
        padding: 1;
    }
    
    .package-checkbox {
        width: 100%;
        padding: 0 1;
    }
    
    .category-header {
        background: $primary;
        text-style: bold;
        padding: 1;
        margin: 0;
    }
    
    .installed {
        color: $success;
        text-style: bold;
    }
    
    .not-installed {
        color: $warning;
    }
    
    #progress-container {
        height: 100%;
        padding: 1;
    }
    
    #progress-title {
        text-style: bold;
        content-align: center middle;
        height: 3;
    }
    
    #progress-output {
        height: 100%;
        background: $panel;
        padding: 1;
    }
    
    #progress-scroll {
        height: 85%;
        border: solid $primary;
    }
    
    Button {
        margin: 0 1;
    }
    """
    
    def compose(self):
        self.installer = PackageInstaller()
        self.selected_packages = set()
        
        yield Header()
        
        with Container(id="main-container"):
            with Horizontal():
                with Vertical(id="category-list"):
                    yield Static("Categories", classes="category-header")
                    self.category_buttons = []
                    for category in PACKAGES.keys():
                        btn = Button(category, variant="default", 
                                   classes="category-button")
                        self.category_buttons.append(btn)
                        yield btn
                
                with ScrollableContainer(id="package-list"):
                    self.package_container = Vertical()
                    yield self.package_container
            
            with Horizontal(id="status-bar"):
                yield Static("Status: Ready", id="status")
                yield Static(f"Distro: {self.installer.distro}", id="distro")
                if self.installer.has_nala:
                    yield Static("Using nala (faster apt)", id="nala-status")
            
            with Horizontal():
                yield Button("Update System", variant="warning", id="update-btn")
                yield Button("Install Selected", variant="success", id="install-btn")
                yield Button("Refresh Status", variant="primary", id="refresh-btn")
        
        yield Footer()
    
    def on_mount(self):
        self.show_packages(list(PACKAGES.keys())[0])
        self.update_package_statuses()
    
    def show_packages(self, category: str):
        self.package_container.remove_children()
        packages = PACKAGES.get(category, {})
        
        available_managers = self.installer.get_available_package_managers()
        
        for pkg_name, managers in packages.items():
            selected_manager = None
            for mgr in available_managers:
                if mgr in managers:
                    selected_manager = mgr
                    break
            
            if selected_manager:
                pkg_id = f"{pkg_name}_{selected_manager}"
                checkbox = Checkbox(pkg_name, value=pkg_id in self.selected_packages,
                                  classes="package-checkbox")
                checkbox.package_info = {
                    'name': pkg_name,
                    'manager': selected_manager,
                    'package': managers[selected_manager]
                }
                self.package_container.mount(checkbox)
    
    def update_package_statuses(self):
        pass
    
    def on_checkbox_changed(self, event: Checkbox.Changed):
        checkbox = event.checkbox
        pkg_info = getattr(checkbox, 'package_info', None)
        
        if pkg_info:
            pkg_id = f"{pkg_info['name']}_{pkg_info['manager']}"
            if event.value:
                self.selected_packages.add(pkg_id)
            else:
                self.selected_packages.discard(pkg_id)
        
        self.query_one("#status").update(f"Selected {len(self.selected_packages)} packages")
    
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "update-btn":
            self.run_update()
        elif event.button.id == "install-btn":
            self.run_installation()
        elif event.button.id == "refresh-btn":
            self.refresh_status()
        else:
            category = event.button.label
            if category in PACKAGES:
                self.show_packages(category)
    
    def run_update(self):
        async def update():
            progress_screen = ProgressScreen()
            await self.push_screen(progress_screen)
            
            def callback(text):
                progress_screen.append_output(text)
            
            progress_screen.append_output("Updating package lists...")
            success = self.installer.update_system(callback)
            
            if success:
                progress_screen.append_output("\n[SUCCESS] System updated successfully!")
            else:
                progress_screen.append_output("\n[ERROR] Update failed!")
        
        asyncio.create_task(update())
    
    def run_installation(self):
        if not self.selected_packages:
            self.query_one("#status").update("No packages selected!")
            return
        
        async def install():
            progress_screen = ProgressScreen()
            await self.push_screen(progress_screen)
            
            def callback(text):
                progress_screen.append_output(text)
            
            progress_screen.append_output(f"Installing {len(self.selected_packages)} packages...\n")
            
            for pkg_id in self.selected_packages:
                parts = pkg_id.rsplit('_', 1)
                if len(parts) != 2:
                    continue
                
                pkg_name = parts[0]
                manager = parts[1]
                
                found = False
                for category in PACKAGES.values():
                    if pkg_name in category and manager in category[pkg_name]:
                        actual_pkg = category[pkg_name][manager]
                        found = True
                        break
                
                if found:
                    progress_screen.append_output(f"\n--- Installing {pkg_name} ---")
                    success = self.installer.install_package(actual_pkg, manager, callback)
                    if success:
                        progress_screen.append_output(f"✓ {pkg_name} installed successfully!")
                    else:
                        progress_screen.append_output(f"✗ Failed to install {pkg_name}")
            
            progress_screen.append_output("\n[COMPLETE] Installation finished!")
        
        asyncio.create_task(install())
    
    def refresh_status(self):
        self.query_one("#status").update("Status: Checking packages...")
        self.update_package_statuses()
        self.query_one("#status").update(f"Status: Ready - {len(self.selected_packages)} selected")

def main():
    app = InstallerApp()
    app.run()

if __name__ == "__main__":
    main()
