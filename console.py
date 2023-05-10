#!/usr/bin/python3
"""The Command Line Interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines Airbnb clone public class instances."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function handle end of file character (Ctrl+D)."""

        print()
        return (True)

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""

        return

    def emptyline(self):
        """Function that does nothing on ENTER."""

        pass


if __name__ == '__main__':
HBNBCommand().cmdloop()
