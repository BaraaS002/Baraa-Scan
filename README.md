# Baraa-Scan
create by Eng Baraa Sahmoud

This code is a simple port scanning tool written in Python. It allows the user to perform various actions related to network scanning. Here's a breakdown of the code:

    The code imports the necessary modules: socket for creating socket objects, and re for validating IP address format and obtaining the IP of a domain.

    Two functions are defined: scan_ports for scanning a range of ports on a target host, and validate_ip for validating the format of an IP address.

    The code then utilizes the termcolor and pyfiglet libraries for colorful and stylized text output.

    Inside a while loop, a menu is displayed with different options for the user to choose from.

    Depending on the user's choice, different actions are performed:
        Option 1 retrieves the local host name.
        Option 2 gets the service name associated with a specific port number.
        Option 3 performs port scanning on a target host within a given port range.
        Option 4 checks if a specific port is open on a target host.
        Option 5 obtains the IP address of a given domain.
        Option 6 exits the program.

Overall, this code provides a basic command-line interface for network scanning tasks
