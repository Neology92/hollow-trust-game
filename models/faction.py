class Faction:
    def __init__(self, name, power, influence, relations):
        self.name = name
        self.power = power
        self.influence = influence
        self.relations = relations  # np. {'Police': -30, 'Iron Spikes': 40}
