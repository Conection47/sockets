import socket
import pyfiglet
import sys

open_ports = []
comands = {"-h", "--help"}
args = sys.argv


main = pyfiglet.figlet_format("TCP SCAN")
print(main, "Developed by: </Conection>")

try:

    ip = str(args[1])
    start_port = int(args[2])
    end_port = int(args[3])
    
except:
    if len(args) == 2:
        if args[1] not in comands:
            print("\n[ERROR] You put wrong arguments or missing arguments, \"--help\" to help.")
            sys.exit(0)

if args[1] == "-h" or args[1] == "--help":
    print("\nUsage: tcp_scan.py <ip> <starting_port> <ending_port>")
    sys.exit(0)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.6)

for portas in range(int(start_port), int(end_port)):
    try:
        result = client.connect((ip, portas))
        if result == 0:
            open_ports.append(portas)
    except:
        pass

for show_open_ports in open_ports:
    print(f"The port {show_open_ports} is open! ")

client.close()
