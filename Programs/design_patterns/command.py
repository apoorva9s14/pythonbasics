"""
Command design patterns
"""

# -----------------------------------------------------------------------
# need to start by preparing what will be executed
# and then to execute it when needed.

import os


class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)


class History(object):
    def __init__(self):
        self._commands = list()

    def history_execute(self, command):
        self._commands.append(command)
        command.execute()

    def history_undo(self):
        self._commands.pop().undo()


history = History()
history.history_execute(RenameFileCommand('command_sample.txt', 'command_sample_copy.txt'))
history.history_undo()
