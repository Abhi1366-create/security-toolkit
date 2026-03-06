import argparse
from scanner.engine import PortScanner
from scanner.validator import validate_target, parse_ports

def main():
    parser = argparse.ArgumentParser(description="Threaded tcp port scanner")

    parser.add_argument("target", help="target ip address")
    parser.add_argument("-p", "--ports", default="1-65535", help="Port range (e.g 1-1000 or 80,443)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    args = parser.parse_args()
    validate_target(args.target)
    ports = parse_ports(args.ports)

    scanner = PortScanner(args.target, ports, args.threads)
    scanner.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
    except Exception as e:
        print(f"Error: {e}")