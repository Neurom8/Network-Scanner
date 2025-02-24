# Network Scanner
A simple network scanner that identifies active hosts and open ports on a given network. It is useful for network administrators, security analysts, and anyone needing to audit network configurations.
## Features
- Scans IP ranges to identify active hosts.
- Performs port scanning on live hosts.
- Provides detailed information on open ports and services.
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Neurom8/Network-Scanner.git
    cd Network-Scanner
    ```

2. Install required dependencies:

    ```bash
    pip3 install python-nmap
    ```

3. Ensure you have `nmap` installed on your machine:

    For Kali/Linux:
    ```bash
    sudo apt-get install nmap
    ```

    For Windows:
    Download and install Nmap from [nmap.org](https://nmap.org/download.html).

## Usage

To use the network scanner:

1. Run the script in the terminal:

    ```bash
    python3 scanner.py
    ```

2. Enter the target IP or range when prompted.

Example:
```bash
$ python3 scanner.py
Enter IP range or address to scan: 
