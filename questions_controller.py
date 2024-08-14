from main_Window import*
from menu_window import *
from random import shuffle, choice

#Модель питання зберігає всю інформацію про нього
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):

        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        

#Клас контролер, буде виконувати всі дії з питанням: відбирати рандомне і.т.д.
class QuestionController:
    def __init__(self):
        self.questions = []
        self.answer_buttons = [ans1_rbtn, ans2_rbtn, ans3_rbtn, ans4_rbtn]
        self.questioin_widget = question_lbl
        self.result_widget = result_lbl

        self.answers_list = questions_list
        self.new_question_input_qustion = question_ledit
        self.new_question_input_answer = answer_ledit
        self.new_question_input_wrong1 = wrong1_ledit
        self.new_question_input_wrong2 = wrong2_ledit
        self.new_question_input_wrong3 = wrong3_ledit

    def shuffle_buttons(self):
        shuffle(self.answer_buttons)    

    def choose_random_answer(self):
        return choice(self.questions)

    def show_question(self):
        next_question = self.choose_random_answer()

        self.shuffle_buttons()
        
        self.questioin_widget.setText(next_question.question)
        self.answer_buttons[0].setText(next_question.answer)
        self.answer_buttons[1].setText(next_question.wrong_answer1)
        self.answer_buttons[2].setText(next_question.wrong_answer2)
        self.answer_buttons[3].setText(next_question.wrong_answer3)

    def add_answer(self, question):
        self.questions.append(question)
        self.answers_list.addItem(question.question)

    def remove_answer(self, id):
        pass

    def check_is_right_answer(self):
        return self.answer_buttons[0].isChecked()