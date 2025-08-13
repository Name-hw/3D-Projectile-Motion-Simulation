import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation

GRAVITATIONAL_ACCELERATION = 9.8  # m/s^2
TOTAL_TIME = 10  # seconds
DELTA_TIME = 0.05  # seconds

time = np.arange(0, TOTAL_TIME, DELTA_TIME)  # seconds
initial_speed = 9  # m/s
theta = 45  # degrees

fig, ax = plt.subplots(1, 1, figsize=(7.5, 7.5))
x = []  # m
y = []  # m
line = ax.plot(0, 0)[0]
frame_count = int(TOTAL_TIME / DELTA_TIME)


def init():
    ax.set_title("Projection Motion Simulation Over Time")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.set_xlabel("X-axis (m)")
    ax.set_ylabel("Y-axis (m)")

    return ax.lines


def update(frame):
    t = time[frame]
    velocity_x = initial_speed * np.cos(np.radians(theta))  # m/s
    velocity_y = initial_speed * np.sin(np.radians(theta))  # m/s
    x.append(velocity_x * t)
    y.append(velocity_y * t - (GRAVITATIONAL_ACCELERATION * t**2) / 2)

    line.set_data(x[:frame], y[:frame])

    print(f"Frame: {frame}, t: {t}, x: {x[frame]}, y: {y[frame]}")

    return (line,)


anim = FuncAnimation(
    fig,
    update,
    frames=frame_count,
    init_func=init,
    interval=DELTA_TIME * 1000,
    repeat=False,
)
plt.show()

# anim.save("animation.gif")
