# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya

from typing import Callable

def start() -> None:
    """
    Starts the game loop.
    The loop will run until `stop()` is called.
    """
    ...

def stop() -> None:
    """
    Stops the game loop, causing `start()` to return.
    """
    ...

def set_update(callback: Callable[[float], None]) -> None:
    """
    Sets the update function.
    
    The update function is called every frame with `delta_time` (time in seconds since last frame).
    
    :param callback: A function that takes a single `float` argument representing delta time.
    """
    ...

def set_render(callback: Callable[[], None]) -> None:
    """
    Sets the render function.
    
    The render function is called every frame after the update function.
    
    :param callback: A function that takes no arguments and returns nothing.
    """
    ...

def set_fps(fps: float) -> None:
    """
    Sets the target frames per second (FPS) for the loop.
    
    :param fps: The desired FPS (e.g., 60.0 for 60 FPS).
    """
    ...