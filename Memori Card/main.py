#Головний файл
from PySide6.QtCore import *
from PySide6.QtWidgets import*

from app import app
from main_Window import window_main
window = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget(window_main)

window.setLayout(window_layout)
window.show()
app.exec()