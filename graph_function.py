import sys, main
from PySide6.QtCore import Qt, QRectF, Slot
from PySide6.QtGui import QBrush, QColor, QPainter, QPen
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox, QPushButton, QWidget, QMainWindow, QVBoxLayout, QLineEdit
from PySide6.QtCharts import QBarSeries, QBarSet, QChart, QChartView



class Visualizer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UI()

    def UI(self):
        w = Visualizer.screen()
        print(w)
        
        
        
        #main layout
        self.main_layout = QGridLayout()
        self.settings_layout = QGridLayout()
        #-----
        
        self.chart = QChart()
        self.barseries = QBarSeries()
        self.barset = QBarSet(None)
        
        self.barset.append([8,8,12,3,6,4,2,3,4,1,2])
        self.barseries.append(self.barset)
        self.chart.addSeries(self.barseries)
        
        self.chartview = QChartView(self.chart, self)
        
        
        self.chartview.setMinimumSize(720,440)
        
        
        #-----
        
        self.main_layout.addWidget(self.chartview, 0, 1, 3, 1)
        
        self.setLayout(self.main_layout)
        
        self.setWindowTitle("Sorting Visualizer")
        self.show()

    