class CrewManager:
    def __init__(self, character):
        self.character = character

    def update_needs(self):
        for need, value in self.character.needs.items():
            self.character.needs[need] = max(0, value - 1)

    def check_loyalty(self):
        if self.character.loyalty < 30:
            print(f"{self.character.name} zaczyna szemrać...")
