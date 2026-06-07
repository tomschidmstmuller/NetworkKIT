import os
import socket
import platform
import psutil
from datetime import datetime

USMI_ASCII = r"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
"""

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unknown"

def bytes_to_human(num):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num < 1024:
            return f"{num:.2f} {unit}"
        num /= 1024
    return f"{num:.2f} PB"

def print_dashboard():
    os.system("cls" if os.name == "nt" else "clear")

    print(USMI_ASCII)

    uname = platform.uname()
    net = psutil.net_io_counters()

    print("SYSTEM")
    print("------")
    print(f"Host      : {socket.gethostname()}")
    print(f"OS        : {uname.system} {uname.release}")
    print(f"Kernel    : {uname.version}")
    print(f"Machine   : {uname.machine}")
    print()

    print("NETWORK")
    print("-------")
    print(f"Local IP  : {get_local_ip()}")
    print(f"Sent      : {bytes_to_human(net.bytes_sent)}")
    print(f"Received  : {bytes_to_human(net.bytes_recv)}")
    print()

    print("INTERFACES")
    print("----------")
    for iface, addrs in psutil.net_if_addrs().items():
        print(f"[{iface}]")
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"  IPv4 : {addr.address}")
        print()

    print(f"Updated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    print_dashboard()
