"""
State design pattern:

The State design pattern is a behavioral pattern that allows an object to change its behavior when its internal state changes. It allows an object to appear as if it is changing its class when the state changes.

Let's create an example of the State pattern for a simple audio player that can be in different playback states: "Playing," "Paused," and "Stopped." We'll use the State pattern to change the behavior of the audio player based on its current state.
"""

from abc import ABC, abstractmethod

# Context class - AudioPlayer
class AudioPlayer:
    def __init__(self):
        self._state = StoppedState()

    def change_state(self, state):
        self._state = state

    def play(self):
        self._state.play()

    def pause(self):
        self._state.pause()

    def stop(self):
        self._state.stop()

# State interface
class State(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete State - PlayingState
class PlayingState(State):
    def play(self):
        print("Already playing.")

    def pause(self):
        print("Pausing...")
        return PausedState()

    def stop(self):
        print("Stopping...")
        return StoppedState()

# Concrete State - PausedState
class PausedState(State):
    def play(self):
        print("Resuming playback...")
        return PlayingState()

    def pause(self):
        print("Already paused.")

    def stop(self):
        print("Stopping...")
        return StoppedState()

# Concrete State - StoppedState
class StoppedState(State):
    def play(self):
        print("Starting playback...")
        return PlayingState()

    def pause(self):
        print("Playback has not started yet.")

    def stop(self):
        print("Already stopped.")

# Client code
if __name__ == "__main__":
    player = AudioPlayer()

    player.play() # Output: Starting playback...
    player.pause() # Output: Pausing...
    player.play() # Output: Resuming playback...
    player.stop() # Output: Stopping...
    player.pause() # Output: Playback has not started yet.





"""
In this example, we have an AudioPlayer class that acts as the context class, which can change its behavior based on the current state. The audio player can be in one of the three states: PlayingState, PausedState, or StoppedState.

The State interface defines the common interface for all states, with methods to handle play, pause, and stop operations.

The concrete state classes (PlayingState, PausedState, and StoppedState) implement the State interface with specific behavior for each state.

When the client code calls methods like play(), pause(), or stop() on the audio player, the behavior of the player changes based on its current state, as determined by the current concrete state.
"""
