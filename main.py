import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Fonction pour dessiner l'horloge
def draw_clock(ax, hour_angle, minute_angle, second_angle):
    ax.clear()

    # Dessiner le cadran
    circle = plt.Circle((0, 0), 1, edgecolor="black", facecolor="white", lw=2)
    ax.add_artist(circle)
    
    # Marquer les heures
    for i in range(12):
        angle = np.deg2rad(i * 30)  # 30° entre chaque heure
        x1, y1 = 0.85 * np.sin(angle), 0.85 * np.cos(angle)
        x2, y2 = 1 * np.sin(angle), 1 * np.cos(angle)
        ax.plot([x1, x2], [y1, y2], color="black", lw=3)
    
    # Dessiner les aiguilles
    def draw_hand(angle, length, color, width):
        x = length * np.sin(np.deg2rad(angle))
        y = length * np.cos(np.deg2rad(angle))
        ax.plot([0, x], [0, y], color=color, linewidth=width, solid_capstyle='round')

    draw_hand(hour_angle, 0.5, "blue", 4)  # Aiguille des heures
    draw_hand(minute_angle, 0.7, "green", 3)  # Aiguille des minutes
    draw_hand(second_angle, 0.9, "red", 2)  # Aiguille des secondes
    
    # Ajuster les axes
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis("off")

# Fonction de mise à jour pour l'animation
def update(frame):
    # Accélération : chaque frame avance de 10 secondes
    seconds = frame * 10
    hours = (seconds // 3600) % 12
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    # Calcul des angles
    hour_angle = 30 * hours + minutes * 0.5
    minute_angle = 6 * minutes + seconds * 0.1
    second_angle = 6 * seconds

    draw_clock(ax, hour_angle, minute_angle, second_angle)

# Création de la figure et animation
fig, ax = plt.subplots(figsize=(6, 6))

ani = animation.FuncAnimation(fig, update, frames=360, interval=50)

ani.save("horloge_animation.gif", writer="ffmpeg", fps=30)

plt.show()
