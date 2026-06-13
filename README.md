
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT

================================================================================
                        NETWORKKIT — PROJECT OVERVIEW
================================================================================
  A comprehensive penetration testing toolkit, system administration suite,
  and developer environment manager. Originally forked from PenTestKit,
  extended with custom USMI tools, monitoring dashboards, compiler managers,
  and homelab utilities.

  Repository : github.com/larvenejafemcoder/NetworkKIT
  License    : GNU General Public License
================================================================================

TABLE OF CONTENTS
--------------------------------------------------------------------------------
  1.  PROJECT STRUCTURE
  2.  CORE MODULES (PenTestKit Fork)
  3.  CUSTOM USMI TOOLS
  4.  VISUAL & ANIMATION
  5.  DEVELOPER ENVIRONMENT
  6.  DOTFILES
  7.  QUICK-START CHEAT SHEET
  8.  DEPENDENCIES
  9.  ARCHITECTURE DIAGRAMS


================================================================================
1. PROJECT STRUCTURE
================================================================================

  NetworkKIT/
  ├── ad/                 Active Directory attack references
  ├── applocker/          AppLocker bypass detection
  ├── auditing/           Docker Bench security parser
  ├── auditor/            *** Custom USMI Network Security Auditor
  ├── automation/         Automated nmap scanning
  ├── compiler/           *** Custom USMI Compiler Manager TUI
  ├── cracking/           Brute-force scripts (SSH, FTP, SMTP, RDP, Oracle)
  ├── dev-installer-tui/  *** Custom Dev Installer TUI (Textual)
  ├── donut/              *** Custom 3D ASCII donut animations
  ├── enumeration/        Enumeration wordlists
  ├── firewall/           Subnet & country extraction
  ├── generate-scripts-lists/  Nmap scan script generators
  ├── grep/               Log/report parsing pipelines
  ├── ldap/               LDAP enumeration (enum4linux, ldapsearch)
  ├── live-hosts/         Live host discovery (27 techniques)
  ├── m365/               Microsoft 365 user generation
  ├── maps/               *** Custom ASCII map installer
  ├── metasploit/         Metasploit reference notes
  ├── misc/               Miscellaneous utilities & cheat sheets
  ├── mobile/             Mobile app pentesting notes
  ├── nessus/             Nessus results processing
  ├── oracle/             Oracle DB assessment scripts
  ├── phishing/           Domain phishing detection (dnstwist)
  ├── port-scanning/      TCP/UDP port scanning (57 scripts)
  ├── reconnaissance/     DNS, WHOIS, Shodan, web recon
  ├── sip/                SIP/VoIP assessment
  ├── skid/               External IP range scanning
  ├── smb/                SMB enumeration & exploitation
  ├── smtp/               SMTP user enumeration
  ├── snmp/               SNMP discovery & scanning
  ├── sqli/               SQL injection references
  ├── ssl/                SSL/TLS scanning
  ├── usmi/               *** Custom USMI server monitoring suite
  ├── web/                Web app assessment (55 tools)
  ├── wifi/               WiFi pentesting notes
  ├── windows/            Windows remote execution notes
  ├── .dotfiles/          System dotfiles (zsh, kitty, neofetch, etc.)
  └── README.md           This file

  *** = Custom USMI additions (not part of the original PenTestKit fork)


