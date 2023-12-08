import sys, main, randomizer, time
from PySide6.QtCore import Qt, QRectF, Slot, QTimer
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication, QSizePolicy


class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()
    
    def drawbars(self, bar_data):
        self.scene.clear()
        # Draw bars
        bar_width = 2
        x_pos = 0
        max_height = max(bar_data)
    
        for height in bar_data:
            bar = QGraphicsRectItem(x_pos, 0, bar_width, height * 1.59)
            bar.setBrush(Qt.white)  # Set bar color
            self.scene.addItem(bar)
            x_pos += bar_width + 1  # Add spacing between bars
            
        # Set the scene rect to match the drawn bars
        self.scene.setSceneRect(0, 175, x_pos, max_height)#horizontal offset, verticle offset, start of the list, max hight of the window
        
        
    
        
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
        self.view.scale(1, -1)
        
        # Create buttons
        self.settings = QPushButton("Settings")
        self.mergesort = QPushButton("Merge Sort")
        self.heapsort = QPushButton("Heap Sort")
        self.bubblesort = QPushButton("Bubble Sort")
        self.quicksort = QPushButton("Quick Sort")
        self.insertationsort = QPushButton("Insertation Sort")
        self.selectionsort = QPushButton("Selection Sort")


        # Button click action
        self.settings.clicked.connect(self.settings_menu)
        self.mergesort.clicked.connect(self.sort)
        self.heapsort.clicked.connect(self.sort)
        self.bubblesort.clicked.connect(self.sort)
        self.quicksort.clicked.connect(self.sort)
        self.insertationsort.clicked.connect(self.sort)
        self.selectionsort.clicked.connect(self.sort)
        
        # Add buttons to the layout
        self.main_layout.addWidget(self.settings, 0, 0)
        self.main_layout.addWidget(self.mergesort, 0, 1)
        self.main_layout.addWidget(self.heapsort, 0, 2)
        self.main_layout.addWidget(self.bubblesort, 1, 1)
        self.main_layout.addWidget(self.quicksort, 1, 2)
        self.main_layout.addWidget(self.insertationsort, 2, 1)
        self.main_layout.addWidget(self.selectionsort, 2, 2)
        
        
        
        
        # Data representing bar heights
        self.bar_data = randomizer.numbers
        
        self.drawbars(self.bar_data)
        
        self.main_layout.addWidget(self.view, 1, 0)
        
        self.setLayout(self.main_layout)
        self.setWindowTitle("Sorting Visualizer")
        self.show()
        
        #print(bar_data)
        

        
    @Slot(str)
    def sort(self, text):
        
        def refresh_screen(self, bar_data):
            self.drawbars(self.bar_data)
            QApplication.processEvents()
            
        
        button =  self.sender()
        text = button.text()

        
        if text == 'Merge Sort':           
            while len(self.bar_data) > 1:
               
                n = len(self.bar_data)
            
                mid = n // 2
                L = self.bar_data[:mid]
                R = self.bar_data[mid:]
            
            
                print('done')
        
        #if text == 'Heap Sort':
        
        if text == "Bubble Sort":
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
                refresh_screen(self, self.bar_data)
                # If no two elements were swapped in the inner loop, the list is already sorted
                if not swapped:
                    break
            print("done")        
        
        
        #if text == 'Quick Sort':
        #if text == 'Insertation Sort':
        #if text == 'Selection Sort':
            
    
    def settings_menu(self):  
        print("work")
        
        
        
        
        
        
        
        
        
        
        print('end')
        
    