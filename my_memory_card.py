#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, QPushButton, QLabel, 
    QRadioButton, QGroupBox, QVBoxLayout,
    QHBoxLayout, QButtonGroup)
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct_ans.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика:\nВсего вопросов:', main_win.total,
        '\nПравильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total)*100, '%' )
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:', (main_win.score/main_win.total)*100, '%')
def next_question():
    main_win.total += 1
    print('Статистика:\nВсего вопросов:', main_win.total,
    '\nПравильных ответов:', main_win.score)
    cur_question = randint(0, len(question_list)- 1) 
    if len(question_list) <= cur_question:
        main_win.cur_question = 0
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def show_correct(res):
    result.setText(res)
    show_result()

question_list = list()
q1 = Question('Государственный язык Испании', "Испанский", 'Бразильский', "Французский", "Русский")
q2 = Question('2 + 2 * 2', '6', '4', '9', '12')
q3 = Question('Какого цвета нет на светофоре', "Белого", "Красного", "Зелёного", "Жёлтого")
q4 = Question('Сколько дней в весокосном году', "366", "365", "367", "264")
q5 = Question('Что из этого овощ', 'морковь', "яблоко", "груша", "арбуз")
q6 = Question('Сколько секунд в одном часу', "3600", "600", "360", "6000")
q7 = Question("Последняя буква алфавита", "я", "ю", "ь", "ы")
q8 = Question("Кто был братом Симки из Фиксиков", "Нолик", "Фаер", "Игрик", "Дедус")
q9 = Question("3 ^ 3", "27", "9", "3", "6")
q10 = Question("4 * 4", "16", "8", "14", "400")
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)
main_layout = QVBoxLayout()
gb_layout = QHBoxLayout()
que_layout = QHBoxLayout()
btn_layout = QHBoxLayout()

question = QLabel('Здесь будет вопрос')
que_layout.addWidget(question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
btn = QPushButton('Ответить')
btn_layout.addStretch(3)
btn_layout.addWidget(btn, stretch=1)
btn_layout.addStretch(3)

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

AnsGroupBox = QGroupBox("Результаты теста:")
AnsGroupBox.hide()
result = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')
corr_layout = QVBoxLayout()
corr_layout.addWidget(result, alignment=(Qt.AlignTop | Qt.AlignLeft))
corr_layout.addWidget(correct_ans, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(corr_layout)
agb_layout = QHBoxLayout()
agb_layout.addWidget(AnsGroupBox)
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addStretch(1)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addStretch(1)
layout_ans1.addLayout(layout_ans3)
layout_ans1.addStretch(1)

RadioGroupBox.setLayout(layout_ans1)
gb_layout.addWidget(RadioGroupBox)

main_layout.addLayout(que_layout)
main_layout.addLayout(gb_layout)
main_layout.addLayout(agb_layout)
main_layout.addLayout(btn_layout)
main_win.setLayout(main_layout)
main_win.score = 0
main_win.total = 0
next_question()
btn.clicked.connect(click_OK)


main_win.show()
app.exec_()