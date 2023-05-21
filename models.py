from transitions import Machine

def on_input_received():
    print('Input received')

def on_start_processing():
    print('Processing started')

def on_processing_complete():
    print('Processing complete')

def on_processing_error():
    print('Error occurred')

def on_reset():
    print('Resetting')

def on_complete():
    print('Processing complete')

class GUI:
    states = ['initial', 'input', 'processing', 'output', 'error', 'final']
    transitions = [
        {'trigger': 'input_received', 'source': 'initial', 'dest': 'input'},
        {'trigger': 'start_processing', 'source': 'input', 'dest': 'processing'},
        {'trigger': 'processing_complete', 'source': 'processing', 'dest': 'output'},
        {'trigger': 'processing_error', 'source': ['input', 'processing'], 'dest': 'error'},
        {'trigger': 'reset', 'source': '*', 'dest': 'initial'},
        {'trigger': 'complete', 'source': 'output', 'dest': 'final'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=GUI.states, transitions=GUI.transitions, initial='initial')

gui = GUI()
gui.input_received()
gui.start_processing()
gui.processing_complete()
gui.complete()




