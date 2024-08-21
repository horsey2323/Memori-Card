#Головний файл
from PySide6.QtCore import *
from PySide6.QtWidgets import*

from app import app
from main_Window import window_main
from menu_window import window_menu
from window_controls import*

window = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget(window_main)
window_layout.addWidget(window_menu)

window.setLayout(window_layout)
window.show()

show_main()
show_questions()
connect_buttons()

app.exec()