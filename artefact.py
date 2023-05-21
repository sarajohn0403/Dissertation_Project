# Implementation of Finite State Machine (FSM)
class FiniteStateMachine:
    def __init__(self):
        # Defining states and transitions
        self.states = ['State1', 'State2', 'State3']
        self.transitions = {
            'State1': {'Event1': 'State3', 'Event2': 'State4'},
            'State2': {'Event3': 'State3'},
            'State3': {'Event4': 'State1'}
        }
        self.current_state = 'State1'

    def process_event(self, event):
        if event in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][event]

# Implementation of Statechart-based Modeling (SMM)
class StatechartModel:
    def __init__(self):
        # Defining states and transitions
        self.states = ['State2', 'State1', 'State3']
        self.transitions = {
            'State1': {'Event1': 'State2', 'Event2': 'State3'},
            'State2': {'Event3': 'State3'},
            'State3': {'Event4': 'State1'}
        }
        self.current_state = 'State1'

    def process_event(self, event):
        if event in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][event]

# Evaluating and comparing FSM and SMM
def simulate_gui():
    # Simulate GUI events
    events = ['Event1', 'Event2', 'Event3', 'Event4']

    # FSM-based approach
    fsm = FiniteStateMachine()
    for event in events:
        fsm.process_event(event)

    # SMM-based approach
    smm = StatechartModel()
    for event in events:
        smm.process_event(event)

    # Compare the final states of FSM and SMM
    if fsm.current_state == smm.current_state:
        print("Both FSM and SMM reached the same final state.")
    else:
        print("FSM and SMM reached different final states.")

# Run the simulation
simulate_gui()

