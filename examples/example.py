# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya

import miniloop
import threading

def update(delta_time):
    print(f"Update: {delta_time:.5f} sec")

def render():
    print("Rendering frame")

# Function to listen for user input and stop the loop
def wait_for_exit():
    input("Press Enter to stop...\n")
    miniloop.stop()

miniloop.set_update(update)
miniloop.set_render(render)
miniloop.set_fps(60)

# Start a separate thread to listen for user input
input_thread = threading.Thread(target=wait_for_exit)
input_thread.start()

# Start the game loop
miniloop.start()
