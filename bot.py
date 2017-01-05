from ircconnector import IRCConnector
from config import *

class Bot:
    def __init__(self, server, port, botname, botnick):
        self.irc = IRCConnector(server, port)
        # you should init_user and set_nick right after connect
        self.irc.init_user(botname)
        self.irc.set_nick(botnick)

    def run(self):
        while True:
            msg = self.irc.get_next_msg()
            if msg['command'] == 'PRIVMSG':
                self.irc.send_msg(msg['target'], msg['text'])

if __name__ == '__main__':
    bot = Bot(server, port, botname, botnick)
    bot.run()
