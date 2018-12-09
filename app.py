
from cmd_dispatch import Cmd_Handler

if(__name__ == '__main__'):
    next_cmd = True
    while(next_cmd):
        try:
            cmd = raw_input('(`help` for list of commands) $> ')

            # Check if the user wants to quit.
            if(cmd == 'exit' or cmd == 'close'):
                next_cmd = False
                print('Goodbye!')
            else:

                # Send the command to the command executor.
                command = Cmd_Handler(cmd)
                if(not command.is_valid):
                    print "That command does not exist. Please try again."

        except(ValueError):
            print 'Please enter a valid command.'
