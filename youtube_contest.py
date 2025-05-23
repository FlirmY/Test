#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
     QApplication, QWidget, QRadioButton , QLabel , QVBoxLayout , QHBoxLayout, QMessageBox
)
#создание приложения и главного окна

def show_win():
    victory_window = QMessageBox()
    victory_window.setText('Вы выйграли +100k$')
    victory_window.exec()



def show_lose():
    lose_window = QMessageBox()
    lose_window.setText('Проиграл')
    lose_window.exec()


app = QApplication([])
window = QWidget()
window.setWindowTitle('Опрос Опрос')
window.resize(600,300)
text = QLabel('сколько зубов у взрослого человека')
button1 = QRadioButton('0')
button1.clicked.connect(show_lose)
button2 = QRadioButton('114')
button2.clicked.connect(show_lose)
button3= QRadioButton('45')
button3.clicked.connect(show_lose)
button4 = QRadioButton('32')
button4.clicked.connect(show_win)
v_line = QVBoxLayout() #главная  вертикальная линия
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout() 

h1_line.addWidget(text,alignment = Qt.AlignCenter)

h2_line.addWidget(button1, alignment = Qt.AlignCenter)
h2_line.addWidget(button2, alignment = Qt.AlignCenter)

h3_line.addWidget(button3, alignment = Qt.AlignCenter)
h3_line.addWidget(button4, alignment = Qt.AlignCenter)

v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
v_line.addLayout(h3_line)
window.setLayout(v_line)
window.show()


window.show()
app.exec()
#создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 