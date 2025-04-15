from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class CharacterPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Postać:"))
        # W przyszłości: dynamiczne dane z obiektów Character
        self.setLayout(layout)
