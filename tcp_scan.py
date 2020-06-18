#Import modules
import socket
import pyfiglet
import sys

#Define variables
open_ports = []
exist_ports_open = 0
comands = {"-h", "--help"}
args = sys.argv

#TCP SCANNER banner / authory of </Conection>
main = pyfiglet.figlet_format("TCP SCAN")
print(main, "Developed by: </Conection>")

#Check if arguments/values are correct
try:

    ip = str(args[1])
    start_port = int(args[2])
    end_port = int(args[3])

#Else...
except:

    if len(args) == 1:
        print("\n[ERROR] You put wrong arguments or missing arguments, \"--help\" to help.")
        sys.exit(0)

    if len(args) == 2:
        if args[1] not in comands:
            print("\n[ERROR] You put wrong arguments or missing arguments, \"--help\" to help.")
            sys.exit(0)

#If user type "-h" or "--help" help him ;)
if args[1] == "-h" or args[1] == "--help":
    print("\nUsage: tcp_scan.py <ip> <starting_port> <ending_port>")
    sys.exit(0)

#Define type of conection (IP/TCP) and set the max of time to try
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

#List of ports to scan
for portas in range(int(start_port), int(end_port)):

    #Try to connect
    result = client.connect_ex((ip, portas))

    print(result)
    #If port is open:
    if result == 0:
        print(f"Port {portas} is open! ")
        exist_ports_open = 1
    #Else:
    else:
        pass
client.close()

#If he do not find any open port:
if exist_ports_open == 0:
    print("No ports open! ")
