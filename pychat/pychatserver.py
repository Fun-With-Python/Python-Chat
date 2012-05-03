import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        if("Hallo Server" in self.data):
            self.request.sendall("Hallo Client")
        else:
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 59999

    # Create the server, binding to localhost on port 59999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
