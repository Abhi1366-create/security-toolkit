import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


class PortScanner:
    def __init__(self, target, ports, max_threads=100):
        self.target = target
        self.ports = ports
        self.max_threads = max_threads
        self.open_ports = []

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((self.target, port))

                if result == 0:
                    return port

        except socket.error:
            return None

        return None

    def run(self):
        print(f"Scanning {self.target}... please wait\n")

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:

            futures = [
                executor.submit(self.scan_port, port)
                for port in self.ports
            ]

            for future in as_completed(futures):
                result = future.result()

                if result is not None:
                    self.open_ports.append(result)
                    print(f"[OPEN] Port {result}")

        print("\nScan complete.")

        if self.open_ports:
            print("Open ports:", sorted(self.open_ports))
        else:
            print("No open ports found.")