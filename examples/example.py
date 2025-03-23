# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya

import miniloop

# Example update function
def update(delta_time):
    print(f"Updating game logic... Delta time: {delta_time:.2f}")

# Example render function
def render():
    print("Rendering frame...")

# Set callbacks
miniloop.set_update(update)
miniloop.set_render(render)

# Set target FPS
miniloop.set_fps(60)

try:
    print("Starting game loop!")
    miniloop.start()
except KeyboardInterrupt:
    print("Stopping game loop...")
    miniloop.stop()

