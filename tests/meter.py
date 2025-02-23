# SPDX-License-Identifier: Apache-2.0
# Author: Qiyaya (Improved with Scoring)

import time
import threading
import miniloop

test_results = []

def calculate_score(target_fps, achieved_fps):
    """Calculates accuracy and stability scores, returns total score."""
    accuracy = max(0, 100 - abs(target_fps - achieved_fps) * 2)  # 100 if perfect, penalized for deviation
    stability = max(0, 100 - abs(target_fps - achieved_fps))  # 100 if perfect, less deviation better
    total_score = accuracy + stability
    return accuracy, stability, total_score

def run_miniloop_test(duration, fps):
    """Runs Miniloop for a given duration and FPS, measuring performance."""
    frame_count = 0

    def update(delta_time):
        nonlocal frame_count
        frame_count += 1

    def render():
        pass

    miniloop.set_update(update)
    miniloop.set_render(render)
    miniloop.set_fps(fps)

    def stop_after_delay():
        time.sleep(duration)
        miniloop.stop()

    threading.Thread(target=stop_after_delay, daemon=True).start()

    start_time = time.perf_counter()
    miniloop.start()
    elapsed_time = time.perf_counter() - start_time

    achieved_fps = frame_count / elapsed_time
    accuracy, stability, total_score = calculate_score(fps, achieved_fps)

    result = {
        "type": "Miniloop",
        "duration": duration,
        "target_fps": fps,
        "achieved_fps": achieved_fps,
        "accuracy": accuracy,
        "stability": stability,
        "score": total_score
    }
    test_results.append(result)

    print(f"[Miniloop] Duration: {elapsed_time:.5f}s | FPS: {fps} | Frames: {frame_count} | Achieved FPS: {achieved_fps:.2f} | Score: {total_score}")

def run_while_loop_test(duration, fps):
    """Runs a basic while loop with sleep for a given duration and FPS, measuring performance."""
    frame_time = 1.0 / fps
    start_time = time.perf_counter()
    frame_count = 0

    while time.perf_counter() - start_time < duration:
        frame_start = time.perf_counter()
        frame_count += 1

        elapsed = time.perf_counter() - frame_start
        time.sleep(max(0, frame_time - elapsed))

    elapsed_time = time.perf_counter() - start_time
    achieved_fps = frame_count / elapsed_time
    accuracy, stability, total_score = calculate_score(fps, achieved_fps)

    result = {
        "type": "While Loop",
        "duration": duration,
        "target_fps": fps,
        "achieved_fps": achieved_fps,
        "accuracy": accuracy,
        "stability": stability,
        "score": total_score
    }
    test_results.append(result)

    print(f"[While Loop] Duration: {elapsed_time:.5f}s | FPS: {fps} | Frames: {frame_count} | Achieved FPS: {achieved_fps:.2f} | Score: {total_score}")

# Run tests for multiple FPS and durations
test_durations = [3, 5, 10]
test_fps_values = [30, 60, 120]

for duration in test_durations:
    for fps in test_fps_values:
        print(f"\n--- Testing {duration}s at {fps} FPS ---")
        run_miniloop_test(duration, fps)
        run_while_loop_test(duration, fps)

# Print final summary
print("\n===== FINAL PERFORMANCE SUMMARY =====")
miniloop_avg_score = sum(r["score"] for r in test_results if r["type"] == "Miniloop") / len([r for r in test_results if r["type"] == "Miniloop"])
while_loop_avg_score = sum(r["score"] for r in test_results if r["type"] == "While Loop") / len([r for r in test_results if r["type"] == "While Loop"])

print(f"\nMiniloop Average Score: {miniloop_avg_score:.2f}/200")
print(f"While Loop Average Score: {while_loop_avg_score:.2f}/200")

if miniloop_avg_score > while_loop_avg_score:
    print("\nMiniloop performed better overall.")
elif miniloop_avg_score < while_loop_avg_score:
    print("\nWhile Loop performed better overall.")
else:
    print("\nBoth performed equally well.")

print("=====================================")
