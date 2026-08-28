import socket
from datetime import datetime
import threading

print("=== Port-Hunter v2.0 Turbo - By ccr600 ===")
target = input("Enter IP or domain to scan: ")
print(f"Scanning target: {target}")
print("Scanning 65,535 ports...")

start_time = datetime.now()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except:
        pass

threads = []
for port in range(1, 65536):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

    if len(threads) >= 100:
        for th in threads:
            th.join()
        threads = []

for th in threads:
    th.join()

end_time = datetime.now()
total_time = end_time - start_time
print(f"\nScanning completed in: {total_time}")