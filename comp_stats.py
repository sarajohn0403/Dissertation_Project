from scipy.stats import ttest_ind

# Data sample
fsm_states = [4, 5, 6, 4, 5]
smm_states = [4, 4, 5, 5, 5]

# Perform independent t-test
t_statistic, p_value = ttest_ind(fsm_states, smm_states)

# Print the results
print("Independent t-test")
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")
