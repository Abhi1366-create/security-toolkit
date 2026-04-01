import nmap
import socket

#  Risk scoring map
risk_map = {
    "ssh": "Medium",
    "http": "Low",
    "https": "Low",
    "ftp": "High",
    "telnet": "High",
    "smtp": "Medium",
    "dns": "Low",
    "smb": "High",
    "rdp": "High",
    "mysql": "High"
}

print("=== Advanced Network Scanner ===")

target = input("Enter IP or domain: ")

#  Resolve domain → IP
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target")
    exit()

print(f"\nTarget: {target} ({target_ip})")

print("\nSelect Scan Mode:")
print("1. Stealth (Low Noise)")
print("2. Standard")
print("3. Service Detection")
print("4. Aggressive")
print("5. Extreme ( Loud)")

choice = input("Enter choice (1-5): ")

#  Scan modes
if choice == "1":
    scan_args = "-sT -T2"  # quiet, slower
elif choice == "2":
    scan_args = "-sT -T4"
elif choice == "3":
    scan_args = "-sV -T4"
elif choice == "4":
    scan_args = "-A -T4"
elif choice == "5":
    scan_args = "-A -T5 -p- --script vuln"
else:
    print("Invalid choice, defaulting to aggressive")
    scan_args = "-A -T4"

print(f"\nRunning scan: {scan_args}\n")

scanner = nmap.PortScanner()

#  Run scan
scanner.scan(target_ip, arguments=scan_args)

#  No hosts found
if not scanner.all_hosts():
    print("No hosts found / scan blocked.")
    exit()

#  Output
for host in scanner.all_hosts():
    print(f"\nHost: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        print(f"\nProtocol: {proto}")

        ports = sorted(scanner[host][proto].keys())

        for port in ports:
            port_data = scanner[host][proto][port]

            service = port_data.get('name', 'unknown')
            product = port_data.get('product', '')
            version = port_data.get('version', '')

            #  Risk scoring
            risk = risk_map.get(service.lower(), "Unknown")

            print(f"[OPEN] Port {port} | {service} {product} {version} | Risk: {risk}")

print("\n=== Scan Complete ===")