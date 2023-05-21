import numpy as np
import matplotlib.pyplot as plt

# data
model_names = ['FSM', 'SMM']
metrics = ['Number of States', 'Number of Transitions', 'Average Transition Length']
data = np.array([[10, 15],
                 [20, 25],
                 [5, 6]])

# Plotting the heatmap
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(data, cmap='YlGnBu')

# Set the axis labels
ax.set_xticks(np.arange(len(model_names)))
ax.set_yticks(np.arange(len(metrics)))
ax.set_xticklabels(model_names)
ax.set_yticklabels(metrics)

# Rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Metric Value", rotation=-90, va="bottom")

# Loop over data dimensions and add text annotations
for i in range(len(metrics)):
    for j in range(len(model_names)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="black")

# Set the title
ax.set_title("Comparison of Metrics - FSM vs. SMM")

# Display the heatmap
plt.show()
