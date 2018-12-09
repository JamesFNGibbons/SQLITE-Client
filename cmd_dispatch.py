"""
    This class is used to manage the command that has been
    entered by the user. It will first check that a command
    exists in the commands folder, which holds the executables.

    If the command does not exist, it will return a false, and
    will return a success if true.

    This class will also manage the paramaters of the commands, and
    pass them to the command executables (located in the commands dir)
    accordingly.

    James Gibbons N0803826
    Nottingham Trent University.

"""

import os.path
import importlib

class Cmd_Handler:

    def __init__(self, cmd):
        # Check if the command exists in the commands dir.
        self.is_valid = os.path.isfile('./commands/' + cmd + '.py')
        self.response = '';

        # Split the command itself away from its params.
        base_cmd = cmd.split(' ')[0]

        # We will now put the paramaters into an array.
        params = []
        for param in cmd.split(' '):
            if(not param == base_cmd):
                params.append(param)

        if(self.is_valid):
            i = importlib.import_module("commands." + base_cmd)
            x = getattr(i, base_cmd)
            cmd = x()
            cmd.on_run(params)

    """
        This function is used to give the resonse
        back to the main loop, and ensure that the
        command is valid. This will also contain the
        response from the command itself, if any.
    """
    def get_response(self):
        return {
            is_valid: self.is_valid,
            response: self.response
        }
