from questions_controller import*

q1 = Question(
    question="5+5",
    answer="9",
    wrong_answer1="20",
    wrong_answer2="21",
    wrong_answer3="22"
)

q2 = Question(
    question="Что то там",
    answer="!",
    wrong_answer1="&",
    wrong_answer2="@",
    wrong_answer3="?"
)

question_controller = QuestionController()
question_controller.add_answer(q1)
question_controller.add_answer(q2)