================================================================================
2. CORE MODULES (PenTestKit Original)
================================================================================

  RECONNAISSANCE (16 tools)
  ──────────────────────────────────────────────────────────────────────────────
  ip.sh / ips.sh         Resolve IP addresses
  whois.sh               WHOIS lookups
  hostname.sh            Hostname resolution
  mx.sh / ns.sh          Mail exchange & nameserver records
  zone-transfer.sh       DNS zone transfer attempts
  ftp-banner.sh          Banner grab FTP servers
  smtp-banner.sh         Banner grab SMTP servers
  webrecon.sh            Automated web recon
  web-reconnaissance.py  Python web reconnaissance
  shodan/                Shodan API integration (shodanhat)

  LIVE HOST DISCOVERY (27 scripts)
  ──────────────────────────────────────────────────────────────────────────────
  discover-live-hosts-icmp-echo.sh       ICMP echo discovery
  discover-live-hosts-syn.sh             SYN scan discovery
  discover-live-hosts-ack.sh             ACK scan discovery
  discover-live-hosts-udp.sh             UDP discovery
  discover-live-hosts-sctp.sh            SCTP protocol discovery
  discover-live-hosts-timestamp.sh       Timestamp request discovery
  discover-live-hosts-protocol-ping.sh   Protocol ping discovery
  discover-live-hosts-oses.sh            OS fingerprint discovery
  discover-local-live-hosts-arpscan.sh   ARP scan (local subnet)
  discover-local-live-hosts-netbios.sh   NetBIOS discovery
  discover-local-live-hosts-netdiscover.sh  Passive network discovery
  discover-local-live-hosts-passively-p0f.sh  Passive OS fingerprinting (p0f)
  ping.sh / ping-from-linux.sh           Standard ping utilities

  PORT SCANNING (57 scripts)
  ──────────────────────────────────────────────────────────────────────────────
  tcp/                    TCP port scanning (full, services, stealth variants)
    tcp-ports-scan-*.sh           Various TCP scan profiles
    full/                          Full TCP port scans
    services/                      Service-specific TCP scans
  udp/                    UDP port scanning (full, services)
    udp-ports-scan-*.sh           Various UDP scan profiles
    full/                          Full UDP port scans
    services/                      Service-specific UDP scans

  CRACKING (19 scripts)
  ──────────────────────────────────────────────────────────────────────────────
  brute-force-ssh-hydra.sh / brute-force-ssh-medusa.sh    SSH brute-force
  brute-force-ftp-hydra.sh / brute-force-ftp-medusa.sh    FTP brute-force
  brute-force-smtp-hydra.sh / brute-force-smtp-medusa.sh  SMTP brute-force
  brute-force-rdp-hydra.sh    RDP brute-force
  oracle-login.sh             Oracle login brute-force
  open-relay-smtp.sh          SMTP open relay testing
  smtp-users-enumeration.sh   SMTP user enumeration
  crunch-charset.sh / crunch-pattern.sh   Password generation
  generate-wordlist.sh / generate-wordlist-from-site.sh    Wordlist creation
  create-password-list-from-rockyou-with-policy.sh         Policy-filtered lists

  WEB ASSESSMENT (55 tools)
  ──────────────────────────────────────────────────────────────────────────────
  dir-scanner-*.sh                    Directory brute-force (dirsearch, ffuf,
                                      gobuster, fine-tuned, proxy variants)
  nikto-scan*.sh                      Nikto web scanner (4 variants)
  nuclei-scan.sh                      Nuclei template scanner
  banner-grabbing-*.sh                Banner grabbing (curl, nc, nmap, wget)
  curl-*.sh                           HTTP method testing (get, post, put, del,
                                      options, trace, robots, proxy)
  robots.sh / robots-ssl.sh           robots.txt analysis
  web-headers-*.sh                    Header manipulation tests (null, malformed)
  wordpress-scan.sh                   WordPress enumeration
  eyewitness.sh / screenshot.sh       Web screenshotting
  check-urls.py                       URL verification
  check-unauthenticated-access.py     Access control testing
  content-type-checker.py             Content-type validation
  compare-post-data.py                POST data comparison
  extract-urls.py                     URL extraction
  headers-checker.py                  Security header audit
  web-app-framework.sh                Framework fingerprinting
  js-map-decoder/                     JavaScript source map decoder
  lists/                              Wordlists (big.list, content-types)

  SERVICE ENUMERATION
  ──────────────────────────────────────────────────────────────────────────────
  smb/          SMB enumeration (null-session, enum4linux, nbtscan, shares)
  snmp/         SNMP discovery, scanning, walking (community.lst)
  ldap/         LDAP scanning (enum4linux, ldapsearch)
  smtp/         SMTP user enumeration
  sip/          SIP/VoIP scanning (svwar, dos)
  ssl/          SSL/TLS scanning (ssl-scan.sh, tlssled.sh)
  oracle/       Oracle DB assessment (ODAT wrappers)
  nessus/       Nessus report processing & grouping

  INFRASTRUCTURE & MISC
  ──────────────────────────────────────────────────────────────────────────────
  live-hosts/     Host discovery (27 scripts)
  firewall/       Subnet analysis, country extraction
  automation/     Automated nmap scanning (nmap_auto.sh)
  generate-scripts-lists/  Nmap scan list generators
  grep/           Results parsing & CSV/Excel formatting (19 scripts)
  metasploit/     Payload, binding, multi-handler notes
  sqli/           SQL injection references (mssql, sqlmap)
  misc/           Cheat sheets (helpful-commands, port-forwarding, socat,
                  ssh, stunnel, openvas, top ports)


================================================================================
3. CUSTOM USMI TOOLS
================================================================================

  USMI Server Monitor (usmi/)
  ──────────────────────────────────────────────────────────────────────────────
  network_spy.py       Basic network dashboard:
                       - System info (host, OS, kernel, machine)
                       - Local IP detection
                       - Network traffic totals (sent/received)
                       - Interface listing with IPv4 addresses
                       Usage: python3 usmi/network_spy.py

  mission_control.py   Live-updating Rich dashboard:
                       - CPU, RAM, Disk progress bars
                       - Real-time upload/download speeds
                       - Top 10 processes by memory
                       - Color-coded ASCII header
                       Usage: python3 usmi/mission_control.py

  server_monitor.py    Advanced live server monitor:
                       - Progress bars with percentage
                       - Drive temperature (smartctl, Linux)
                       - Top 15 processes (CPU% + RAM MB)
                       - Self-updating every 0.5s
                       Usage: python3 usmi/server_monitor.py

  Network Security Auditor (auditor/)
  ──────────────────────────────────────────────────────────────────────────────
  network_auditor.py   Multi-function security audit tool:
                       - Network range port scanning (threaded)
                       - Service banner grabbing
                       - SSL certificate inspection
                       - DNS enumeration (dig)
                       - Web security header analysis
                       - Directory listing detection
                       - FTP anon login testing
                       - Report generation (text file)
                       Usage:
                         python3 auditor/network_auditor.py                  # interactive
                         python3 auditor/network_auditor.py -m scan -t 192.168.1.0/24

  Web Scraping (web/)
  ──────────────────────────────────────────────────────────────────────────────
  webscraper.py        Lightweight web scraper:
                       - Single page scrape
                       - Website crawling (depth/pages/rate limits)
                       - Product scraping (CSS selectors)
                       - Export: txt, csv, json
                       Usage:
                         python3 web/webscraper.py -u https://example.com -m crawl -d 2 -p 50

  db_scraper.py        Database web scraper:
                       - CSS selector scraping with pagination
                       - HTML table extraction
                       - REST API endpoint scraping
                       - JSON file loading
                       - Export: Excel, SQLite, MongoDB, PostgreSQL, MySQL, JSON
                       Usage:
                         python3 web/db_scraper.py -u https://example.com -m table -o sqlite

  ASCII Map (maps/)
  ──────────────────────────────────────────────────────────────────────────────
  ascii-map.sh         Interactive ASCII map installer for Ubuntu:
                       - mapscii (terminal world map)
                       - ttymap (interactive console map)
                       - ascii-map (simple ASCII viewer)
                       Usage: bash maps/ascii-map.sh

  Delete the empty dirs by removing them:
  Delete-Item -Path ".dotfiles\gnominise", ".dotfiles\Tahoe-icons" -Force

  ──────────────────────────────────────────────────────────────────────────────
  Donut (donut/)
  ──────────────────────────────────────────────────────────────────────────────
  donut.py             Classic 3D rotating donut (Pygame):
                       - Full-screen 1920x1080 rendering
                       - HSV color cycling
                       - Based on Andy Sloane's donut.c
                       Usage: python3 donut/donut.py

  donut_chorus.py      Terminal multi-donut animation:
                       - 8 simultaneous rotating donuts
                       - Each with independent bobbing motion
                       - Random color shimmer per frame
                       - Pure ANSI (no external deps)
                       Usage: python3 donut/donut_chorus.py


