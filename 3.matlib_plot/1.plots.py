import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.title("Figure 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#--------------------------------------------------------------------------------
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.title("Figure 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#--------------------------------------------------------------------------------

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.title("Figure 3")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#--------------------------------------------------------------------------------

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.title("Figure 4")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#--------------------------------------------------------------------------------

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.title("Figure 5")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#---------------------------------------------------------------------------------
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.title("Figure 6")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#---------------------------------------------------------------------------------
plt.plot(ypoints, linestyle = 'dotted')
plt.title("Figure 7")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#---------------------------------------------------------------------------------
plt.plot(ypoints, linestyle = 'dashed')
plt.title("Figure 8")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#---------------------------------------------------------------------------------
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Figure 9: Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
#---------------------------------------------------------------------------------