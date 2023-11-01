import sys, main, randomizer
from PySide6.QtCore import Qt, QRectF, Slot
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication


class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()

    def UI(self):
        
        available_geometry = self.screen().availableGeometry()
        size = available_geometry.height() * .7
        
        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QGridLayout(self.central_widget)

        
        # Create a QGraphicsView and QGraphicsScene
        scene = QGraphicsScene(self)
        view = QGraphicsView(scene)
        
        # Data representing bar heights
        bar_data = randomizer.numbers

        # Draw bars
        bar_width = 2
        x_pos = 50
        for height in bar_data:
            bar = QGraphicsRectItem(x_pos, self.height() - height, bar_width, height)
            bar.setBrush(Qt.magenta)  # Set bar color
            scene.addItem(bar)
            x_pos += bar_width + 2  # Add spacing between bars
        
        self.main_layout.addWidget(view)
        self.setLayout(self.main_layout)
        self.setWindowTitle("Sorting Visualizer")
        self.show()

