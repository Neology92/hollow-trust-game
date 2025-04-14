from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Gang Manager")
window.setMinimumSize(300, 200)

# --- Fullscreen functionality ---

normal_window_geometry = None
def showNormal():
    global normal_window_geometry
    window.showNormal()
    if normal_window_geometry:
        window.setGeometry(normal_window_geometry)
    
    

def showFullScreen():
    global normal_window_geometry 
    normal_window_geometry = window.geometry()
    window.showFullScreen()

    

def toggleFullScreen():
    print("Toggling fullscreen")
    if window.isFullScreen():
        showNormal()
    else:
        showFullScreen()


setFullscreen = QtWidgets.QAction("&Fullscreen", window)
setFullscreen.setShortcut("F11")
setFullscreen.setStatusTip("Change to fullscreen mode")
setFullscreen.triggered.connect(toggleFullScreen)

# Add the action to a menu bar
menuBar = QtWidgets.QMenuBar(window)
viewMenu = menuBar.addMenu("&View")
viewMenu.addAction(setFullscreen)


# ---


def send_on_mission():
    label.setText("Wysłano członka na misję!")

layout = QtWidgets.QVBoxLayout()

button = QtWidgets.QPushButton("Wyślij na misję")
button.setGeometry(50, 50, 200, 50)

button.setStyleSheet("""
    QPushButton {
        background-color: #8B0000;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #A52A2A;
    }
    QPushButton:pressed {
        background-color: #5A0000;
    }
""")

button2 = QtWidgets.QPushButton("Anuluj misję")
button2.setGeometry(50, 120, 200, 50)

button.clicked.connect(send_on_mission)

label = QtWidgets.QLabel("Stan: gotowy")

layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())




