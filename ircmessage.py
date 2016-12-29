import re

class IRCMessage(dict):
    def __init__(self, msg):
        msg = msg.strip()
        self['command'] = None
        self['sender'] = None
        match = re.search('^(?::(\S+) )?([a-zA-Z]+|\d\d\d)((?: [^: \t\n\r\f\v]\S*)*)(?: :(.*))?$', msg)
        if match:
            sender, command, params, text = match.groups()
            params = params.split()
            self['sender'] = sender
            self['command'] = command
            if command.isnumeric():
                params = params[1:]
                if text != None:
                    params.append(text)
                self['text'] = ' '.join(params)
            elif command == 'PING':
                self['server'] = text.strip()
            elif command in ['NOTICE', 'PRIVMSG']:
                self['target'] = params[0]
                self['text'] = text
            elif command == 'INVITE':
                self['target'] = params[1]
            elif command == 'MODE':
                self['target'] = params[0]
                self['mode'] = params[1]
                if len(param) > 2:
                    self['users'] = params[2:]
            elif commnad == 'ERROR':
                self['text'] = text
        else:
            self['text'] = msg
        print(msg)
        print(self)

