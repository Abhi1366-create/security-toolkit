import ipaddress
def validate_target(target):
    try:
        ipaddress.ip_address(target)
    except ValueError:
        raise ValueError("Invalid target ip address format")
    
def parse_ports(port_string):
    
    if "-" in port_string:
        start, end = map(int, port_string.split("-"))
        return range(start, end +1)
    
    return [int(p.strip()) for p in port_string.split(",")]
