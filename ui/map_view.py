from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

# Przykładowe dane – docelowo powinny pochodzić z pliku JSON lub klasy reprezentującej mapę
DISTRICTS = [
    ["Brass Hollow", "Cinderside", "Rust Market"],
    ["Gallows End", "Ivory Path", "Silence Ward"],
    ["Blackreach", "Fogway", "Thorn Alley"]
]

class MapView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        layout.setSpacing(10)
        self.setLayout(layout)

        for row_idx, row in enumerate(DISTRICTS):
            for col_idx, district_name in enumerate(row):
                button = QPushButton(district_name)
                button.setFixedSize(150, 80)
                button.clicked.connect(lambda checked, name=district_name: self.on_district_clicked(name))
                layout.addWidget(button, row_idx, col_idx)

    def on_district_clicked(self, district_name):
        print(f"Dzielnica kliknięta: {district_name}")
        # Tutaj może się pojawić np. otwarcie panelu dzielnicy, dialogu, itd.
