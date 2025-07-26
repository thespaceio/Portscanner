
# 🔎 Portscanner

A simple Python-based port scanner that identifies open ports on a given IP address or hostname. This scanner also attempts to retrieve service banners from open ports, providing basic fingerprinting for services running on the target.

## 📜 Description

This `Portscanner` script uses the Python `socket` and `IPy` libraries to perform basic port scanning tasks. It accepts a target (IP address or domain name), checks if the IP is valid or resolves the domain to an IP, and scans a range of ports to identify which are open.

The scanner also tries to grab banners from open ports — this can give insight into the service running on the port (e.g., Apache, SSH, FTP, etc.).

---

## 🚀 Features

* ✅ Scans ports in the range `1–99` (customizable)
* ✅ Detects and lists open ports
* ✅ Grabs banners from open ports (if available)
* ✅ Accepts IP address or domain name as target
* ✅ Handles single or multiple targets (see note below)
* ⚠️ Lightweight and fast with a 0.5s timeout per port

---

## 🧰 Requirements

* Python 3.x
* [`IPy`](https://pypi.org/project/IPy/)

Install IPy with:

```bash
pip install IPy
```

---

## 📁 File Structure

```bash
portscanner.py    # Main port scanning logic
```

---

## 🧪 Usage

You can run the script by editing the `__main__` block (currently commented out at the bottom of the script). Here's an example on how to use it:

```python
if __name__ == "__main__":
    target = input("[+] Enter target(s) to scan (separate multiple targets with ','): ")
    
    if "," in target:
        for ip in target.split(","):
            scanner = Portscan(ip.strip(), 99)
            scanner.scan()
            print(f"\n[+] Results for {ip.strip()}:")
            print(f"Open Ports: {scanner.open_ports}")
            print(f"Banners: {scanner.banner_list}")
    else:
        scanner = Portscan(target, 99)
        scanner.scan()
        print(f"\n[+] Results for {target}:")
        print(f"Open Ports: {scanner.open_ports}")
        print(f"Banners: {scanner.banner_list}")
```

Then run the script:

```bash
python portscanner.py
```

---

## 📌 Notes

* The scanner uses a fixed port range (`1–99`). You can modify the `scan()` method or pass custom ranges for broader scans.
* Domain resolution is handled automatically using `socket.gethostbyname()`.
* This tool is for **educational purposes only**. Always ensure you have permission before scanning any target.

---

## 🔐 Disclaimer

> ⚠️ **This tool is intended for educational and ethical security testing only. Unauthorized scanning of networks or devices is illegal and unethical. Use responsibly.**

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
