#Файл в якому выдтворено ынтерфейс меню
from PySide6.QtCore import*
from PySide6.QtWidgets import*

window_menu = QWidget()
window_menu_layout = QVBoxLayout()

# Віджети вікна #

questions_list = QListWidget()

add_questions_pbtn = QPushButton("Додати питання")
remove_questions_pbtn = QPushButton("Видалити питання")

question_ledit = QLineEdit()
answer_ledit = QLineEdit()
wrong1_ledit = QLineEdit()
wrong2_ledit = QLineEdit()
wrong3_ledit = QLineEdit()

back_to_main_pbtn = QPushButton("Повернутись в меню")

# ЛЕЙAУТИ ВІКНА #

button_row_layout = QHBoxLayout()
question_form_layout = QFormLayout()

# РОЗТАШOВУЄМО ВІДЖЕТИ У ЛЕЙАУТАХ #

window_menu_layout.addWidget(questions_list)

button_row_layout.addWidget(add_questions_pbtn)
button_row_layout.addWidget(remove_questions_pbtn)
window_menu_layout.addLayout(button_row_layout)

question_form_layout.addRow("Введіть питанння:", question_ledit)
question_form_layout.addRow("Введіть питанння:", answer_ledit)
question_form_layout.addRow("Введіть питанння:", wrong1_ledit)
question_form_layout.addRow("Введіть питанння:", wrong2_ledit)
question_form_layout.addRow("Введіть питанння:", wrong3_ledit)
window_menu_layout.addLayout(question_form_layout)

window_menu_layout.addWidget(back_to_main_pbtn)

window_menu.setLayout(window_menu_layout)

