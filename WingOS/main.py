'''
 [011010111011]
 [011010111011]
 [011010111011]
               [011010111011]
               [011010111011]
               [011010111011]
                             [011010111011]
                             [011010111011]
                             [011010111011]

        The Blackwing Project: WingOS
This is our little project, designed to be an os that runs in python and C++. Is it efficient? No. Will it work? Yes.
'''
try:
    from sly import Lexer, Parser
    import login
    import nano
    import os
    import sudo
    import sys
    import username
except ImportError as e:
    print("Internal ImportError Found, Please contact the dev with the error message:\n\n%s" % e)
    exit(0)
except AttributeError as e:
    print("Internal AttributeError Found, Please contact the dev with the error message:\n\n%s" % e)
    exit(0)     

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

dir=str(os.getcwd())

def run_console():
    class OSLexerconsole(Lexer):
        tokens = {
            FILE, EXIT, HELP, INFO, CLEAR, SUDO, ALPHA, LS, ARGS, CHANGE, PWD, NANO, RM, LOG, BIOS
        }

        EXIT = 'exit'
        ARGS = r'(-[A-Za-z0-9]{1})(?<!--[A-Za-z0-9])'
        HELP = 'help'
        INFO = 'info'
        CLEAR = 'clear'
        NANO = 'nano'
        SUDO = 'sudo.*'
        ALPHA = 'alpha'
        LS = 'ls'
        CHANGE = r'change\w'
        PWD = 'pwd'
        FILE = '([A-Za-z0-9]+).([A-Za-z0-9]+)'
        RM = "rm"
        LOG = "log.*"
        BIOS = "bios.*"

        ignore = r' ()'
        ignore_newline = r'\n'
        ignore_tab = r'\t'
        
        def error(self, t):
            if self.index==0:
                print("Command:",console,"not found in command list or you don't have the permissions to execute it (Are you root?)")
                blockPrint()
                self.index += 1
            else:
                self.index += 1

    class OSParserconsole(Parser):
        tokens = OSLexerconsole.tokens

        @_('CLEAR')
        def statement(self, t):
            os.system('clear')
            blockPrint()

        @_('EXIT')
        def statement(self, t):
            exit(0)

        @_('BIOS')
        def statement(self, t):
            if t.LOG == "bios log":
                with open("data.txt") as f:
                    text=f.read()
                    f.close()
                print(text)

        @_('RM FILE')
        def statement(self, t):
            if os.path.exists(t.FILE):
                os.removedirs(t.FILE)

        @_('ALPHA SUDO')
        def statement(self, t):
            if os.path.exists("log.txt"):
                with open("log.txt","w") as f:
                    wrt=t.ALPHA+t.SUDO
                    f.write(wrt)
                    f.close()
                    sudo.alphacmds()
            else:
                with open("log.txt","x") as f:
                    wrt=t.ALPHA+t.SUDO
                    f.write(wrt)
                    f.close()
                    sudo.alphacmds()

        @_('CHANGE ARGS')
        def statement(self, t):
            try:
                if t.ARGS == "-n":
                    login.change_username()
                    blockPrint()
                elif t.ARGS == "-p":
                    login.change_password()
                    blockPrint()
            except EOFError:
                pass

        @_('NANO FILE')
        def statement(self, t):
            nano.main(t.FILE)

        @_('PWD')
        def statement(self, t):
            print(dir)

        @_('NANO')
        def statement(self,t):
            nano.main(None)

        @_('LOG')
        def statement(self, t):
            if t.LOG == "log view":
                with open("log.txt") as f:
                    text=f.read()
                    f.close()
                print(text)

        @_('LS ARGS')
        def statement(self, t):
            try:
                if t.ARGS == "-a":
                    ls=os.listdir()
                    print(str(ls).strip("[").strip("]"))
                    blockPrint()
                else:
                    ls=os.listdir()
                    lscontent = [x for x in ls if not x.startswith('.')]
                    lscontent = [x for x in lscontent if not x.startswith('_')]
                    lscontent = [x for x in lscontent if not x.endswith('.lock')]
                    ls=str(lscontent)
                    print(ls.strip("[").strip("]"))
                    blockPrint()
            except EOFError:
                pass

        @_('LS')
        def statement(self, t):
            ls=os.listdir()
            lscontent = [x for x in ls if not x.startswith('.')]
            lscontent = [x for x in lscontent if not x.startswith('_')]
            lscontent = [x for x in lscontent if not x.startswith('replit')]
            lscontent = [x for x in lscontent if not x.startswith('Make')]
            lscontent = [x for x in lscontent if not x.endswith('.o')]
            lscontent = [x for x in lscontent if not x.endswith('.toml')]
            lscontent = [x for x in lscontent if not x.endswith('main')]
            lscontent = [x for x in lscontent if not x.endswith('debug')]
            lscontent = [x for x in lscontent if not x.endswith('.lock')]
            ls=str(lscontent)
            print(ls.strip("[").strip("]"))
            blockPrint()

        @_('HELP')
        def statement(self, t):
            enablePrint()
            print('''
Commands:

return = Exits WingOS
help = Opens this message
info = Loads the system information
clear = Clear the console
sudo = Super user commands
fetch = WingOS's APT system
showpwd/hidepwd = show or hide the OSeadcrumb
nano = Text Editor
changepass = change password with associated user
changename = change username with associated user
pwd = show present working directory
ls = list files

GLOBAL ARGS:

-y = Confirm all prompts
--help = show help
-a = access all availiable data
--silent = return no feedback
--error = search an error code
''')
            return 'End of help'

        @_('INFO')
        def statement(self, t):
            enablePrint()
            print('''
WingOS Shell/Language

Full Official Release v1.0.0

Current Channel: Stable Official

Last Update: 27/09/23 16:00 BST

Dev: OrionOreo
''')
            return 'END OF INFO'

    consolelexer = OSLexerconsole()
    consoleparser = OSParserconsole()
    try:
        enablePrint()
        console = input(username.user+"@"+"wing["+dir+"]> ")
        if os.path.exists("log.txt"):
            with open("log.txt","w") as f:
                f.write(console)
                f.close()
        else:
            with open("log.txt","x") as f:
                f.write(console)
                f.close()
        while console:
            result = consoleparser.parse(consolelexer.tokenize(console))
            if os.path.exists("log.txt"):
                with open("log.txt","w") as f:
                    f.write(console)
                    f.close()
            else:
                with open("log.txt","x") as f:
                    f.write(console)
                    f.close()
            print(result)
            enablePrint()
            console = input(username.user+"@"+"wing["+dir+"]> ")
    except EOFError:
        blockPrint()
        pass
    except NameError as e:
        print("Internal NameError Found, Please contact the dev with this error message:\n\n%s" % e)
        exit(2)
    except KeyboardInterrupt:
        x=input("\nAre you sure you want to exit? [Y/N]\n\n")
        x=x.upper()
        if x=="Y":
            exit(1)
        elif x=="N":
            pass
        else:
            print("Bad Input: %s" % x)
    except AttributeError as e:
        print("Internal AttributeError Found, Please contact the dev with this error message:\n\n%s" % e)
        exit(3)

login.auth()
while login.authent is True:
    run_console()