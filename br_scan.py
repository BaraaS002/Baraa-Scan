import socket
import re # use to validate IP address format and get the ip of this domain

# Function to scan ports
def scan_ports(target_host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout value for the connection

        # Attempt to connect to the port
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

# Function to validate IP address format
def validate_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return pattern.match(ip)

if __name__ == '__main__':




    from termcolor import colored
    from pyfiglet import Figlet

    fig = Figlet(font='slant')

    print(colored(fig.renderText('Baraa Scan'), 'green'))

    from termcolor import colored
    print(colored('Create by Eng Baraa Sahmoud', 'red', attrs=['reverse', 'blink']))


    while True:
        print("\nMenu:")
        print("*** Baraa Scan ***")
        print("1. Get localhost")  # Get the local host name
        print("2. Get the service name for this port")# Get the service name for a port
        print("3. Port scanning")
        print("4. Check if a port is open")
        print("5. Get the ip of this domain")
        print("6. Exit")
        print("*** ☠️ ***")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hostname = socket.gethostname()
            print("Local Hostname:", hostname)

        elif choice == "2":
            port = int(input("Enter the port number: "))
            try:
                service = socket.getservbyport(port)
                print(f"Service name for port {port}: {service}")
            except OSError:
                print("Error retrieving service name")




        elif choice == "3":
            target_host = input("Enter the target IP address or hostname: ")

            # Validate IP address
            if not validate_ip(target_host):
                print("Invalid target host IP address")
                continue

            start_port = int(input("Enter the starting port: "))
            end_port = int(input("Enter the ending port: "))

            open_ports = scan_ports(target_host, start_port, end_port)
            if open_ports:
                print("Open ports:")
                for port in open_ports:
                    print(port)
            else:
                print("No open ports found")

        elif choice == "4":
            target_host = input("Enter the target IP address or hostname: ")

            # Validate IP address
            if not validate_ip(target_host):
                print("Invalid target host IP address")
                continue

            port = int(input("Enter the port number: "))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout value for the connection

            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")

            sock.close()
        elif choice == "5":
            domain = input("Enter the domain name: ")
            try:
                ip_address = socket.gethostbyname(domain)
                print(f"IP address for domain {domain}: {ip_address}")
            except socket.gaierror:
                print("Failed to get IP address for the domain")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
