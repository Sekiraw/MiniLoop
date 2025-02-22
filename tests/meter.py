# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya

import time
import threading
import miniloop

frame_count_miniloop = 0


def update(delta_time):
    global frame_count_miniloop
    frame_count_miniloop += 1


def render():
    pass


def miniloop_test(duration=5, fps=60):
    global frame_count_miniloop
    frame_count_miniloop = 0

    miniloop.set_update(update)
    miniloop.set_render(render)
    miniloop.set_fps(fps)

    def stop_after_delay():
        time.sleep(duration)
        miniloop.stop()

    threading.Thread(target=stop_after_delay).start()

    start_time = time.perf_counter()
    miniloop.start()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Miniloop ran for {elapsed_time:.5f} seconds.")
    print(f"Frames processed by Miniloop: {frame_count_miniloop}")
    print(f"Achieved FPS: {frame_count_miniloop / elapsed_time:.2f}")


def while_loop_test(duration=5, fps=60):
    target_fps = fps
    frame_time = 1.0 / target_fps
    start_time = time.perf_counter()
    frame_count = 0

    while time.perf_counter() - start_time < duration:
        frame_start = time.perf_counter()
        time.sleep(frame_time)
        frame_count += 1

    elapsed_time = time.perf_counter() - start_time
    print(f"While loop ran for {elapsed_time:.5f} seconds.")
    print(f"Frames processed: {frame_count}")
    print(f"Achieved FPS: {frame_count / elapsed_time:.2f}")


print("Testing Miniloop:")
miniloop_test(3)

print("\nTesting While Loop:")
while_loop_test(3)
