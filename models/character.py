class Character:
    def __init__(self, name, loyalty, skills, needs):
        self.name = name
        self.loyalty = loyalty
        self.skills = skills  # np. {'stealth': 3, 'negotiation': 5}
        self.needs = needs    # np. {'money': 100, 'safety': 70}
        self.available = True