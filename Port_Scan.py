import socket

target_ip = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

def scan_ports(ip, start, end):
    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

scan_ports(target_ip, start_port, end_port)
