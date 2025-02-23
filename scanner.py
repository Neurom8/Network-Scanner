import nmap

def scan_ports(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024', '-sV')  # Scan ports 1-1024
    for host in scanner.all_hosts():
        print(f"\n[+] Target: {host}")
        for proto in scanner[host].all_protocols():
            print(f"  Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"  Port {port}: {scanner[host][proto][port]['state']} ({scanner[host][proto][port]['name']})")

target_ip = input("Enter target IP or domain: ")
scan_ports(target_ip)
