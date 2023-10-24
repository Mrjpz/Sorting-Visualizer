import sys
import visualizer
from randomizer import numbers
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit




if __name__ == '__main__':
    
    application = QApplication(sys.argv)
    
    window = visualizer.Visualizer()
    window.show()
    window.resize(1920, 1080)
    
    
    sys.exit(application.exec())