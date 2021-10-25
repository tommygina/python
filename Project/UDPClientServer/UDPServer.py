# !/usr/bin/python

import socket

def udpserver(udpserverport):
    address = ('0.0.0.0', udpserverport)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)

    print("udp server is running at", udpserverport)

    while True:
        data, addr = s.recvfrom(2048)
        if not data:
            break
        print("got data from", addr)
        print(data.decode())
    s.close()

if __name__ == '__main__':
	udpserver(8888)