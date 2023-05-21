import numpy as np
import pandas as pd

# metrics data
number_of_states = [4, 4]
number_of_transitions = [6, 8]
average_transition_length = [1.5, 1.8]
maximum_depth_of_state_hierarchies = [2, 3]

# DataFrame created to store the metrics
metrics_df = pd.DataFrame({
    'Number of States': number_of_states,
    'Number of Transitions': number_of_transitions,
    'Average Transition Length': average_transition_length,
    'Maximum Depth of State Hierarchies': maximum_depth_of_state_hierarchies })

# Calculate descriptive statistics
descriptive_stats = metrics_df.describe()

# Print the descriptive statistics
print(descriptive_stats)
