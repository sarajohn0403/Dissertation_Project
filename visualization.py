import matplotlib.pyplot as plt

# Example data
model_names = ['FSM', 'SMM']
number_of_states = [10, 15]
number_of_transitions = [20, 25]

# Bar chart - Number of States and Transitions
plt.figure(figsize=(8, 6))
plt.bar(model_names, number_of_states, label='Number of States')
plt.bar(model_names, number_of_transitions, label='Number of Transitions')
plt.xlabel('Model')
plt.ylabel('Count')
plt.title('Comparison of Number of States and Transitions')
plt.legend()
plt.show()

# Example data
scatter_states = [10, 12, 8, 15, 20]
scatter_transitions = [20, 18, 25, 22, 28]

# Scatter plot - Number of States vs. Number of Transitions
plt.figure(figsize=(8, 6))
plt.scatter(scatter_states, scatter_transitions)
plt.xlabel('Number of States')
plt.ylabel('Number of Transitions')
plt.title('Scatter Plot: Number of States vs. Number of Transitions')
plt.show()