================================================================================
4. DEVELOPER ENVIRONMENT
================================================================================

  Compiler Manager TUI (compiler/)
  ──────────────────────────────────────────────────────────────────────────────
  compiler_manager.py  Rich-powered TUI for toolchain installation:
                       - Standard compilers: GCC, Clang, Java, .NET,
                         Node.js, TypeScript, Rust, Go, Swift
                       - Embedded: ARM GCC, AVR-GCC, PlatformIO,
                         MicroPython, ESP32 tools
                       - Robotics: ROS 2 Humble (auto-install)
                       - FPGA: Xilinx/Intel guide + open-source tools
                       - USB udev rules for dev boards
                       - Installation report generation
                       - Compiler verification test suite
                       Usage: python3 compiler/compiler_manager.py
                       Requires: Linux (Ubuntu/Debian/Arch)

  Dev Installer TUI (dev-installer-tui/)
  ──────────────────────────────────────────────────────────────────────────────
  Textual-based package installer:
                       - 7 categories, 30+ development tools
                       - Multi-package manager support:
                         - Debian/Ubuntu: nala, apt
                         - Arch Linux: pacman, yay (AUR)
                       - Checkbox selection UI
                       - Real-time installation output
                       - System update functionality
                       Usage:
                         pip install -r dev-installer-tui/requirements.txt
                         python3 dev-installer-tui/main.py
                       Requires: Linux, Textual


================================================================================
5. SYSTEM DOTFILES
================================================================================

  Location: .dotfiles/
  ──────────────────────────────────────────────────────────────────────────────
  Shell:
    .dotfiles/config.fish               Fish shell config
    .dotfiles/zsh/                       ZSH config, aliases, .zshrc, .bashrc

  Terminal Emulators:
    .dotfiles/alacritty/                 Alacritty config (dank-theme, nordic,
                                         keybinds)
    .dotfiles/kitty/                     Kitty config (dank-theme, tabs)

  Themes:
    .dotfiles/tahoe-theme/               GTK theme (Tahoe-Light, Tahoe-Dark)
                                         with gtk-3.0, gtk-4.0 styling
    .dotfiles/gnome-terminal/            GNOME Terminal dconf settings

  System Info:
    .dotfiles/neofetch/                  Neofetch config, ASCII art (pfp.jpg)
    .dotfiles/fastfetch/                 Fastfetch JSON config

  Tools:
    .dotfiles/starship/                  Starship prompt installer
    .dotfiles/fonts/                     Font installer script
    .dotfiles/install.sh                 Master dotfiles installer


================================================================================
6. QUICK-START CHEAT SHEET
================================================================================

  TARGET                      COMMAND
  ──────────────────────────────────────────────────────────────────────────────
  USMI dashboard              python3 usmi/network_spy.py
  USMI live monitor           python3 usmi/server_monitor.py
  Audit local network         python3 auditor/network_auditor.py -m scan -t 192.168.1.0/24
  SSL check                   python3 auditor/network_auditor.py -m ssl -t example.com
  DNS recon                   python3 auditor/network_auditor.py -m dns -t example.com
  Web security check          python3 auditor/network_auditor.py -m web -t https://example.com
  Scrape website              python3 web/webscraper.py -u https://example.com -m single
  Crawl website               python3 web/webscraper.py -u https://example.com -m crawl -d 3 -p 100
  Export table to SQLite      python3 web/db_scraper.py -u https://example.com -m table -o sqlite
  Compiler manager            python3 compiler/compiler_manager.py
  Dev installer TUI           python3 dev-installer-tui/main.py
  Donut (Pygame)              python3 donut/donut.py
  Donut chorus (terminal)     python3 donut/donut_chorus.py
  ASCII map                   bash maps/ascii-map.sh
  Dotfiles install            bash .dotfiles/install.sh
  nmap auto                   bash automation/nmap_auto.sh


