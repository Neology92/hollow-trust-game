class DialogNode:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices  # {label: next_node}

class DialogSystem:
    def __init__(self, starting_node):
        self.current_node = starting_node

    def choose(self, label):
        if label in self.current_node.choices:
            self.current_node = self.current_node.choices[label]
        else:
            print("Nieznany wybór")
