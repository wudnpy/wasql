import os
import string
import sys
import random
import re

import json
import socket

class ASQLConnector():

    user = None
    dataset = {}

    # Отправка данных на сервер
    def connect(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 7653))

        f_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

        self.dataset['f_name'] = f_name

        json_data = json.dumps(self.dataset, ensure_ascii=False)
        #print("JSON DATA: " + str(json_data))
        json_data = json_data.encode("utf-8")
        #print("ENCODE JSON DATA: "+str(json_data))
        #json_data = json_data.decode('utf-8')
        #print("DECODE JSON DATA: " + str(json_data))
        client_socket.send(json_data)

        client_socket.close()
