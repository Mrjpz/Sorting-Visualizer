
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit



class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        
        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.setLayout(layout)
        
        self.setWindowTitle("Sorting Visualizer")
        self.show()
