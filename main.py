import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == '__main__':
    t_vals = np.linspace(0, 1, 100)
    x_true = t_vals**2
    x_discrete = 2 * t_vals
    x_integrated = 1 * t_vals
    wall_x = 1.0
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    plt.subplots_adjust(hspace=0.5)

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 2.2)
    ax1.set_xlabel("Time (Seconds)")
    ax1.set_ylabel("Displacement (Meters)")
    ax1.set_title("Entity Displacement: Discrete vs Integration")
    ax1.grid(True, linestyle="--", alpha=0.7)

    ax1.plot(t_vals, x_true, label="True Displacement",
             color="blue", linewidth=2)
    ax1.plot(t_vals, x_discrete, label="Discreted Average",
             color="orange", linestyle="--", linewidth=1.8)
    ax1.plot(t_vals, x_integrated, label="Integrated Average",
             color="red", linestyle=":", linewidth=1.8)
    ax1.legend(fontsize=9, loc="upper left")

    ax1.text(0.55, 0.1,
        r"$x(t) = t^2$",
        fontsize=10, color="blue",
        ha="left", va="bottom")
    ax1.text(0.50, 1.5,
        r"$x_{n+1} = x_n + v(t_n)\Delta t$",
        fontsize=10, color="orange",
        ha="left", va="bottom")
    ax1.text(0.55, 0.7,
        r"$\bar{v} = \frac{1}{1-0}\int_0^1 2\tau \, d\tau$",
        fontsize=10, color="red",
        ha="left", va="bottom")

    true_car1, = ax1.plot([], [], 'o', color="blue", markersize=10)
    discrete_car1, = ax1.plot([], [], 'o', color="orange", markersize=10)
    integrated_car1, = ax1.plot([], [], 'o', color="red", markersize=10)

    ax2.set_xlim(0, 2.2)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_yticks([])
    ax2.set_xlabel("Displacement (Meters)")
    ax2.set_title("Entity Movement Simulation: Discrete vs Integration")

    ax2.axvline(x=wall_x, color="black", linestyle="--", linewidth=2, label="Wall at x=1")

    true_car2, = ax2.plot([], [], 'o', color="blue", markersize=10, label="True Displacement")
    discrete_car2, = ax2.plot([], [], 'o', color="orange", markersize=10, label="Discreted Average")
    integrated_car2, = ax2.plot([], [], 'o', color="red", markersize=10, label="Integrated Average")

    ax2.legend(loc="upper right")

    def init():
        true_car1.set_data([], [])
        discrete_car1.set_data([], [])
        integrated_car1.set_data([], [])

        true_car2.set_data([], [])
        discrete_car2.set_data([], [])
        integrated_car2.set_data([], [])
        return true_car1, discrete_car1, integrated_car1, true_car2, discrete_car2, integrated_car2

    def update(frame):
        t = t_vals[frame]

        true_car1.set_data([t], [x_true[frame]])
        discrete_car1.set_data([t], [x_discrete[frame]])
        integrated_car1.set_data([t], [x_integrated[frame]])

        xt = min(x_true[frame], wall_x)
        true_car2.set_data([xt], [0.2])

        xd = x_discrete[frame]
        discrete_car2.set_data([xd], [0])

        xi = min(x_integrated[frame], wall_x)
        integrated_car2.set_data([xi], [-0.2])

        return true_car1, discrete_car1, integrated_car1, true_car2, discrete_car2, integrated_car2

    ani = animation.FuncAnimation(
        fig, update, frames=len(t_vals),
        init_func=init, blit=True, interval=50
    )

    ani.save("data.gif", writer="pillow", fps=60)
    plt.show()
