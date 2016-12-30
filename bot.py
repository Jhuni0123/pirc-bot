from ircconnector import IRCConnector
from config import *

class Bot:
    def __init__(self, server, port):
        self.irc = IRCConnector(server, port)
        self.irc.init_user(botname)
        self.irc.set_nick(botnick)
        chan = '#jhuni-bot-test'
        self.irc.join_chan(chan)
        self.irc.send_msg(chan, 'Hi')
        self.irc.get_names(chan)

    def run(self):
        while True:
            msg = self.irc.get_next_msg()
            if msg['command'] == 'PRIVMSG':
                self.irc.send_msg(msg['target'], msg['text'])

if __name__ == '__main__':
    bot = Bot(server, port)
    bot.run()
