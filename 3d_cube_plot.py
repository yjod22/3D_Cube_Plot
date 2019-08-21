import matplotlib.pyplot as plt
import numpy as np
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Set the sizes of the coordinates
x, y, z = 16, 16, 16

# Generate the basic array which is randomly filled with 0 or 1
cube = np.random.randint(2, size=x * y * z)

# Set the color array
colors = np.zeros(cube.shape + (3,))
for idx, val in enumerate(cube):
    if val == 1:
        randNumR = np.random.rand(1)
        randNumG = np.random.rand(1)
        randNumB = np.random.rand(1)
        colors[idx, 0] = randNumR
        colors[idx, 1] = randNumG
        colors[idx, 2] = randNumB
    else:
        pass

# Reshape the basic array to 3D
cube_3D = cube.reshape((x, y, z))

# Replace 0, 1 with False, True
cube_3D = cube_3D > 0

# Reshape the color array to 4D
colors_4D = colors.reshape((x, y, z, 3))

# Plot everything
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(cube_3D, facecolors=colors_4D, edgecolors='white', linewidth=0.5)
plt.show()
