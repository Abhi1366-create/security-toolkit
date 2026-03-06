import socket

services = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS"
}

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect((ip, port))

        if port == 80:
            s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

        response = s.recv(1024).decode(errors="ignore")

        banner = response.split("\n")[0]

        service = services.get(port, "Unknown")

        print(f"[+] {port} OPEN | {service} | {banner.strip()}")

        s.close()

    except:
        print(f"[-] {port} CLOSED")


def main():
    target = input("Target IP: ")

    ports = [21, 22, 25, 80, 443]

    print(f"\nScanning {target}...\n")

    for port in ports:
        grab_banner(target, port)


if __name__ == "__main__":
    main()