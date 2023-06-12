from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
main_win = QWidget()

btn_OK = QPushButton("Ответ")

main_win.setWindowTitle("ОПРОС")
main_win.resize(500, 500)
wopros = QLabel("Какой национальности не существует?")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("Правильно/Неправильно")
lb_Correct = QLabel("Правильный ответ")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=(Qt.AlignHCenter), stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(wopros, alignment=(Qt.AlignHCenter))
layout_line4 = QHBoxLayout()
layout_line1 = QHBoxLayout()
layout_line1.addWidget(wopros, alignment=(Qt.AlignHCenter))
layout_line3 = QHBoxLayout()
layout_line4.addWidget(RadioGroupBox)
layout_line4.addWidget(AnsGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line4)
layout_card.addLayout(layout_line3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox.hide()
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответ")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText("Следующий вопрос")

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    wopros.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

num_q = -1
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Немецкий', 'Русский')
q2 = Question('Год отмены крепостного права', '1861', '1864', '1859', '1868')
q3 = Question('Какой из ответов правильный?', 'Правильный', 'Этот', 'Никакой', 'Все')
q4 = Question('120+65 = ?', '185', '180', '175', '190')
q5 = Question('В чем изеряется мощность?', 'Ватты', 'Джоули', 'Паскали', 'Секунды')
question_list = [q1, q2, q3, q4, q5]

def next_question():
    global num_q, question_list
    num_q = num_q + 1
    if num_q >= len(question_list):
        num_q = 0
    quest = question_list[num_q]
    ask(quest)

def start_test():
    if btn_OK.text()=="Ответ":
        check_answer()
    else:
        next_question()
next_question()

btn_OK.clicked.connect(start_test)


main_win.setLayout(layout_card)
main_win.show()
app.exec_()    
