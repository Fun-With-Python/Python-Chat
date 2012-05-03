from Tkinter import *
from socket import *
import thread

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.socket()

    def callback(self, event):
        message = self.entry_field.get()
        tcpCliSock.send(message)

    def create_widgets(self):
        self.messaging_field = Text(self, width = 110, height = 20, wrap = WORD)
        self.messaging_field.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.entry_field = Entry(self, width = 92)
        self.entry_field.grid(row = 1, column = 0, sticky = W)
        self.entry_field.bind('<Return>', self.callback)

    def add(self, data):
        self.messaging_field.insert(END, data)

    def socket(self):
        def loop0():
            while 1:
                data = tcpCliSock.recv(BUFSIZE)
                if data: self.add(data)

        thread.start_new_thread(loop0, ())



root = Tk()
root.title("Chat client")
root.geometry("550x260")

app = Application(root)

root.mainloop()

