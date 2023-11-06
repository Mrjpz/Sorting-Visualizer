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
        scene.setBackgroundBrush(Qt.black)
        view = QGraphicsView(scene)
        
        # Create button for algorithm
        self.quicksort = QPushButton("Quicksort")
        self.quicksort.clicked.connect(self.sort)
        self.main_layout.addWidget(self.quicksort)
        
        
        # Data representing bar heights
        self.bar_data = randomizer.numbers
        
        # Draw bars
        bar_width = 2
        x_pos = 50
        for height in self.bar_data:
            bar = QGraphicsRectItem(x_pos, self.height() - height, bar_width, height)
            bar.setBrush(Qt.white)  # Set bar color
            scene.addItem(bar)
            x_pos += bar_width + 1  # Add spacing between bars
        
        self.main_layout.addWidget(view)
        self.setLayout(self.main_layout)
        self.setWindowTitle("Sorting Visualizer")
        self.show()
        
        #print(bar_data)
    @Slot(str)
    def sort(self, text):
        button =  self.sender()
        text = button.text()
        b = 0
        if text == "Quicksort":
            for i in range(len(self.bar_data)-b-1):
                print(i)
                del self.bar_data[i]
                b += 1
                