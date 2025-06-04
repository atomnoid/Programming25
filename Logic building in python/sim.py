import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.cosmology import Planck18 as cosmo
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constants
H0 = cosmo.H0.value  # Hubble constant (km/s/Mpc)
G = 4.3e-9  # Gravitational constant in (Mpc⋅(km/s)^2) / M_sun
num_galaxies = 200  # Number of galaxies
box_size = 1000  # Mpc (simulation volume)

# Initialize galaxy positions randomly
np.random.seed(42)
positions = np.random.uniform(-box_size / 2, box_size / 2, (num_galaxies, 3))
masses = np.random.uniform(1e10, 1e12, num_galaxies)  # Solar masses

# Initialize velocities using Hubble Flow
velocities = (H0 / 1e3) * positions  # Hubble Flow in Mpc/s

# Time step (1 million years per step)
dt = 1e6 * 3.154e7  # seconds
num_steps = 200

# Simulation loop
def update(frame):
    global positions, velocities

    # Compute pairwise distances and gravitational force
    acc = np.zeros_like(positions)
    for i in range(num_galaxies):
        diff = positions - positions[i]
        r = np.linalg.norm(diff, axis=1) + 1e-3  # Avoid division by zero
        force = G * masses[i] * masses[:, None] * diff / r[:, None]**3
        acc[i] = np.sum(force, axis=0) / masses[i]

    # Update velocities and positions
    velocities += acc * dt  # v = v0 + at
    positions += velocities * dt / (3.086e19)  # Convert seconds to Mpc

    # Apply Hubble expansion
    velocities += (H0 / 1e3) * positions * dt

    # Update plot
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='cyan', s=10)
    ax.set_xlim(-box_size / 2, box_size / 2)
    ax.set_ylim(-box_size / 2, box_size / 2)
    ax.set_zlim(-box_size / 2, box_size / 2)
    ax.set_title(f"Cosmological Simulation - Step {frame+1}")
    ax.set_xlabel('X (Mpc)')
    ax.set_ylabel('Y (Mpc)')
    ax.set_zlabel('Z (Mpc)')

# Visualization
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=50)
plt.show()
