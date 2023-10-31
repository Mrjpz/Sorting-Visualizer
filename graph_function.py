import sys, main, randomizer
from PySide6.QtCore import Qt, QRectF, Slot
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit
from PySide6.QtCharts import QBarSeries, QBarSet, QChart, QChartView



class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()

    def UI(self):
        
        available_geometry = self.screen().availableGeometry()
        size = available_geometry.height() * .7
        bar_width = 1
        
        #main layout
        self.main_layout = QGridLayout()
        self.settings_layout = QGridLayout()
        
        
        self.setLayout(self.main_layout)
        self.setWindowTitle("Sorting Visualizer")
        self.show()

    