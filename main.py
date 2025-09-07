import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == '__main__':
    total_frames = 30
    t_values = np.linspace(0, 1, total_frames)

    true_displacement = t_values**2
    discrete_displacement = 2 * t_values
    integrated_displacement = 1 * t_values
    wall_position = 1.0

    fig, (ax_time, ax_sim) = plt.subplots(2, 1, figsize=(8, 8))
    plt.subplots_adjust(hspace=0.5)

    fig.canvas.manager.set_window_title("Visualization")

    ax_time.set_xlim(0, total_frames)
    ax_time.set_ylim(0, 2.2)
    ax_time.set_xlabel("Frame Number (t)")
    ax_time.set_ylabel("Displacement In Meters (y)")
    ax_time.set_title("Entity Displacement (30 FPS)")
    ax_time.grid(True, linestyle="--", alpha=0.7)

    ax_time.plot(range(total_frames), true_displacement, label="True Displacement",
                 color="blue", linewidth=1)
    ax_time.plot(range(total_frames), discrete_displacement, label="Discrete Approximation",
                 color="red", linestyle="--", linewidth=1)
    ax_time.plot(range(total_frames), integrated_displacement, label="Integrated Average",
                 color="green", linestyle=":", linewidth=1)
    ax_time.axhline(y=wall_position, color="black", linestyle="-", linewidth=2, label="Wall at y=1")
    ax_time.legend(fontsize=9, loc="upper left")

    ax_time.text(20, 0.1, r"$y = t^2$", fontsize=10, color="blue")
    ax_time.text(10, 1.5, r"$y_{n+1} = y_n + v(t_n)\Delta t$", fontsize=10, color="red")
    ax_time.text(15, 0.7, r"$y = \frac{1}{1-0} \int_0^2 2\tau d\tau$", fontsize=10, color="green")

    marker_true_time, = ax_time.plot([], [], 'o', color="blue", markersize=5)
    marker_discrete_time, = ax_time.plot([], [], 'o', color="red", markersize=5)
    marker_integrated_time, = ax_time.plot([], [], 'o', color="green", markersize=5)

    ax_sim.set_xlim(0, 2.2)
    ax_sim.set_ylim(-0.5, 0.5)
    ax_sim.set_yticks([])
    ax_sim.set_xlabel("Displacement In Meters (x)")
    ax_sim.set_title("Entity Movement Simulation (30 FPS)")
    
    marker_true_sim, = ax_sim.plot([], [], 'o', color="blue", markersize=5, label="True Displacement")
    marker_discrete_sim, = ax_sim.plot([], [], 'o', color="red", markersize=5, label="Discrete Approximation")
    marker_integrated_sim, = ax_sim.plot([], [], 'o', color="green", markersize=5, label="Integrated Average")
    ax_sim.axvline(x=wall_position, color="black", linestyle="-", linewidth=2, label="Wall at x=1")
    ax_sim.grid(True, linestyle="--", alpha=0.7)

    ax_sim.legend(loc="upper right")

    def init():
        marker_true_time.set_data([], [])
        marker_discrete_time.set_data([], [])
        marker_integrated_time.set_data([], [])
        marker_true_sim.set_data([], [])
        marker_discrete_sim.set_data([], [])
        marker_integrated_sim.set_data([], [])
        return (marker_true_time, marker_discrete_time, marker_integrated_time,
                marker_true_sim, marker_discrete_sim, marker_integrated_sim)

    def update(frame):
        x_true_pos = min(true_displacement[frame], wall_position)
        x_discrete_pos = discrete_displacement[frame]
        x_integrated_pos = min(integrated_displacement[frame], wall_position)

        marker_true_time.set_data([frame], [x_true_pos])
        marker_discrete_time.set_data([frame], [x_discrete_pos])
        marker_integrated_time.set_data([frame], [x_integrated_pos])

        marker_true_sim.set_data([x_true_pos], [0.2])
        marker_discrete_sim.set_data([x_discrete_pos], [0])
        marker_integrated_sim.set_data([x_integrated_pos], [-0.2])

        return (marker_true_time, marker_discrete_time, marker_integrated_time,
                marker_true_sim, marker_discrete_sim, marker_integrated_sim)

    animation_obj = animation.FuncAnimation(
        fig, update, frames=total_frames,
        init_func=init, blit=True, interval=150
    )

    animation_obj.save("data.gif", writer="pillow", fps=5)

    plt.show()
