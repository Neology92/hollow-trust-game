import random

class FactionAPI:
    def __init__(self, faction, all_factions):
        self.faction = faction
        self.all_factions = all_factions

    def take_turn(self):
        rival = random.choice(self.all_factions)
        if rival.name != self.faction.name:
            action = random.choice(["attack", "ally", "spy"])
            self.perform_action(rival, action)

    def perform_action(self, target, action):
        print(f"{self.faction.name} performs {action} on {target.name}")
        # logika wpływająca na relacje, moc, wpływy itd.
