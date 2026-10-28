# Port-Hunter v2.0 Turbo

A lightweight, fast TCP port scanner written in pure Python. No nmap, no dependencies.

By ccr600

### How it works
- **AF_INET + SOCK_STREAM:** TCP / IPv4 scanning
- **settimeout(0.5):** No hanging threads
- **Limited Threading (100):** Scans in batches of 100

### Usage
python main.py

### Example
Enter IP or domain to scan: scanme.nmap.org
Port 22 is open
Port 80 is open

### Docker - DevSecOps

```bash
docker build -t port-hunter-v2 .
docker run -it --rm port-hunter-v2
```
