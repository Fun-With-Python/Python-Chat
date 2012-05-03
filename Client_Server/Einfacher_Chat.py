import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

try: 
    while True: 
        komm, addr = s.accept() 
        while True: 
            data = komm.recv(1024)

            if not data: 
                komm.close() 
                break

            print "[%s] %s" % (addr[0], data) 
            nachricht = raw_input("Antwort: ") 
            komm.send(nachricht) 
finally: 
    s.close()
