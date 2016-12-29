from ircconnector import IRCConnector
from config import *

class Bot:
    def __init__(self):
        self.irc = IRCConnector(server, port)
        self.irc.init_user(botname)
        self.irc.set_nick(botnick)
        chan = '#jhuni-bot-test'
        self.irc.join_chan(chan)
        self.irc.send_msg(chan, 'Hi')

    def run(self):
        while True:
            if not self.irc.msg_queue.empty():
                s = self.irc.msg_queue.get()
                if s:
                    pass

if __name__ == '__main__':
    bot = Bot()
    bot.run()
