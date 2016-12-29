import re

class IRCMessage(dict):
    def __init__(self, msg):
        match = re.search('^(?::(\S+) )?([a-zA-Z]+|\d\d\d)((?: [^: \t\n\r\f\v]\S*)*)(?: :(.*))?$', msg)
        if match:
            sender, command, params, text = match.groups()
            params = params.split()
            self['command'] = command
            if command.isnumeric():
                params = params[1:]
                if text != None:
                    params.append(text)
                self['text'] = ' '.join(params)
            elif command in ['NOTICE', 'PRIVMSG']:
                self['target'] = params[0]
                self['text'] = text 
        else:
            self['text'] = msg
        print(msg)
        print(self)

