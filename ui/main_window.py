from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QAction, QMenuBar
from ui.map_view import MapView
from ui.character_panel import CharacterPanel

class MainWindow(QMainWindow):
    normal_window_geometry = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hollow Trust")
        self.setGeometry(100, 100, 1200, 800)
        normal_window_geometry = self.geometry()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout.addWidget(MapView())
        layout.addWidget(CharacterPanel())
        self.central_widget.setLayout(layout)


        
        setFullscreen = QAction("&Fullscreen", self)
        setFullscreen.setShortcut("F11")
        setFullscreen.setStatusTip("Change to fullscreen mode")
        setFullscreen.triggered.connect(self.toggleFullScreen)

        # Add the action to a menu bar
        menuBar = QMenuBar(self)
        viewMenu = menuBar.addMenu("&View")
        viewMenu.addAction(setFullscreen)



    def show(self):
        return super().show()
    

    # --- Fullscreen functionality ---


    def showNormal(self):
        super().showNormal()
        if self.normal_window_geometry:
            self.setGeometry(self.normal_window_geometry)
        
        

    def showFullScreen(self):
        self.normal_window_geometry = self.geometry()
        super().showFullScreen()

        

    def toggleFullScreen(self):
        print("Toggling fullscreen")
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
