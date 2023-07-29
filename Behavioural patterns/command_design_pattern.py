"""
Command design pattern:

The Command design pattern is a behavioral pattern that converts requests or simple operations into standalone objects. It allows you to parameterize objects with different requests, delay or queue a request's execution, and support undoable operations.

Let's create an example of a simple command design pattern for a remote control that operates electronic devices (e.g., TV, Stereo). We'll have a Command interface, concrete command classes (TurnOnCommand and TurnOffCommand), and an Invoker class (remote control) that triggers the commands.
"""

from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command class for turning on a device
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

# Concrete Command class for turning off a device
class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

# Receiver class (Electronic devices)
class Television:
    def turn_on(self):
        print("TV is turned on.")

    def turn_off(self):
        print("TV is turned off.")

class Stereo:
    def turn_on(self):
        print("Stereo is turned on.")

    def turn_off(self):
        print("Stereo is turned off.")

# Invoker class (Remote Control)
class RemoteControl:
    def __init__(self):
        self._commands = {}

    def add_command(self, command_name, command):
        self._commands[command_name] = command

    def press_button(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Invalid command!")

# Example usage
if __name__ == "__main__":
    tv = Television()
    stereo = Stereo()

    turn_on_tv = TurnOnCommand(tv)
    turn_off_tv = TurnOffCommand(tv)
    turn_on_stereo = TurnOnCommand(stereo)
    turn_off_stereo = TurnOffCommand(stereo)

    remote = RemoteControl()
    remote.add_command("on_tv", turn_on_tv)
    remote.add_command("off_tv", turn_off_tv)
    remote.add_command("on_stereo", turn_on_stereo)
    remote.add_command("off_stereo", turn_off_stereo)

    remote.press_button("on_tv")     # Output: TV is turned on.
    remote.press_button("off_tv")    # Output: TV is turned off.
    remote.press_button("on_stereo") # Output: Stereo is turned on.
    remote.press_button("off_stereo")# Output: Stereo is turned off.
    remote.press_button("invalid")   # Output: Invalid command!





"""
In this example, the Command interface defines the execute() method that encapsulates the action to be performed. The TurnOnCommand and TurnOffCommand classes are concrete commands that encapsulate the actions of turning on and turning off electronic devices (Television and Stereo). The Television and Stereo classes are the receivers that perform the actual actions.

The RemoteControl class acts as the invoker and maintains a dictionary of commands. It can add new commands and trigger the execution of a command when a button is pressed.

By using the Command design pattern, the remote control can easily support different commands, and it is also possible to queue or undo commands if needed. The pattern promotes flexibility and extensibility in handling user actions.
"""
