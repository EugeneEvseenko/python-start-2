#создай приложение для запоминания информации
#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle, randint
#главное окно
app = QApplication([])
#my_win = QWidget() лишнее
#my_win.setWindowTitle('Memory Card') лишнее
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.passed = False

question_list = []
question_list.append(Question('Какой национальности не существует?','Смурфы','Энцы', 'Чулымцы', 'Алеуты'))
question_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
question_list.append(Question('Национальная хижина якутов:','Ураса','Юрта','Иглу','Хата'))

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

ResultGB = QGroupBox("")
resV = QVBoxLayout()
res_label_total = QLabel("Всего:")
res_label_correct = QLabel("Правильных:")
res_label_wrong = QLabel("Не правильных:")
res_label_rating = QLabel("Рейтинг:")

resV.addWidget(res_label_total, alignment=Qt.AlignLeft)
resV.addWidget(res_label_correct, alignment=Qt.AlignLeft)
resV.addWidget(res_label_wrong, alignment=Qt.AlignLeft)
resV.addWidget(res_label_rating, alignment=Qt.AlignLeft)
ResultGB.setLayout(resV)
ResultGB.hide()

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('Ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(ResultGB)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! вот что ты забыл добавить !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
AnsGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

answers = [rbtn1,rbtn2,rbtn3,rbtn4]

def show_all_results():
    window.setWindowTitle('Результаты теста')
    lb_Question.setText("Результаты")
    res_label_total.setText("Всего: "+str(window.total))
    res_label_correct.setText('Правильных: '+str(window.score))
    res_label_wrong.setText("Не правильных: "+str(window.total-window.score))
    res_label_rating.setText("Рейтинг: "+str(int(window.score/window.total*100))+'%')
    ResultGB.show()
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    btn_OK.setText("Заново")

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def next_question():
    window.setWindowTitle("Memo Card - Вопрос {} из {}".format(window.total +1, len(question_list)))
    while True:
        rindex = randint(0, len(question_list)-1)
        question = question_list[rindex]
        if not question.passed:
            break
    window.target = rindex
    window.total += 1
    ask(question)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Результаты':
        show_all_results()
    elif btn_OK.text() == 'Заново':
        window.score = 0
        window.total = 0
        window.target = 0
        for item in question_list:
            item.passed = False
        ResultGB.hide()
        next_question()
    else:
        next_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    question_list[window.target].passed = True
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    if window.total == len(question_list):
        btn_OK.setText("Результаты")

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
window.target = 0 # не была объявлена
next_question()
window.resize(400,300)
window.show()
app.exec()