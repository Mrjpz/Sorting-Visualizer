import sys, main, randomizer, time
from PySide6.QtCore import Qt, QRectF, Slot, Signal, QTimer, QThread
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication, QSizePolicy

class WorkerThread(QThread):
    refresh_screen_signal = Signal(list) 
    stop_sorting_signal = Signal(bool)
    def __init__(self, text, bar_data):
        super().__init__()
        self.text = text
        self.bar_data = bar_data
    
    def run(self): 
        if self.text == 'Merge Sort':           
            
    
            def merge_sort(lst):
                if len(lst) > 1:   
                    mid = len(lst) // 2
                    L = lst[:mid]
                    R = lst[mid:]
                
                    merge_sort(L)
                    merge_sort(R)
                    
                
                    i = j = k = 0
                
                    while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                            lst[k] = L[i]
                            i += 1
                        else:
                            lst[k] = R[j]
                            j += 1
                        k += 1
                        
                        
                    
                    
                    
                        
                    while i < len(L):
                        lst[k] = L[i]
                        i += 1
                        k += 1
                        
                        
                    while j < len(R):
                        lst[k] = R[j]
                        j += 1
                        k += 1
                        
                    
                
            merge_sort(self.bar_data)
            
            
            print(self.bar_data,'done')
            
        #if self.text == 'Heap Sort':
        
        if self.text == "Bubble Sort":
            
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
                
                self.refresh_screen_signal.emit(self.bar_data.copy())  # Emit the signal
                time.sleep(0.05)
                
                # If no two elements were swapped in the inner loop, the list is already sorted
                if not swapped:
                    self.completed = True
                    self.refresh_screen_signal.emit(self.bar_data.copy())
                    time.sleep(0.05)
                    break
                '''elif self.stop == True:
                    break'''
            print("done")
        
        
        #if self.text == 'Quick Sort':
        #if self.text == 'Insertation Sort':
        #if self.text == 'Selection Sort':
        
        
        
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
            if self.completed == True:
                bar.setBrush(Qt.green)
            else:
                bar.setBrush(Qt.white)
            self.scene.addItem(bar)
            x_pos += bar_width + 1  # Add spacing between bars
            
            
        # Set the scene rect to match the drawn bars
        self.scene.setSceneRect(0, 175, x_pos, max_height)#horizontal offset, verticle offset, start of the list, max hight of the window
        
        
    
        
    def UI(self):
        available_geometry = self.screen().availableGeometry()
        size = available_geometry.height() * .7
        self.completed = False

        
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
        self.randomize = QPushButton("Randomize List")
        self.mergesort = QPushButton("Merge Sort")
        self.heapsort = QPushButton("Heap Sort")
        self.bubblesort = QPushButton("Bubble Sort")
        self.quicksort = QPushButton("Quick Sort")
        self.insertationsort = QPushButton("Insertation Sort")
        self.selectionsort = QPushButton("Selection Sort")


        # Button click action
        self.settings.clicked.connect(self.settings_menu)
        self.randomize.clicked.connect(self.randomizer)
        self.mergesort.clicked.connect(self.sort)
        self.heapsort.clicked.connect(self.sort)
        self.bubblesort.clicked.connect(self.sort)
        self.quicksort.clicked.connect(self.sort)
        self.insertationsort.clicked.connect(self.sort)
        self.selectionsort.clicked.connect(self.sort)
        
        # Add buttons to the layout
        self.main_layout.addWidget(self.settings, 0, 0)
        self.main_layout.addWidget(self.randomize, 0, 0)
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
    def refresh_screen(self, bar_data):
            self.drawbars(self.bar_data)
            QApplication.processEvents()
            
            
    def sort(self, text):
   
        button =  self.sender()
        text = button.text()
        self.stop = False
        self.worker_thread = WorkerThread(text, self.bar_data)
        self.worker_thread.refresh_screen_signal.connect(self.refresh_screen)
        self.worker_thread.stop_sorting_signal.connect(self.randomizer)
        self.worker_thread.start()
        
        
    
    def settings_menu(self):  
        print("work")
        
        
        
        
        
        
        
        
        
        
        print('end')
        
    def randomizer(self):
        self.stop = True
        self.completed = False
        randomizer.random.shuffle(self.bar_data)
        self.drawbars(self.bar_data)
        QApplication.processEvents()
       