# Echo server program
import socket, socketserver, pickle
from algo import *

import socketserver

class ServerSA(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = pickle.loads(self.request.recv(1024).strip())
        print('Sort requested'+str(self.data[0]) + 'for the array : '+str(self.data[1]))

        if self.data[0] == 'bubble_sort':
            res = bubble_sort(self.data[1])
        elif self.data[0] == 'optimised_bubble_sort':
            res = optimisedbubble_sort(self.data[1])
        elif self.data[0] == 'selection_sort':
            res = selection_sort(self.data[1])
        elif self.data[0] == 'insertion_sort':
            res = insertion_sort(self.data[1])
        elif self.data[0] == 'cocktail_sort':
            res = cocktail_sort(self.data[1])
        elif self.data[0] == 'bogo_sort':
            res = bogo_sort(self.data[1])
        elif self.data[0] == 'count_sort':
            res = counting_sort(self.data[1])
        elif self.data[0] == 'bucket_sort':
            res = bucket_sort(self.data[1])

        self.request.sendall(pickle.dumps(res))

if __name__ == '__main__':
    HOST, PORT = 'localhost', 15151

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), ServerSA) as server:
        server.serve_forever()