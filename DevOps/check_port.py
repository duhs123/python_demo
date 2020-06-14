import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)

for ip in 37, 38,40:
    try:
        sk.connect(("172.26.0." + str(ip), 10000))
        print("172.26.0.%d server open \n" % ip)
    except Exception:
        print("172.26.0.%d server not open" % ip)

sk.close()
