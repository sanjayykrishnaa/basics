import matplotlib.pyplot as plt
import numpy as np

# Create a single figure with multiple subplots
fig, axs = plt.subplots(4, 2, figsize=(10, 10))

# Plot the first subplot
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
axs[0, 0].plot(xpoints, ypoints)
axs[0, 0].set_title("Plot 1")

# Plot the second subplot
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
axs[0, 1].plot(xpoints, ypoints)
axs[0, 1].set_title("Plot 2")

# Plot the third subplot
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
axs[1, 0].plot(xpoints, ypoints, 'o')
axs[1, 0].set_title("Plot 3")

# Plot the fourth subplot
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
axs[1, 1].plot(xpoints, ypoints)
axs[1, 1].set_title("Plot 4")

# Plot the fifth subplot
ypoints = np.array([3, 8, 1, 10, 5, 7])
axs[2, 0].plot(ypoints)
axs[2, 0].set_title("Plot 5")

# Plot the sixth subplot
ypoints = np.array([3, 8, 1, 10])
axs[2, 1].plot(ypoints, marker='o')
axs[2, 1].set_title("Plot 6")

# Plot the seventh subplot
axs[3, 0].plot(ypoints, linestyle='dotted')
axs[3, 0].set_title("Plot 7")

# Plot the eighth subplot
axs[3, 1].plot(ypoints, linestyle='dashed')
axs[3, 1].set_title("Plot 8")

# Set the overall title for the figure
fig.suptitle("Multiple Plots")

# Adjust the spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
