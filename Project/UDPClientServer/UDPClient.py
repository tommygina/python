# !/usr/bin/python

import socket

def udpclient(udpserverip, udpserverport):
    addr = (udpserverip, udpserverport)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input()
        if not data:
            print("input msg error")
            break
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == '__main__':
    udpclient("127.0.0.1", 8888)