================================================================================
7. DEPENDENCIES
================================================================================

  REQUIRED (most modules)
  ──────────────────────────────────────────────────────────────────────────────
  Python 3.8+
  nmap
  whois, dig, nslookup

  PYTHON PACKAGES
  ──────────────────────────────────────────────────────────────────────────────
  psutil                  usmi/, auditor/          System/network stats
  rich                    usmi/, compiler/         Terminal UI, formatting
  textual                 dev-installer-tui/       TUI framework
  requests                web/, auditor/           HTTP client
  beautifulsoup4          web/                     HTML parsing
  pandas, openpyxl        web/db_scraper.py        Excel export
  pymongo                 web/db_scraper.py        MongoDB export
  psycopg2-binary         web/db_scraper.py        PostgreSQL export
  mysql-connector-python  web/db_scraper.py        MySQL export
  pygame                  donut/donut.py           3D rendering

  SYSTEM TOOLS
  ──────────────────────────────────────────────────────────────────────────────
  smartmontools           Drive temperature (server_monitor.py)
  dig                     DNS enumeration (auditor)
  nala                    Faster apt wrapper (dev-installer-tui)

  Install all Python deps:
    pip install psutil rich textual requests beautifulsoup4 pandas openpyxl
    pip install pymongo psycopg2-binary mysql-connector-python pygame


