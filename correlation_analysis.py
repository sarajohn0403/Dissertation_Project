import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# metrics data
number_of_states = [4, 5, 6, 4, 5]
number_of_transitions = [6, 8, 9, 6, 7]
average_transition_length = [1.5, 1.8, 1.7, 1.6, 1.7]
maximum_depth_of_state_hierarchies = [2, 3, 2, 3, 2]

# Create a DataFrame to store the metrics
metrics_df = pd.DataFrame({
    'States': number_of_states,
    'Transitions': number_of_transitions,
    'Avg Transition': average_transition_length,
    'Hierarchies': maximum_depth_of_state_hierarchies
})

# Calculate correlation matrix
correlation_matrix = metrics_df.corr()

# Print correlation matrix
print(correlation_matrix)

# Visualize correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
