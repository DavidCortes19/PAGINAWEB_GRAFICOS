import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
  
# adjust figure and assign coordinates
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

pp0=plt.plot(1, 2, marker="o", color="red")
pp1 = plt.Rectangle((2, 10),6, 4 , color="green")
pp2 = plt.Circle((12, 7), radius=2)
pp3 = plt.Polygon([[8, 5],[3, 4],[5, 8]], color="yellow")
  
# depict illustrations
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.add_patch(pp3)
plt.ylim(0, 15)
plt.xlim(0, 15)
plt.title("Figuras geometricas")
plt.show()