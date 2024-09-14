import socket

print("""                
                    | |                
  _ __ ___   ___  __| |_   _ ___  __ _ 
 | '_ ` _ \ / _ \/ _` | | | / __|/ _` |
 | | | | | |  __/ (_| | |_| \__ \ (_| |
 |_| |_| |_|\___|\__,_|\__,_|___/\__,_|                                    
                                       
""")
def scan_ports(target, ports):
    """
    Scan the specified ports on the target host.

    :param target: Target hostname or IP address.
    :param ports: List of ports to scan.
    :return: Dictionary with port numbers and their statuses.
    """
    open_ports = {}

    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the connection
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports[port] = 'Open'
            else:
                open_ports[port] = 'Closed'

    return open_ports


def main():
    target = input("Enter the target IP address or hostname: ")
    ports = [22, 80, 443, 8080]  # Example ports to scan

    print(f"Scanning ports on {target}...")
    open_ports = scan_ports(target, ports)

    for port, status in open_ports.items():
        print(f"Port {port}: {status}")


if __name__ == "__main__":
    main()
