import socket, ssl
import threading
from queue import Queue


class IRCConnector:
    def __init__(self, server, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        self._sock = ssl.wrap_socket(s)

        self.msg_queue = Queue()
        _thread = threading.Thread(target = self.recv_msg, daemon = True)
        _thread.start()

    def init_user(self, name):
        self._send('USER ' + (name + ' ') * 3 + ':' + name)

    def set_nick(self, nick):
        self._send('NICK ' + nick)

    def join_chan(self, chan_name):
        self._send('JOIN ' + chan_name)

    def send_msg(self, chan_name, text):
        self._send('PRIVMSG ' + chan_name + ' ' + text)

    def part_chan(self, chan_name, text = ''):
        self._send('PART ' + chan_name + ' ' + text)

    def _send(self, str):
        self._sock.send((str + '\n').encode())

    def recv_msg(self):
        while True:
            raw_bytes = self._sock.recv(8192)
            if raw_bytes:
                msg_list = raw_bytes.split(b'\r\n')
                msg_list.pop()
                for msg_bytes in msg_list:
                    self.msg_queue.put(msg_bytes.decode(errors = 'ignore').strip('\r\n'))
            else:
                self._sock.close()
                break
