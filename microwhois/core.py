import socket

def lookup(domain):

    print()
    print("MicroWhois")
    print("=" * 40)

    try:
        s = socket.create_connection(("whois.iana.org",43),timeout=5)
        s.send((domain + "\r\n").encode())

        data = b""

        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk

        s.close()

        print(data.decode(errors="replace"))

    except Exception as e:
        print("WHOIS lookup failed.")
        print(e)
