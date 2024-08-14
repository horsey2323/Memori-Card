#Файл, в якому інтерфейс головного вікна

from PySide6.QtCore import*
from PySide6.QtWidgets import*

window_main = QWidget()
window_main_layout = QVBoxLayout()

# Віджети вікна #

menu_pbtn = QPushButton("Налаштування")
rest_pbtn = QPushButton("Відпочинок")
give_answer_pbtn = QPushButton("Відповісти")

rest_sbox = QSpinBox()
rest_sbox.setValue(30)

ans1_rbtn = QRadioButton("Answer 1")
ans2_rbtn = QRadioButton("Answer 2")
ans3_rbtn = QRadioButton("Answer 3")
ans4_rbtn = QRadioButton("Answer 4")

question_lbl = QLabel("Question")
minutes_lbl = QLabel("хвилини")
result_lbl = QLabel("Правильна відповідь")

answers_gbox = QGroupBox()
result_gbox = QGroupBox()

# ЛЕЙАУТИ ВІКНА #

header_layout = QHBoxLayout()

answers_gbox_layout = QVBoxLayout()
result_gbox_layout = QVBoxLayout()

answer_buttons_row1_layout = QHBoxLayout()
answer_buttons_row2_layout = QHBoxLayout()
# РОЗТАШOВУЄМО ВІДЖЕТИ У ЛЕЙАУТАХ #

header_layout.addWidget(menu_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(minutes_lbl)
window_main_layout.addLayout(header_layout)

window_main_layout.addWidget(question_lbl)

answer_buttons_row1_layout.addWidget(ans1_rbtn)
answer_buttons_row1_layout.addWidget(ans2_rbtn)

answer_buttons_row2_layout.addWidget(ans3_rbtn)
answer_buttons_row2_layout.addWidget(ans4_rbtn)

answers_gbox_layout.addLayout(answer_buttons_row1_layout)
answers_gbox_layout.addLayout(answer_buttons_row2_layout)

answers_gbox.setLayout(answers_gbox_layout)
window_main_layout.addWidget(answers_gbox)

result_gbox_layout.addWidget(result_lbl)
result_gbox.setLayout(result_gbox_layout)
window_main_layout.addWidget(result_gbox)

window_main_layout.addWidget(give_answer_pbtn)

window_main.setLayout(window_main_layout)