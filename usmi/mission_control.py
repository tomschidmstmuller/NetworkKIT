import socket
import time
from datetime import timedelta

import psutil
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

console = Console()


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unknown"


def bytes_fmt(n):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def progress_bar(percent, width=20):
    filled = int(percent / 100 * width)
    return "█" * filled + "░" * (width - filled)


last = psutil.net_io_counters()
last_time = time.time()


def build_dashboard():
    global last, last_time

    layout = Layout()

    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    now = time.time()
    net = psutil.net_io_counters()

    dt = max(now - last_time, 0.001)

    up_speed = (net.bytes_sent - last.bytes_sent) / dt
    down_speed = (net.bytes_recv - last.bytes_recv) / dt

    last = net
    last_time = now

    info = Table(show_header=False)
    info.add_row("Hostname", socket.gethostname())
    info.add_row("IP", get_ip())
    info.add_row("CPU", f"{cpu}%")
    info.add_row("RAM", f"{ram.percent}%")
    info.add_row("Disk", f"{disk.percent}%")
    info.add_row("Uptime", str(timedelta(seconds=int(time.time() - psutil.boot_time()))))

    status = f"""
CPU   [{progress_bar(cpu)}] {cpu:.1f}%
RAM   [{progress_bar(ram.percent)}] {ram.percent:.1f}%
DISK  [{progress_bar(disk.percent)}] {disk.percent:.1f}%

UPLOAD   {bytes_fmt(up_speed)}/s
DOWNLOAD {bytes_fmt(down_speed)}/s
"""

    proc_table = Table(title="Top Processes")
    proc_table.add_column("PID")
    proc_table.add_column("Process")
    proc_table.add_column("Memory MB")

    procs = []

    for p in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            mem = p.info["memory_info"].rss / 1024 / 1024
            procs.append((p.info["pid"], p.info["name"], mem))
        except:
            pass

    procs.sort(key=lambda x: x[2], reverse=True)

    for pid, name, mem in procs[:10]:
        proc_table.add_row(str(pid), str(name), f"{mem:.1f}")

    title = Panel.fit(
        """
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
""",
        title="USMI Mission Control"
    )

    layout.split_column(
        Layout(title, size=10),
        Layout(Panel(info, title="System Info"), size=10),
        Layout(Panel(status, title="Resource Monitor"), size=10),
        Layout(proc_table)
    )

    return layout


if __name__ == "__main__":
    with Live(build_dashboard(), refresh_per_second=1, screen=True) as live:
        while True:
            live.update(build_dashboard())
            time.sleep(1)
