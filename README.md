# Baraa-Scan Tool
By Eng Baraa Sahmoud 
Baraa Scan is a versatile network scanning tool designed to help you perform various network-related tasks such as port scanning, DNS lookup, IP location, and more. This tool is built using Python and leverages libraries like `socket`, `requests`, `re`, `termcolor`, and `pyfiglet` to provide a user-friendly interface for network analysis.

## Features

1. **Get Localhost**: Retrieves the local hostname of the machine.
2. **Get Service Name for a Port**: Finds the service name associated with a specific port.
3. **Port Scanning**: Scans a range of ports on a target host to identify open ports.
4. **Check if a Port is Open**: Checks if a specific port on a target host is open.
5. **Get IP of a Domain**: Resolves the IP address of a given domain name.
6. **DNS Lookup**: Performs a DNS lookup to retrieve all IP addresses associated with a domain.
7. **IP Locator**: Provides geographical information (country, region, city, etc.) for a given IP address.
8. **Exit**: Exits the tool.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/baraa-scan.git
 
   ```
   ```bash
   cd baraa-scan
   ```
2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Then, install the required Python packages:
   ```bash
   pip install termcolor pyfiglet requests
   ```

3. **Run the Tool**:
   ```bash
   python baraa_scan.py
   ```

## Usage

1. **Get Localhost**:
   - Select option `1` from the menu to display the local hostname.

2. **Get Service Name for a Port**:
   - Select option `2` and enter the port number to retrieve the associated service name.

3. **Port Scanning**:
   - Select option `3`, enter the target IP address or hostname, and specify the port range to scan for open ports.

4. **Check if a Port is Open**:
   - Select option `4`, enter the target IP address or hostname, and specify the port number to check if it is open.

5. **Get IP of a Domain**:
   - Select option `5` and enter the domain name to resolve its IP address.

6. **DNS Lookup**:
   - Select option `6` and enter the domain name to perform a DNS lookup and retrieve all associated IP addresses.

7. **IP Locator**:
   - Select option `7` and enter the IP address to get geographical information such as country, region, city, etc.

8. **Exit**:
   - Select option `8` to exit the tool.

## Example

```bash
$ python baraa_scan.py

  ____            _       ____                  
 | __ )  __ _ ___| |__   / ___|  ___ __ _ _ __  
 |  _ \ / _` / __| '_ \  \___ \ / __/ _` | '_ \ 
 | |_) | (_| \__ \ | | |  ___) | (_| (_| | | | |
 |____/ \__,_|___/_| |_| |____/ \___\__,_|_| |_|
 
Create by Eng Baraa Sahmoud

Menu:
*** Baraa Scan ***
1. Get localhost
2. Get the service name for this port
3. Port scanning
4. Check if a port is open
5. Get the IP of this domain
6. DNS lookup
7. IP Locator
8. Exit
*** ☠️ ***
Enter your choice (1-8): 3
Enter the target IP address or hostname: 192.168.1.1
Enter the starting port: 1
Enter the ending port: 100
Open ports:
22
80
```


.

---

