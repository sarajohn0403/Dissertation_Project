# Define the State class
class State:
    def __init__(self, name):
        self.name = name

# Define the Transition class
class Transition:
    def __init__(self, event, source, target):
        self.event = event
        self.source = source
        self.target = target

# Define the FSM model for the social media profile scenario
def create_fsm_model():
    # Define states
    initial_state = State("Initial")
    login_state = State("Login")
    profile_state = State("Profile")
    edit_profile_state = State("Edit Profile")

    # Define transitions
    transitions = [
        Transition("Login", initial_state, login_state),
        Transition("View Profile", login_state, profile_state),
        Transition("Edit Profile", profile_state, edit_profile_state),
        Transition("Save Profile", edit_profile_state, profile_state)
    ]

    # Create FSM model
    finite_model = {
        "states": [initial_state, login_state, profile_state, edit_profile_state],
        "transitions": transitions
    }
    return finite_model

# Define the SMM model for the social media profile scenario
def create_smm_model():
    # Define states
    initial_state = State("Initial")
    login_state = State("Login")
    profile_state = State("Profile")
    edit_profile_state = State("Edit Profile")

    # Define transitions
    transitions = [
        Transition("Login", initial_state, login_state),
        Transition("View Profile", login_state, profile_state),
        Transition("Edit Profile", profile_state, edit_profile_state),
        Transition("Save Profile", edit_profile_state, profile_state)
    ]

    # Create SMM model
    state_model = {
        "states": [initial_state, login_state, profile_state, edit_profile_state],
        "transitions": transitions
    }
    return state_model

# Function to calculate quantitative metrics for a given model
def calculate_metrics(model):
    num_states = len(model["states"])
    num_transitions = len(model["transitions"])
    avg_transition_length = num_states / num_transitions
    max_state_depth = calculate_max_state_depth(model["states"])

    return num_states, num_transitions, avg_transition_length, max_state_depth

# Function to calculate the maximum depth of state hierarchies in a given list of states
def calculate_max_state_depth(states):
    max_depth = 0

    for state in states:
        depth = calculate_state_depth(state, 0)
        max_depth = max(max_depth, depth)

    return max_depth

# Helper function to calculate the depth of a state within the state hierarchy
def calculate_state_depth(state, current_depth):
    if not hasattr(state, "substates"):
        return current_depth

    max_substate_depth = 0

    for substate in state.substates:
        substate_depth = calculate_state_depth(substate, current_depth + 1)
        max_substate_depth = max(max_substate_depth, substate_depth)

    return max_substate_depth

# Function to display the quantitative metrics
def display_metrics(num_states, num_transitions, avg_transition_length, max_state_depth):
    print("Quantitative Metrics:")
    print("Number of States:", num_states)
    print("Number of Transitions:", num_transitions)
    print("Average Length of Transitions:", avg_transition_length)
    print("Maximum Depth of State Hierarchies:", max_state_depth)

# Create the FSM model for the social media profile scenario
fsm_model = create_fsm_model()

# Create the SMM model for the social media profile scenario
smm_model = create_smm_model()

# Calculate metrics for the FSM model
fsm_metrics = calculate_metrics(fsm_model)

# Calculate metrics for the SMM model
smm_metrics = calculate_metrics(smm_model)

# Display metrics for the FSM model
print("FSM Model Metrics:")
display_metrics(*fsm_metrics)
print()

# Display metrics for the SMM model
print("SMM Model Metrics:")
display_metrics(*smm_metrics)
