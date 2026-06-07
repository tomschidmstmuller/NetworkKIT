#!/usr/bin/env python3
"""
Network Security Auditor - Educational Tool
FOR USE ONLY ON NETWORKS YOU OWN OR HAVE WRITTEN PERMISSION TO TEST
"""

import socket
import subprocess
import threading
import time
import sys
import argparse
from datetime import datetime
import ipaddress
import ssl
import requests
from urllib.parse import urlparse

class NetworkAuditor:
    def __init__(self):
        self.results = []
        self.lock = threading.Lock()
        self.banner = """
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
        """
        
    def log_result(self, message):
        """Thread-safe logging"""
        with self.lock:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {message}")
            self.results.append(message)
    
    def scan_port(self, ip, port, timeout=1):
        """Scan a single port to check if it's open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            
            if result == 0:
                # Try to get service banner
                service = self.get_service_banner(ip, port)
                self.log_result(f"🔓 PORT OPEN: {ip}:{port} - {service}")
                return True
            return False
        except:
            return False
    
    def get_service_banner(self, ip, port, timeout=3):
        """Attempt to grab service banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((ip, port))
            
            # Send generic probe for some services
            probes = {
                21: "HELP\r\n",      # FTP
                22: "SSH-2.0-Test\r\n",  # SSH
                25: "HELO test\r\n", # SMTP
                80: "HEAD / HTTP/1.0\r\n\r\n",  # HTTP
                443: "",  # HTTPS will use SSL
                3306: "",  # MySQL
                5432: "",  # PostgreSQL
            }
            
            banner = ""
            if port in probes and probes[port]:
                sock.send(probes[port].encode())
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            elif port == 443:
                # Try SSL connection
                context = ssl.create_default_context()
                ssl_sock = context.wrap_socket(sock, server_hostname=ip)
                banner = ssl_sock.version() if hasattr(ssl_sock, 'version') else "SSL/TLS"
            else:
                # Try generic banner grab
                sock.send(b"\r\n")
                banner = sock.recv(256).decode('utf-8', errors='ignore').strip()
            
            sock.close()
            return banner[:100] if banner else "Unknown service"
        except:
            return "Service detected but banner unavailable"
    
    def scan_network_range(self, network_cidr, ports_to_scan=None):
        """Scan a network range for open ports"""
        if ports_to_scan is None:
            ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 5432, 8080, 8443]
        
        try:
            network = ipaddress.ip_network(network_cidr, strict=False)
            self.log_result(f"🔍 Scanning network: {network_cidr}")
            self.log_result(f"🎯 Target ports: {ports_to_scan}")
            
            active_hosts = []
            
            # First, find active hosts with ping
            for ip in network.hosts():
                if self.ping_host(str(ip)):
                    active_hosts.append(str(ip))
            
            if not active_hosts:
                self.log_result("⚠️ No active hosts found")
                return
            
            self.log_result(f"✅ Found {len(active_hosts)} active hosts")
            
            # Scan ports on active hosts
            threads = []
            for target_ip in active_hosts:
                self.log_result(f"📡 Scanning {target_ip}...")
                for port in ports_to_scan:
                    thread = threading.Thread(target=self.scan_port, args=(target_ip, port))
                    thread.start()
                    threads.append(thread)
                    
                    # Rate limiting
                    if len(threads) >= 50:
                        for t in threads:
                            t.join()
                        threads = []
            
            # Wait for remaining threads
            for t in threads:
                t.join()
                
        except Exception as e:
            self.log_result(f"❌ Error scanning network: {e}")
    
    def ping_host(self, ip):
        """Check if host is reachable"""
        try:
            output = subprocess.run(
                ['ping', '-c', '1', '-W', '1', ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return output.returncode == 0
        except:
            return False
    
    def check_ssl_certificate(self, domain, port=443):
        """Check SSL certificate information"""
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    self.log_result(f"🔐 SSL Certificate for {domain}:")
                    self.log_result(f"   - Subject: {cert.get('subject', 'N/A')}")
                    self.log_result(f"   - Issuer: {cert.get('issuer', 'N/A')}")
                    self.log_result(f"   - Expires: {cert.get('notAfter', 'N/A')}")
                    self.log_result(f"   - SAN: {cert.get('subjectAltName', 'N/A')}")
                    
                    # Check if expired
                    from datetime import datetime
                    expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    if expiry < datetime.now():
                        self.log_result(f"   ⚠️ CERTIFICATE EXPIRED!")
                    return cert
        except Exception as e:
            self.log_result(f"❌ SSL check failed for {domain}: {e}")
            return None
    
    def check_common_vulnerabilities(self, ip, port):
        """Check for common misconfigurations"""
        vulnerabilities = []
        
        # Check for open MySQL with default credentials
        if port == 3306:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((ip, port))
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                if 'mysql' in banner.lower():
                    vulnerabilities.append("MySQL detected - check for default credentials")
                sock.close()
            except:
                pass
        
        # Check for open FTP anonymous access
        if port == 21:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((ip, port))
                sock.send(b"USER anonymous\r\n")
                response = sock.recv(256).decode('utf-8', errors='ignore')
                if '230' in response:  # Login successful
                    vulnerabilities.append("FTP anonymous login allowed!")
                sock.close()
            except:
                pass
        
        return vulnerabilities
    
    def dns_enumeration(self, domain):
        """Perform basic DNS enumeration"""
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
        
        self.log_result(f"🌐 DNS Enumeration for {domain}")
        
        for record in record_types:
            try:
                result = subprocess.run(
                    ['dig', '+short', domain, record],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout.strip():
                    self.log_result(f"   {record} records: {result.stdout.strip()}")
            except:
                pass
        
        # Check for subdomains (basic)
        common_subdomains = ['www', 'mail', 'ftp', 'blog', 'shop', 'api', 'admin', 'test']
        self.log_result(f"   Checking common subdomains...")
        
        for sub in common_subdomains:
            test_domain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(test_domain)
                self.log_result(f"   ✅ Found: {test_domain}")
            except:
                pass
    
    def web_security_check(self, url):
        """Basic web security checks"""
        try:
            self.log_result(f"🌍 Web security check for {url}")
            
            # Check headers
            response = requests.get(url, timeout=10, verify=False)
            headers = response.headers
            
            security_headers = {
                'Strict-Transport-Security': 'HSTS',
                'Content-Security-Policy': 'CSP',
                'X-Frame-Options': 'Clickjacking protection',
                'X-Content-Type-Options': 'MIME sniffing protection',
                'X-XSS-Protection': 'XSS protection'
            }
            
            for header, description in security_headers.items():
                if header in headers:
                    self.log_result(f"   ✅ {description} present")
                else:
                    self.log_result(f"   ⚠️ Missing {description}")
            
            # Check server info
            if 'Server' in headers:
                self.log_result(f"   ℹ️ Server: {headers['Server']}")
            
            # Check for directory listing
            test_paths = ['/', '/admin', '/backup', '/.git', '/config']
            for path in test_paths:
                try:
                    test_url = url.rstrip('/') + path
                    resp = requests.get(test_url, timeout=5, verify=False)
                    if resp.status_code == 200 and ('Index of' in resp.text or 'Directory listing' in resp.text):
                        self.log_result(f"   ⚠️ Directory listing enabled: {test_url}")
                except:
                    pass
                    
        except Exception as e:
            self.log_result(f"❌ Web check failed: {e}")
    
    def generate_report(self, filename="security_audit_report.txt"):
        """Generate a report of findings"""
        with open(filename, 'w') as f:
            f.write("NETWORK SECURITY AUDIT REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now()}\n\n")
            f.write("FINDINGS:\n")
            f.write("-" * 30 + "\n")
            for result in self.results:
                f.write(result + "\n")
            f.write("\n" + "=" * 50 + "\n")
            f.write("RECOMMENDATIONS:\n")
            f.write("1. Close unnecessary open ports\n")
            f.write("2. Update all software to latest versions\n")
            f.write("3. Enable all security headers for web services\n")
            f.write("4. Use strong authentication (no default credentials)\n")
            f.write("5. Implement proper firewall rules\n")
            f.write("6. Regular security audits and penetration testing\n")
            f.write("7. Keep all systems patched and updated\n")
        
        self.log_result(f"📄 Report saved to {filename}")
    
    def run_interactive(self):
        """Interactive mode"""
        print(self.banner)
        print("\n⚠️  LEGAL WARNING: Only use this tool on networks you own")
        print("   or have explicit written permission to test!\n")
        
        while True:
            print("\n" + "="*50)
            print("AUDITOR MENU:")
            print("1. Scan network range")
            print("2. Check SSL certificate")
            print("3. DNS enumeration")
            print("4. Web security check")
            print("5. Generate report")
            print("6. Exit")
            
            choice = input("\nSelect option (1-6): ").strip()
            
            if choice == '1':
                network = input("Enter network CIDR (e.g., 192.168.1.0/24): ")
                ports = input("Enter ports (comma-separated, or press Enter for defaults): ")
                if ports:
                    ports_list = [int(p.strip()) for p in ports.split(',')]
                else:
                    ports_list = None
                self.scan_network_range(network, ports_list)
                
            elif choice == '2':
                domain = input("Enter domain or IP: ")
                port = input("Enter port (default 443): ") or "443"
                self.check_ssl_certificate(domain, int(port))
                
            elif choice == '3':
                domain = input("Enter domain: ")
                self.dns_enumeration(domain)
                
            elif choice == '4':
                url = input("Enter URL (e.g., https://example.com): ")
                self.web_security_check(url)
                
            elif choice == '5':
                self.generate_report()
                
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice")

def main():
    parser = argparse.ArgumentParser(description="Network Security Auditor - For authorized use only")
    parser.add_argument("-m", "--mode", choices=["interactive", "scan", "ssl", "dns", "web"], 
                       default="interactive", help="Operation mode")
    parser.add_argument("-t", "--target", help="Target IP, domain, or network")
    parser.add_argument("-p", "--ports", help="Ports to scan (comma-separated)")
    
    args = parser.parse_args()
    
    auditor = NetworkAuditor()
    print(auditor.banner)
    
    if args.mode == "interactive":
        auditor.run_interactive()
    elif args.mode == "scan" and args.target:
        ports = [int(p.strip()) for p in args.ports.split(',')] if args.ports else None
        auditor.scan_network_range(args.target, ports)
    elif args.mode == "ssl" and args.target:
        auditor.check_ssl_certificate(args.target)
    elif args.mode == "dns" and args.target:
        auditor.dns_enumeration(args.target)
    elif args.mode == "web" and args.target:
        auditor.web_security_check(args.target)
    else:
        print("Error: Target required for non-interactive mode")
        parser.print_help()

if __name__ == "__main__":
    main()
