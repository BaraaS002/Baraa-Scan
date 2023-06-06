import socket
import re  
import requests 




def scan_ports(target_host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def validate_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return pattern.match(ip)  


if __name__ == '__main__':
    
    
    
    #######################################################################################
    from termcolor import colored
    from pyfiglet import Figlet

    fig = Figlet(font='slant')
    print(colored(fig.renderText('Baraa Scan'), 'green'))
    print(colored('Create by Eng Baraa Sahmoud', 'red', attrs=['reverse', 'blink']))
    #######################################################################################
    while True:
        print("\nMenu:")
        print("*** Baraa Scan ***")
        print("1. Get localhost")
        print("2. Get the service name for this port")
        print("3. Port scanning")
        print("4. Check if a port is open")
        print("5. Get the IP of this domain")
        print("6. DNS lookup")  
        print("7. IP Locator") 
        print("8. Exit")
        print("*** ☠️ ***")
        choice = input("Enter your choice (1-8): ")

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

            
            if not validate_ip(target_host):
                print("Invalid target host IP address")
                continue

            port = int(input("Enter the port number: "))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
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
            except socket.gaierror:# gaierror: get address info error
                print("Failed to get IP address for the domain")

        elif choice == "6":
            domain = input("Enter the domain name: ")
            try:
                ip_addresses = socket.getaddrinfo(domain, None)
                print(f"IP addresses for domain {domain}:")
                for ip in ip_addresses:
                    print(ip[4][0])
            except socket.gaierror:
                print("Failed to get IP addresses for the domain")

        elif choice == "7":
            ip_address = input("Enter the IP address to locate: ")
            url = f"http://ip-api.com/json/{ip_address}"
            response = requests.get(url)
            data = response.json()
            if data["status"] == "fail":
                print("Failed to locate the IP address")
            else:
                print("IP Locator Results:")
                print(f"IP Address: {data['query']}")
                print(f"Country: {data['country']}")
                print(f"Region: {data['regionName']}")
                print(f"City: {data['city']}")
                print(f"ZIP Code: {data['zip']}")
                print(f"Latitude: {data['lat']}")
                print(f"Longitude: {data['lon']}")
                
        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
