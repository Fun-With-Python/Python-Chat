import socket
import sys
#dwdawa
HOST, PORT = "localhost", 59999
data = "".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data + "\n")
    
        # Receive data from the server and shut down
        received = sock.recv(1024)

        print "Sent:     {}".format(data)
        print "Received: {}".format(received)
    finally:
        sock.close()
        
        data = raw_input()
        if data == "" :
            break;
