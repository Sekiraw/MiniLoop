# MiniLoop

MiniLoop is a lightweight Python game loop library designed to provide a simple and efficient way to manage update and render cycles in real-time applications.

---

## Why MiniLoop?
When developing real-time applications like games and simulations, having an efficient and stable game loop is crucial. MiniLoop is designed to provide a precise, high-performance loop with built-in timing management, making it a superior alternative to a basic while loop.

- <strong>More Accurate Frame Timing</strong>
    - MiniLoop ensures consistent frame pacing by using a high-resolution timer. Unlike a simple while loop that can suffer from frame drift and timing inconsistencies, MiniLoop dynamically adjusts to keep the frame rate steady.

- <strong>Improved CPU Efficiency</strong>
    - A basic while loop can waste CPU cycles when waiting for the next frame, leading to higher power consumption and unnecessary CPU usage. MiniLoop intelligently sleeps between frames, reducing resource usage while maintaining target FPS.

- <strong>Higher FPS Stability</strong>
From our benchmarks:

MiniLoop achieved <u>60.69 FPS</u>
While loop only reached <u>58.89 FPS</u> 
This means <strong>MiniLoop maintains a smoother experience</strong>, preventing stuttering and inconsistencies.
- <strong>Optimized Python Function Calls</strong>
    - MiniLoop caches function pointers before the loop starts, minimizing overhead when calling update() and render().
A plain while loop calls Python functions inefficiently, slowing down performance.
- <strong>Cross-Platform & Easy to Use</strong>
    - Works on Windows, Linux, and macOS with precise timing control.
Simple API: just set your update() and render() functions, and MiniLoop takes care of the rest.
- <strong>Built-In Stop Handling</strong>
    - MiniLoop includes a clean stop mechanism that allows safe termination from Python, unlike a while loop that may require manual handling with try/except.

TL;DR
- More stable FPS
- Lower CPU usage
- Better timing accuracy
- Easier to use

If you're working on a game, simulation, or any real-time application, MiniLoop is the better choice. Try it out and experience a smoother, more efficient loop!

## Features

- High-performance game loop with adjustable FPS
- Support for user-defined update and render callbacks
- Cross-platform high-resolution timer
- Simple start/stop functionality

---

## Requirements

- Python 3.x (recommended: 3.7 or higher)

---

## Installation

Install the package using pip:

```bash
pip install miniloop
```

## Usage
Here is an example of how to use MiniLoop:

```python
import miniloop

def update(delta_time):
    print(f"Update: {delta_time:.5f} sec")

def render():
    print("Rendering frame")

miniloop.set_update(update)
miniloop.set_render(render)
miniloop.set_fps(60)  # Target 60 FPS

miniloop.start()
```
## Output Example
```plaintext
Update: 0.01667 sec
Rendering frame
Update: 0.01665 sec
Rendering frame
...
```

# Performance Benchmark: Miniloop vs While Loop

This benchmark compares the performance of **Miniloop** and a standard **While Loop** at different frame rates (FPS) and durations. The test evaluates both accuracy (how closely the achieved FPS matches the target) and stability (frame-time consistency).

## Test Configuration
- **Durations Tested:** 3s, 5s, 10s  
- **FPS Targets:** 30, 60, 120  
- **Metrics Evaluated:**  
  - **Achieved FPS:** The actual FPS measured during execution.  
  - **Score (0-200):** A combination of accuracy and stability.  

## Results

### 3-Second Tests
| FPS Target | Miniloop Achieved FPS | Miniloop Score | While Loop Achieved FPS | While Loop Score |
|------------|----------------------|---------------|----------------------|---------------|
| 30 FPS     | 30.15                 | 199.55        | 29.73                 | 199.17        |
| 60 FPS     | 60.83                 | 197.50        | 58.98                 | 196.87        |
| 120 FPS    | 117.47                | 192.40        | 116.26                | 188.77        |

### 5-Second Tests
| FPS Target | Miniloop Achieved FPS | Miniloop Score | While Loop Achieved FPS | While Loop Score |
|------------|----------------------|---------------|----------------------|---------------|
| 30 FPS     | 30.00                 | 199.99        | 29.74                 | 199.23        |
| 60 FPS     | 60.55                 | 198.33        | 58.94                 | 196.82        |
| 120 FPS    | 118.07                | 194.20        | 116.14                | 188.41        |

### 10-Second Tests
| FPS Target | Miniloop Achieved FPS | Miniloop Score | While Loop Achieved FPS | While Loop Score |
|------------|----------------------|---------------|----------------------|---------------|
| 30 FPS     | 29.94                 | 199.80        | 29.75                 | 199.25        |
| 60 FPS     | 60.64                 | 198.09        | 58.93                 | 196.78        |
| 120 FPS    | 117.59                | 192.78        | 116.22                | 188.64        |

---

## Final Performance Summary
- **Miniloop Average Score:** **196.97 / 200**  
- **While Loop Average Score:** **194.87 / 200**  

## Conclusion
Miniloop outperformed the While Loop overall, achieving a slightly higher **accuracy and stability** in frame rates, particularly at higher FPS targets. While both methods performed well, Miniloop provided better consistency, especially for longer durations.

## How It Works
MiniLoop miniloop runs a continuous loop, calling the user-defined update and render functions at a target frame rate. The update function receives delta_time, which represents the time elapsed since the last frame, allowing smooth time-based updates.

## Limitations
- ~~Currently limited to single-threaded execution.~~
- No built-in event handling; input handling must be managed externally.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## Local Development
To set up a local development environment, follow these steps:

1. Create and activate a virtual environment:
    ```bash
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    venv/Scripts/activate
    ```
2. Build & install the project
    ```bash
    python setup.py build
    python setup.py install
    ```
The module is now installed in the virtual environment. You can test it by running the example script:

```bash
python examples/example.py
```


## License
This project is licensed under the Apache-2.0 License. See the LICENSE file for details.

## Author
Developed by Sekiraw

## Acknowledgements
Thanks to the Python development community for providing tools and resources to make this project possible.

```vbnet
This styling ensures clarity, proper sectioning, and good readability. Let me know if you`d like any further adjustments!
```