================================================================================
9. ARCHITECTURE DIAGRAMS
================================================================================

  The following Mermaid diagrams describe the project architecture, tool
  workflows, and component relationships. Render them at:
    https://mermaid.live/
  Or with: npx @mermaid-js/mermaid-cli -i diagrams.md -o output.png

  ──────────────────────────────────────────────────────────────────────────────
  9.1  ARCHITECTURE — Complete Project Structure
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  graph TB
      subgraph "NetworkKIT"
          NK["NetworkKIT<br/>No Built-in Database"]

          subgraph "Original PenTestKit Modules"
              RECON["Reconnaissance<br/>16 tools<br/>whois, dig, shodan"]
              LIVE["Live Host Discovery<br/>27 scripts<br/>ICMP, TCP, UDP, ARP"]
              PORT["Port Scanning<br/>57 scripts<br/>TCP Full/Services/Stealth<br/>UDP Full/Services"]
              CRACK["Cracking<br/>19 scripts<br/>Hydra, Medusa, Crunch"]
              WEB["Web Assessment<br/>55 tools<br/>Nikto, Nuclei, Gobuster"]
              SVC["Service Enum<br/>SMB, SNMP, LDAP,<br/>SMTP, SIP, SSL, Oracle"]
          end

          subgraph "Custom USMI Additions"
              USMI_MON["Server Monitor<br/>network_spy.py<br/>mission_control.py<br/>server_monitor.py"]
              AUDITOR["Network Auditor<br/>network_auditor.py<br/>Port scan + SSL + DNS + Web"]
              SCRAPER["Web Scrapers<br/>webscraper.py<br/>db_scraper.py"]
              DONUT["Donut Animations<br/>donut.py (Pygame)<br/>donut_chorus.py (ANSI)"]
              MAPS["ASCII Maps<br/>ascii-map.sh"]
          end

          subgraph "Dev Environment"
              COMPILER["Compiler Manager<br/>compiler_manager.py<br/>GCC, Clang, Java, Rust, Go..."]
              DEVINST["Dev Installer TUI<br/>dev-installer-tui/main.py<br/>Textual UI, 30+ tools"]
          end

          subgraph "Dotfiles"
              DOTFILES[".dotfiles/<br/>zsh, kitty, alacritty,<br/>neofetch, fastfetch,<br/>tahoe-theme GTK"]
          end

          USMI_MON --> |psutil, rich| SYSTEM[System Sources<br/>CPU, RAM, Disk, Net]
          AUDITOR --> |socket, ssl, requests| NET[Network Targets]
          SCRAPER --> EXPORT[Export Destinations]
      end

      subgraph "Optional External Destinations"
          EXCEL[Excel Files]
          SQLITE[(SQLite)]
          EXTDB[(External DBs<br/>PostgreSQL / MySQL / MongoDB<br/>User Must Install)]
      end

      EXPORT --> EXCEL
      EXPORT --> SQLITE
      EXPORT --> EXTDB

      style NK fill:#1a1a1a,stroke:#ef4444,stroke-width:3px
      style RECON fill:#1e3a5f,stroke:#3b82f6
      style LIVE fill:#1e3a5f,stroke:#3b82f6
      style PORT fill:#1e3a5f,stroke:#3b82f6
      style CRACK fill:#1e3a5f,stroke:#3b82f6
      style WEB fill:#1e3a5f,stroke:#3b82f6
      style SVC fill:#1e3a5f,stroke:#3b82f6
      style USMI_MON fill:#5b1a1a,stroke:#ef4444
      style AUDITOR fill:#5b1a1a,stroke:#ef4444
      style SCRAPER fill:#5b1a1a,stroke:#ef4444
      style DONUT fill:#5b1a1a,stroke:#ef4444
      style MAPS fill:#5b1a1a,stroke:#ef4444
      style COMPILER fill:#1a3d1a,stroke:#22c55e
      style DEVINST fill:#1a3d1a,stroke:#22c55e
      style EXTDB fill:#336791,stroke:#00aaff,stroke-dasharray: 5 5
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.2  USMI DATAFLOW — Monitoring Pipeline
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  flowchart LR
      subgraph "System Sources"
          CPU["/proc/stat<br/>CPU Percent"]
          RAM["/proc/meminfo<br/>Memory Usage"]
          DISK["/proc/diskstats<br/>Disk Usage"]
          NET["/proc/net/dev<br/>Network Counters"]
          PROCS["/proc/[PID]/<br/>Process Stats"]
          UPTIME["/proc/uptime<br/>Boot Time"]
          SMART["smartctl<br/>Drive Temp (Linux)"]
      end

      subgraph "USMI Collection Layer"
          PS_PSUTIL["psutil<br/>Cross-platform<br/>system/network API"]
          SUBPROC["subprocess<br/>smartctl calls"]
      end

      subgraph "USMI Tools"
          NS["network_spy.py<br/>Static Dashboard<br/>One-shot display"]
          MC["mission_control.py<br/>Live Dashboard<br/>1s refresh"]
          SM["server_monitor.py<br/>Live Dashboard<br/>0.5s refresh"]
      end

      subgraph "Output"
          RICH["rich Library<br/>Progress Bars, Tables,<br/>Panels, Layouts"]
          TTY["TTY Output<br/>ANSI colors<br/>CLI display"]
      end

      CPU --> PS_PSUTIL
      RAM --> PS_PSUTIL
      DISK --> PS_PSUTIL
      NET --> PS_PSUTIL
      PROCS --> PS_PSUTIL
      UPTIME --> PS_PSUTIL
      SMART --> SUBPROC

      PS_PSUTIL --> NS
      PS_PSUTIL --> MC
      PS_PSUTIL --> SM
      SUBPROC --> SM

      NS --> RICH
      MC --> RICH
      SM --> RICH
      RICH --> TTY

      style NS fill:#5b1a1a,stroke:#ef4444
      style MC fill:#5b1a1a,stroke:#f97316
      style SM fill:#5b1a1a,stroke:#eab308
      style RICH fill:#1e3a5f,stroke:#3b82f6
      style CPU fill:#1a1a1a,stroke:#6b7280
      style RAM fill:#1a1a1a,stroke:#6b7280
      style DISK fill:#1a1a1a,stroke:#6b7280
      style NET fill:#1a1a1a,stroke:#6b7280
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.3  AUDITOR SEQUENCE — Security Audit Workflow
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  sequenceDiagram
      actor User
      participant AU as network_auditor.py
      participant PS as Port Scanner
      participant BG as Banner Grabber
      participant SSL as SSL Checker
      participant DNS as DNS Enumerator
      participant WEB as Web Checker
      participant FILE as Report Export

      User->>AU: Launch (interactive/CLI)

      rect rgb(30, 58, 95)
          Note over PS,WEB: Port Scan Phase
          AU->>PS: scan_network_range(cidr, ports)
          PS->>PS: Ping sweep for active hosts
          PS->>PS: Threaded port connect scan
          PS->>BG: get_service_banner(ip, port)
          BG->>BG: Protocol-specific probes<br/>(HELP, HEAD, SSH banner)
          BG-->>PS: Service fingerprint
          PS-->>AU: Open ports + banners
      end

      rect rgb(91, 26, 26)
          Note over SSL,DNS: Analysis Phase
          AU->>SSL: check_ssl_certificate(domain)
          SSL->>SSL: SSL handshake, cert inspection
          SSL-->>AU: Subject, issuer, expiry, SAN
          AU->>DNS: dns_enumeration(domain)
          DNS->>DNS: dig A, AAAA, MX, NS, TXT, CNAME
          DNS->>DNS: Subdomain brute-force
          DNS-->>AU: DNS records
          AU->>WEB: web_security_check(url)
          WEB->>WEB: Header audit, directory listing
          WEB-->>AU: Security findings
      end

      rect rgb(26, 61, 26)
          Note over FILE: Report Phase
          User->>AU: Generate Report
          AU->>FILE: Write report file
          FILE-->>User: security_audit_report.txt
      end
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.4  COMPILER TUI — Toolchain Manager Structure
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  graph TB
      subgraph "compiler_manager.py<br/>USMITUI Class"
          START["Launch TUI"] --> HEADER["Display USMI Header<br/>+ Press Enter to continue"]
          HEADER --> MENU["Main Menu<br/>9 Options"]

          MENU --> OPT1["1. Standard Compilers<br/>GCC, Clang, Java, .NET<br/>Node, TS, Rust, Go, Swift"]
          MENU --> OPT2["2. Embedded & IoT<br/>ARM GCC, AVR-GCC<br/>PlatformIO, MicroPython, ESP32"]
          MENU --> OPT3["3. Robotics<br/>ROS 2 Humble<br/>Clang for ROS"]
          MENU --> OPT4["4. FPGA Toolchains<br/>Xilinx/Intel guides<br/>Open-source (yosys)"]
          MENU --> OPT5["5. Install ALL<br/>Full automation<br/>15 components"]
          MENU --> OPT6["6. System Setup<br/>USB udev rules<br/>User groups"]
          MENU --> OPT7["7. Generate Report<br/>Status summary<br/>Save to file"]
          MENU --> OPT8["8. Run Tests<br/>GCC, Python,<br/>Node, Rust verify"]
          MENU --> OPT9["9. Exit"]
      end

      subgraph "Detection Layer"
          DISTRO["Distro Detection<br/>/etc/os-release"]
          STATUS["Status Checks<br/>gcc --version<br/>java --version<br/>rustc --version<br/>..."]
      end

      subgraph "Installation Backend"
          APT["sudo apt install -y"]
          WGET["wget + tar -xjf"]
          CURL["curl | python3"]
          GIT["git clone + make"]
      end

      DISTRO --> MENU
      STATUS --> MENU
      OPT1 --> APT
      OPT2 --> WGET
      OPT2 --> CURL
      OPT3 --> APT
      OPT5 --> APT
      OPT5 --> WGET
      OPT5 --> CURL
      OPT6 --> APT

      style START fill:#1a3d1a,stroke:#22c55e
      style MENU fill:#1e3a5f,stroke:#3b82f6
      style OPT1 fill:#5b1a1a,stroke:#ef4444
      style OPT2 fill:#5b1a1a,stroke:#ef4444
      style OPT3 fill:#5b1a1a,stroke:#ef4444
      style OPT4 fill:#5b1a1a,stroke:#ef4444
      style OPT5 fill:#854d0e,stroke:#eab308
      style OPT6 fill:#1e3a5f,stroke:#3b82f6
      style OPT7 fill:#1e3a5f,stroke:#3b82f6
      style OPT8 fill:#1e3a5f,stroke:#3b82f6
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.5  DEVINSTALLER STATE — Package Installer States
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  stateDiagram-v2
      [*] --> DistroDetection
      DistroDetection --> Ready: Distro Identified<br/>(Debian / Arch)

      Ready --> CategoryBrowse: Select Category
      Ready --> SystemUpdate: Press Update

      CategoryBrowse --> PackageSelect: View Packages
      PackageSelect --> PackageSelect: Toggle Checkbox

      PackageSelect --> ConfirmInstall: Press Install
      ConfirmInstall --> Installing: Confirm
      ConfirmInstall --> PackageSelect: Cancel

      Installing --> ProgressOutput: Real-time output
      ProgressOutput --> PackageSelect: Success
      ProgressOutput --> PackageSelect: Partial Failure
      ProgressOutput --> PackageSelect: Error

      SystemUpdate --> ProgressOutput: apt update / pacman -Sy
      SystemUpdate --> Ready: Complete

      state DistroDetection {
          [*] --> CheckOSRelease
          CheckOSRelease --> Debian: ID=ubuntu/debian
          CheckOSRelease --> Arch: ID=arch
          CheckOSRelease --> NalaCheck: Detected Debian
          NalaCheck --> HasNala: nala installed
          NalaCheck --> NoNala: nala not installed
      }

      state PackageSelect {
          [*] --> SelectCategory
          SelectCategory --> CodeEditors
          SelectCategory --> VersionControl
          SelectCategory --> ProgLanguages
          SelectCategory --> BuildTools
          SelectCategory --> Containers
          SelectCategory --> Databases
          SelectCategory --> PackageMgrs
      }
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.6  PORTSCAN HIERARCHY — 57 Scanning Scripts
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  graph TB
      subgraph "Port Scanning (57 scripts)"
          TCP["TCP Scanning"] --> TCP_FULL["TCP Full Scans<br/>8 scripts<br/>common, all, fast<br/>service, version, OS"]
          TCP --> TCP_SRV["TCP Service Scans<br/>4 scripts<br/>srv, srv-common<br/>srv-all, srv-fast"]
          TCP --> TCP_STEALTH["TCP Stealth Variants<br/>ports-scan-*.sh<br/>13 scripts<br/>stealth, paranoid,<br/>delay, nc, netcat"]

          UDP["UDP Scanning"] --> UDP_FULL["UDP Full Scans<br/>6 scripts<br/>common, all, fast<br/>service, version"]
          UDP --> UDP_SRV["UDP Service Scans<br/>5 scripts<br/>srv, srv-common<br/>srv-all, srv-fast"]
          UDP --> UDP_STEALTH["UDP Stealth Variants<br/>ports-scan-*.sh<br/>9 scripts"]
      end

      subgraph "Scan Profiles"
          PROFILES["Profile Suffixes"] --> FAST["-fast<br/>Quick top ports"]
          PROFILES --> COMMON["-common<br/>Most frequent"]
          PROFILES --> STEALTH["-stealth<br/>Slow, undetected"]
          PROFILES --> PARANOID["-paranoid<br/>Extremely slow"]
          PROFILES --> ALL["-all<br/>65535 ports"]
          PROFILES --> NOPING["-noping-nodns<br/>No pre-discovery"]
          PROFILES --> RATELIMIT["-ratelimited<br/>Throttled output"]
      end

      TCP_STEALTH --> PROFILES
      UDP_STEALTH --> PROFILES
      TCP_FULL --> PROFILES
      UDP_FULL --> PROFILES

      style TCP fill:#1e3a5f,stroke:#3b82f6
      style TCP_FULL fill:#5b1a1a,stroke:#ef4444
      style TCP_SRV fill:#5b1a1a,stroke:#ef4444
      style TCP_STEALTH fill:#854d0e,stroke:#eab308
      style UDP fill:#1e3a5f,stroke:#3b82f6
      style UDP_FULL fill:#5b1a1a,stroke:#ef4444
      style UDP_SRV fill:#5b1a1a,stroke:#ef4444
      style UDP_STEALTH fill:#854d0e,stroke:#eab308
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.7  LIVEHOST MINDMAP — 27 Discovery Techniques
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  mindmap
    root((Live Host Discovery<br/>27 Techniques))
      ICMP
        ICMP Echo
        ICMP Timestamp
        ICMP Address Mask
        ICMP Protocol Ping
      TCP
        SYN Scan
        ACK Scan
        TCP Null
        TCP FIN
        TCP Xmas
      UDP
        UDP Scan
      ARP
        ARP Scan
        ARP Local Subnet
      SCTP
        SCTP Discovery
      Application
        NetBIOS
        mDNS
        SMB Discovery
      Passive
        p0f (Passive OS)
        netdiscover
        Packet Sniffing
      Protocol
        Protocol Ping
        Remote OS Detect
      Efficiency
        Top100 Quick
        List-based Batch
        IP Range Subnet
        Debug Mode
        All Methods
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.8  WEB TOOLMAP — 55 Web Assessment Tools
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  mindmap
    root((Web Assessment<br/>55 Tools))
      Directory Scanning
        dirsearch
        ffuf
        gobuster
        Fine-tuning
        Proxy
      Vulnerability Scanners
        Nikto - Standard
        Nikto - User Agent
        Nikto - Proxy
        Nikto - UA+Proxy
        Nuclei Scan
      Banner Grabbing
        curl HTTP
        curl HTTP Proxy
        nc
        nc HTTP
        nmap Script
        nmap Built-in
        wget HTTP
      HTTP Methods
        GET
        POST
        PUT
        DELETE
        OPTIONS
        TRACE
        Robots
      WordPress
        Wordpress Scan
      Screenshots
        EyeWitness
        Screenshot.sh
        HTML to PNG
      Web App Detection
        Framework Detect
        App Recon
        Content Type Check
      Code Analysis
        JS Map Decoder
        Extract URLs
        Compare POST Data
        Headers Checker
        Access Check
        URL Check
      Wordlists
        big.list
        Common Content Types
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.9  CRACKING FLOW — Brute-Force Pipeline
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  flowchart TB
      subgraph "Service Discovery"
          RECON["Reconnaissance<br/>Identify open ports"]
          RECON --> SVC["Service Identification<br/>SSH:22, FTP:21, SMTP:25<br/>RDP:3389, Oracle:1521"]
      end

      subgraph "Tool Selection"
          SVC --> CHOOSE["Choose Tool"]
          CHOOSE --> HYDRA["Hydra<br/>Multi Protocol<br/>Fast, Parallel"]
          CHOOSE --> MEDUSA["Medusa<br/>Parallel Attempts<br/>Modular Design"]
      end

      subgraph "Wordlist Generation"
          WL["Generate Wordlists"] --> CRUNCH["crunch<br/>Custom patterns"]
          WL --> ROCKYOU["rockyou filter<br/>Policy-based<br/>Length, charset"]
          WL --> SITE["Generate from Site<br/>Scrape keywords"]
      end

      subgraph "Execution"
          HYDRA --> EXEC["Brute Force<br/>Hydra/Medusa"]
          MEDUSA --> EXEC
          CRUNCH --> EXEC
          ROCKYOU --> EXEC
          SITE --> EXEC

          EXEC --> RESULT{"Result"}
          RESULT -->|Success| REPORT["Log Credentials<br/>Save to report"]
          RESULT -->|Failure| RETRY["Retry with<br/>Options/Usernames"]
          RESULT -->|Blocked| DELAY["Increase delay<br/>Reduce rate"]
      end

      subgraph "Special Cases"
          ORACLE["Oracle Login<br/>ODAT wrappers<br/>SID guessing"]
          SMTPS["SMTP<br/>User Enumeration<br/>Open Relay Check"]
          ANON["Anonymous FTP<br/>Check for<br/>public access"]
      end

      EXEC --> ORACLE
      EXEC --> SMTPS
      EXEC --> ANON

      style RECON fill:#1e3a5f,stroke:#3b82f6
      style HYDRA fill:#5b1a1a,stroke:#ef4444
      style MEDUSA fill:#5b1a1a,stroke:#ef4444
      style CRUNCH fill:#854d0e,stroke:#eab308
      style ROCKYOU fill:#854d0e,stroke:#eab308
      style EXEC fill:#5b1a1a,stroke:#ef4444
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.10  DONUT COMPARISON — Visual Tool Comparison
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  flowchart LR
      subgraph "donut.py"
          PYGAME["Pygame Engine<br/>1920x1080 Fullscreen"]
          GPU["GPU Accelerated<br/>HW Surface Rendering"]
          HSV["HSV Color Cycling<br/>hue += 0.005"]
          CHARS["Chars: .,-~:;=!*#$@"]
          CONTROL["Controls:<br/>ESC to exit"]
      end

      subgraph "donut_chorus.py"
          ANSI["Pure ANSI Terminal<br/>80x24 Buffer"]
          NODEPS["No Dependencies<br/>Python stdlib only"]
          MULTI["8 Simultaneous Donuts<br/>Each with:<br/>- Independent rotation<br/>- Bobbing motion<br/>- Random shimmer"]
          FPS["~20 FPS<br/>time.sleep(0.05)"]
          COLOR["Random ANSI Colors<br/>31-36, 91-96"]
      end

      subgraph "Comparison"
          COMPARE1["Resolution<br/>Pygame: 1920x1080<br/>Chorus: 80x24 chars"]
          COMPARE2["Performance<br/>Pygame: GPU accelerated<br/>Chorus: CPU rendering"]
          COMPARE3["Portability<br/>Pygame: Requires pygame<br/>Chorus: Any terminal"]
          COMPARE4["Visuals<br/>Pygame: Single, smooth<br/>Chorus: 8, chaotic"]
      end

      PYGAME --> COMPARE1
      PYGAME --> COMPARE2
      ANSI --> COMPARE1
      ANSI --> COMPARE2
      HSV --> COMPARE4
      MULTI --> COMPARE4

      style PYGAME fill:#5b1a1a,stroke:#ef4444
      style GPU fill:#1e3a5f,stroke:#3b82f6
      style HSV fill:#854d0e,stroke:#eab308
      style ANSI fill:#1a3d1a,stroke:#22c55e
      style MULTI fill:#5b1a1a,stroke:#ef4444
  ```

  ──────────────────────────────────────────────────────────────────────────────
  9.11  QUICK REFERENCE — Decision Tree
  ──────────────────────────────────────────────────────────────────────────────

  ```mermaid
  flowchart TB
      USER["What do you want to do?"]

      USER -->|"Monitor<br/>system health"| MON["USMI Monitor"]
      MON --> MON1["Static snapshot?"]
      MON --> MON2["Live dashboard?"]
      MON1 -->|"Yes"| NS["python3 usmi/network_spy.py"]
      MON2 -->|"Basic live"| MC["python3 usmi/mission_control.py"]
      MON2 -->|"With drive temp"| SM["python3 usmi/server_monitor.py"]

      USER -->|"Security<br/>audit"| AUDIT["Network Auditor"]
      AUDIT --> AUD1["Full interactive?"]
      AUDIT --> AUD2["Quick scan?"]
      AUDIT --> AUD3["SSL check?"]
      AUDIT --> AUD4["DNS recon?"]
      AUDIT --> AUD5["Web check?"]
      AUD1 -->|"Menu-driven"| AU1["python3 auditor/network_auditor.py<br/>Choose option 1-5"]
      AUD2 -->|"CIDR range"| AU2["python3 auditor/network_auditor.py<br/>-m scan -t 192.168.1.0/24"]
      AUD3 -->|"Domain"| AU3["python3 auditor/network_auditor.py<br/>-m ssl -t example.com"]
      AUD4 -->|"Domain"| AU4["python3 auditor/network_auditor.py<br/>-m dns -t example.com"]
      AUD5 -->|"URL"| AU5["python3 auditor/network_auditor.py<br/>-m web -t https://example.com"]

      USER -->|"Network<br/>scanning"| SCAN["PenTestKit Scans"]
      SCAN --> SC1["Live hosts?"]
      SCAN --> SC2["Port scanning?"]
      SCAN --> SC3["Web recon?"]
      SCAN --> SC4["Cracking?"]
      SC1 -->|"27 methods"| LS["bash live-hosts/discover-live-hosts-*.sh"]
      SC2 -->|"57 scripts"| PS["bash port-scanning/tcp/tcp-ports-scan-*.sh"]
      SC3 -->|"55 tools"| WS["bash web/dir-scanner-*.sh<br/>bash web/nikto-scan.sh"]
      SC4 -->|"19 scripts"| CS["bash cracking/brute-force-*-hydra.sh"]

      USER -->|"Install dev<br/>tools"| DEV["Dev Environment"]
      DEV --> DV1["Compiler manager?"]
      DEV --> DV2["Package installer?"]
      DV1 -->|"Rich TUI"| CMP["python3 compiler/compiler_manager.py"]
      DV2 -->|"Textual TUI"| DVT["python3 dev-installer-tui/main.py"]

      USER -->|"Visual<br/>effects"| VFX["Donut Animations"]
      VFX --> VF1["Fullscreen Pygame?"]
      VFX --> VF2["Terminal-based?"]
      VF1 -->|"1920x1080"| DN1["python3 donut/donut.py"]
      VF2 -->|"8 donuts"| DN2["python3 donut/donut_chorus.py"]

      USER -->|"Setup<br/>environment"| ENV["Environment Setup"]
      ENV --> EV1["Dotfiles?"]
      ENV --> EV2["ASCII map?"]
      ENV --> EV3["Scrape data?"]
      EV1 -->|"All dotfiles"| DF["bash .dotfiles/install.sh"]
      EV2 -->|"World map"| MP["bash maps/ascii-map.sh"]
      EV3 -->|"Website"| SCR["python3 web/webscraper.py -u URL -m single"]
      EV3 -->|"To database"| DBS["python3 web/db_scraper.py -u URL -o sqlite"]

      style USER fill:#1a1a1a,stroke:#ef4444,stroke-width:3px
      style MON fill:#5b1a1a,stroke:#ef4444
      style AUDIT fill:#5b1a1a,stroke:#ef4444
      style SCAN fill:#1e3a5f,stroke:#3b82f6
      style DEV fill:#1a3d1a,stroke:#22c55e
      style VFX fill:#854d0e,stroke:#eab308
      style ENV fill:#1e3a5f,stroke:#3b82f6
  ```


================================================================================
                          END OF PROJECT OVERVIEW
================================================================================
  "Universal Space Marine Intelligent — Semper Excellus"
