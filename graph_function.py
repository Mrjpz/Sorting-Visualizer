import sys, main, randomizer, time
from PySide6.QtCore import Qt, QRectF, Slot, Signal, QTimer, QThread
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication, QSizePolicy

class WorkerThread(QThread):
    drawbars_emit = Signal(list) 
    stop_sorting_signal = Signal(bool)
    
    def __init__(self, text, bar_data):
        super().__init__()
        self.text = text
        self.bar_data = bar_data
        
    stop = False
    def run(self): 
        n = len(self.bar_data)
        
        def refresh_screen(self, bar_data):
            self.drawbars_emit.emit(self.bar_data)
            QApplication.processEvents()
            #might not even need this funciton 
        
        
        if self.text == 'Merge Sort':           
            
   
            def merge(arr, l, m, r):
                n1 = m - l + 1
                n2 = r - m
    
    # Create temporary arrays
                L = arr[l:l + n1]
                R = arr[m + 1:m + 1 + n2]
    
    # Merge the temporary arrays back into arr[l..r]
                i = j = 0
                k = l
    
                while i < n1 and j < n2:
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                self.drawbars_emit.emit(self.bar_data)
                QApplication.processEvents()
                time.sleep(.05)
    # Copy the remaining elements of L[], if any
                while i < n1:
                    arr[k] = L[i]
                    i += 1
                    k += 1
    
    # Copy the remaining elements of R[], if any
                while j < n2:
                    arr[k] = R[j]
                    j += 1
                    k += 1

            def merge_sort(arr, l, r):
                if l < r:
        # Find the middle point to divide the array into two halves
                    m = (l + r) // 2
        
        # Call merge_sort() for each half
                    merge_sort(arr, l, m)
                    merge_sort(arr, m + 1, r)
        
        # Merge the two halves
                    merge(arr, l, m, r)
                    self.drawbars_emit.emit(self.bar_data)
                    QApplication.processEvents()
                    time.sleep(.05)


            
            n = len(self.bar_data)
            merge_sort(self.bar_data, 0, n - 1)
            print("Sorted array is:", self.bar_data)

            
        #if self.text == 'Heap Sort':
        
        if self.text == "Bubble Sort":
            

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
                
                self.drawbars_emit.emit(self.bar_data)
                QApplication.processEvents()
                time.sleep(.05)
            
                # If no two elements were swapped in the inner loop, the list is already sorted
                if not swapped:
                    self.completed = True
                    break
                if self.stop:
                    self.stop = False
                    break
                    
            print("done")
        
        
        #if self.text == 'Quick Sort':
        if self.text == 'Insertation Sort':
            cont = True
            if n <= 1:
                cont = False  # If the array has 0 or 1 element, it is already sorted, so return
 
            for i in range(1, n):  # Iterate over the array starting from the second element
                key = self.bar_data[i]  # Store the current element as the key to be inserted in the right position
                j = i-1
                while j >= 0 and key < self.bar_data[j]:  # Move elements greater than key one position ahead
                    self.bar_data[j+1] = self.bar_data[j]  # Shift elements to the right
                    j -= 1
                self.bar_data[j+1] = key  # Insert the key in the correct position
                
                self.drawbars_emit.emit(self.bar_data)
                QApplication.processEvents()
                time.sleep(.05)
                
                if cont == False:
                    break
                
        #if self.text == 'Selection Sort':
        #if self.text == 'Radix Sort':
        if self.text == 'Randomize List':
            print('front')
            self.stop = True
            print(self.stop)
            self.completed = False
            randomizer.random.shuffle(self.bar_data)
            self.drawbars_emit.emit(self.bar_data)
            QApplication.processEvents()
            print('end')
        
        
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
                bar.setBrush(QBrush(Qt.green))
            else:
                bar.setBrush(QBrush(Qt.white))
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
        self.randomize.clicked.connect(self.sort)
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
            
            
    def sort(self, text):
   
        button =  self.sender()
        text = button.text()
        self.worker_thread = WorkerThread(text, self.bar_data)
        self.worker_thread.drawbars_emit.connect(self.drawbars)
        self.worker_thread.start()
        
        
    
    def settings_menu(self):  
        print("work")
        
        
        
        
        
        
        
        
        
        
        print('end')
        
    
       
       
       
       
