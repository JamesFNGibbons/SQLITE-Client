
import os
import importlib

class commands:

    def __init__(self):
        self.description = 'Provides a list of commands.'

    def on_run(self, params):
        print('-------------------------------------')
        print('--------- List of Commands ----------');
        print('-------------------------------------')
        print("\n");

        # List all the files in the commands direcroty
        # and read the descriptions.
        files = os.listdir('./commands');
        for name in files:
            if(not name.split('.')[1] == 'pyc'):
                cmd_name = name.split('.')[0]

                if(not cmd_name == '__init__'):
                    i = importlib.import_module("commands.commands")
                    x = getattr(i, 'commands')
                    cmd = x()

                    print(cmd_name + ' ==== ' + cmd.description)
        print("\n\n")
