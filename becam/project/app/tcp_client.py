from contextlib import closing
import socket
import json
import time
import os

HOST, PORT = os.getenv('HOST_SOCKET_CLIENT'), 9999


while 1:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.connect((HOST, PORT))
        measurements = {}
        measurements['temperature'] = 28.1
        measurements['humidity'] = 52.1
        measurements['f_measurement'] = '2019-02-10T21:55:37'
        measurements['msystem'] = 1
        measurements = json.dumps(measurements)
        print(measurements)
        sock.sendall(bytes(measurements + "\n", encoding='utf8'))
        received = str(sock.recv(1024))
        print("Received: {}".format(received))
        time.sleep(20)
