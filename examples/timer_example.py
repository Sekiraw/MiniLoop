# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya

import miniloop

class Timer:
    """A simple timer that triggers a callback at a fixed interval."""
    def __init__(self, interval: float, callback):
        """
        :param interval: Time interval in seconds.
        :param callback: Function to call when the timer reaches the interval.
        """
        self.interval = interval
        self.callback = callback
        self.elapsed_time = 0.0

    def update(self, delta_time: float):
        """Updates the timer and calls the callback when the interval is reached."""
        self.elapsed_time += delta_time
        if self.elapsed_time >= self.interval:
            self.callback()
            self.elapsed_time = 0.0  # Reset timer

class Game:
    def __init__(self):
        """Initializes the game and creates a timer."""
        self.timer = Timer(3.0, self.on_timer_trigger)

    def on_timer_trigger(self):
        """Function called every 3 seconds."""
        print("3 seconds have passed!")

    def update(self, delta_time: float):
        """Updates game logic, including the timer."""
        self.timer.update(delta_time)

    def render(self):
        """Handles rendering (if needed)."""
        pass

    def run(self, fps: float = 60):
        """Starts the game loop."""
        miniloop.set_update(self.update)
        miniloop.set_render(self.render)
        miniloop.set_fps(fps)
        miniloop.start()

# Create a game instance and run
game = Game()
game.run()
