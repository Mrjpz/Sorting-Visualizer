import sys, main, randomizer, time
from PySide6.QtCore import Qt, QRectF, Slot, QTimer
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication


class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()
    
    
    def drawbars(self, bar_data):
        self.scene.clear()
        # Draw bars
        bar_width = 2
        x_pos = 50
        for height in self.bar_data:
            bar = QGraphicsRectItem(x_pos, self.height() - height, bar_width, height)
            bar.setBrush(Qt.white)  # Set bar color
            self.scene.addItem(bar)
            x_pos += bar_width + 1  # Add spacing between bars
    
        
    def UI(self):
        available_geometry = self.screen().availableGeometry()
        size = available_geometry.height() * .7
        
        
        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QGridLayout(self.central_widget)
        
        # Create a QGraphicsView and QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.black)
        self.view = QGraphicsView(self.scene)
        
        # Create button for algorithm
        self.quicksort = QPushButton("Quicksort")
        self.quicksort.clicked.connect(self.sort)
        self.main_layout.addWidget(self.quicksort)
        
        
        # Data representing bar heights
        self.bar_data = randomizer.numbers
        
        self.drawbars(self.bar_data)
        
        self.main_layout.addWidget(self.view)
        self.setLayout(self.main_layout)
        self.setWindowTitle("Sorting Visualizer")
        self.show()
        
        #print(bar_data)
        

        
    @Slot(str)
    def sort(self, text):
        button =  self.sender()
        text = button.text()
        self.timer = QTimer(self)
        self.timer.start(0)
        if text == "Quicksort":
            n = len(self.bar_data)

            # Outer loop for traversing the entire list
            for i in range(n):
                # Flag to optimize the sorting process, if no swaps are made, the list is already sorted
                swapped = False
    
                # Inner loop for pairwise comparison and swapping
                for j in range(0, n - i - 1):
                    # Swap if the element found is greater than the next element
                    if self.bar_data[j] > self.bar_data[j + 1]:
                        self.bar_data[j], self.bar_data[j + 1] = self.bar_data[j + 1], self.bar_data[j]
                        swapped = True
                        #print(self.bar_data)
                self.scene.clear()
                self.drawbars(self.bar_data)
                QApplication.processEvents()
                # If no two elements were swapped in the inner loop, the list is already sorted
                if not swapped:
                    break
                    
                    
            
            print('done')
            self.timer.stop()