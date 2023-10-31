import sys, graph_function
from randomizer import numbers
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = graph_function.Visualizer()
    available_geometry = w.screen().availableGeometry()
    size = available_geometry.height() * .80
    w.setFixedSize(size, size)
    w.show()
    sys.exit(app.exec())