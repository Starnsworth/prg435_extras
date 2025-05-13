# Ping a port range on an IP.
# Program to ping a port to see if it is open.
import socket
ports = [8432,50, 80,8080, 995, 420, 5515]
hostname= "localhost"

def checkPortState(ports,hostname):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"{port} : {s.connect_ex((hostname, port)) == 0}")

# returns true if port in use. false if port not in use.
print("Port : State")
checkPortState(ports,hostname)