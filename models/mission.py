class Mission:
    def __init__(self, title, danger, reward, required_skills):
        self.title = title
        self.danger = danger
        self.reward = reward
        self.required_skills = required_skills
        self.assigned = []
