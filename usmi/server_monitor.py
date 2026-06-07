import os
import re
import socket
import platform
import subprocess
import time
from datetime import timedelta

import psutil
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

console = Console()

prev_net = psutil.net_io_counters()
prev_time = time.time()


def human(n):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}PB"


def bar(percent, width=24):
    filled = int(percent / 100 * width)
    return "█" * filled + "░" * (width - filled)


def get_drive_temp(device=None):
    if os.name == "nt":
        return None

    if device is None:
        for candidate in ["/dev/nvme0n1", "/dev/sda", "/dev/sdb"]:
            t = get_drive_temp(candidate)
            if t is not None:
                return t
        return None

    try:
        result = subprocess.run(
            ["smartctl", "-A", device],
            capture_output=True,
            text=True
        )

        output = result.stdout

        match = re.search(
            r"Temperature_Celsius.*?(\d+)$",
            output,
            re.MULTILINE
        )

        if match:
            return int(match.group(1))

        match = re.search(
            r"Temperature:\s+(\d+)",
            output
        )

        if match:
            return int(match.group(1))

        return None

    except Exception:
        return None


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("1.1.1.1", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unknown"


ASCII = r"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
"""


def dashboard():
    global prev_net, prev_time

    layout = Layout()

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    now = time.time()
    net = psutil.net_io_counters()

    delta = max(now - prev_time, 0.001)

    up = (net.bytes_sent - prev_net.bytes_sent) / delta
    down = (net.bytes_recv - prev_net.bytes_recv) / delta

    prev_net = net
    prev_time = now

    sysinfo = Table(show_header=False)
    sysinfo.add_row("Host", socket.gethostname())
    sysinfo.add_row("OS", f"{platform.system()} {platform.release()}")
    sysinfo.add_row("Kernel", platform.version())
    sysinfo.add_row("IP", get_ip())
    sysinfo.add_row(
        "Uptime",
        str(timedelta(seconds=int(time.time() - psutil.boot_time())))
    )

    usage = Table(show_header=False)
    usage.add_row("CPU ", f"{bar(cpu)} {cpu:.1f}%")
    usage.add_row("RAM ", f"{bar(ram.percent)} {ram.percent:.1f}%")
    temp = get_drive_temp()
    temp_str = f"{temp}°C" if temp else "N/A"
    usage.add_row("Disk", f"{bar(disk.percent)} {disk.percent:.1f}%  {temp_str}")
    usage.add_row("Up", f"{human(up)}/s")
    usage.add_row("Down", f"{human(down)}/s")

    proc_table = Table(title="Top Processes")
    proc_table.add_column("PID")
    proc_table.add_column("Process")
    proc_table.add_column("CPU%")
    proc_table.add_column("RAM MB")

    procs = []

    for p in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_info"]
    ):
        try:
            procs.append(
                (
                    p.info["pid"],
                    p.info["name"],
                    p.info["cpu_percent"],
                    p.info["memory_info"].rss / 1024 / 1024,
                )
            )
        except Exception:
            pass

    procs.sort(key=lambda x: x[3], reverse=True)

    for pid, name, cpu_p, mem in procs[:15]:
        proc_table.add_row(
            str(pid),
            str(name)[:30],
            str(cpu_p),
            f"{mem:.1f}",
        )

    layout.split_column(
        Layout(Panel(ASCII, title="USMI")),
        Layout(
            Panel.fit(sysinfo, title="Neofetch"),
            size=10,
        ),
        Layout(
            Panel.fit(usage, title="Resources"),
            size=10,
        ),
        Layout(proc_table),
    )

    return layout


with Live(
    dashboard(),
    refresh_per_second=2,
    screen=True,
) as live:
    while True:
        live.update(dashboard())
        time.sleep(0.5)
