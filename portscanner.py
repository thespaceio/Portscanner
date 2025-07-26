
import socket
from IPy import IP

class Portscan():
    banner_list = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num


    def scan(self):
        for port in range(1, 100):
            self.scan_port(port)

    """
    To get the IP address of a website we use;
    "nslookup + (website name)" in the terminal.
    """
    def check_ip(self):
        try:
            # IP(ip)
            IP(self.target)
            return (self.target)
        except ValueError:
            return socket.gethostbyname(self.target)





    # This will only run with the IP website, not with the name of the website.
    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)        # This will make it run faster, though we lose the accuracy but, it runs faster. But if after 0.5secs if it does not get a socket it takes it has closed
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip("\n").strip("\r")
                self.banner_list.append(banner)
            except:
                self.banner_list.append(" ")
            sock.close()
        except:
            pass


"""    # To test this code in the main module, so it does not run in another module when imported as a library module
if __name__ == "__main__":
    target = input("[+] Enter target(s) to scan(Separate multiple targets with ','): ")
    # port_num = input("Enter the number of ports that you want to scan: ")

    if "," in target:
        for ips in target.split(","):
            scan(ips.strip(" "))
    else:
        scan(target)"""

