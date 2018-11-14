import sys
from window1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        '''
        Кнопки ввода
        '''
        self.ui.Button_1.clicked.connect(self.input_1)
        self.ui.Button_2.clicked.connect(self.input_2)
        self.ui.Button_3.clicked.connect(self.input_3)
        self.ui.Button_4.clicked.connect(self.input_4)
        self.ui.Button_5.clicked.connect(self.input_5)
        self.ui.Button_6.clicked.connect(self.input_6)
        self.ui.Button_7.clicked.connect(self.input_7)
        self.ui.Button_8.clicked.connect(self.input_8)
        self.ui.Button_9.clicked.connect(self.input_9)
        self.ui.Button_0.clicked.connect(self.input_0)
        self.ui.Button_divide.clicked.connect(self.input_divide)
        self.ui.Button_mult.clicked.connect(self.input_mult)
        self.ui.Button_dot.clicked.connect(self.input_dot)
        self.ui.Button_diff.clicked.connect(self.input_diff)
        self.ui.Button_sum.clicked.connect(self.input_sum)
        self.ui.Button_left_parenthesis.clicked.connect(self.input_left_parenthesis)
        self.ui.Button_right_parenthesis.clicked.connect(self.input_right_parenthesis)

        # кнопка вывода '=' и привязка к клавише enter
        self.ui.Button_result.clicked.connect(self.input_result)
        self.ui.Button_result.setAutoDefault(True)  # click on <Enter>
        self.ui.plainTextEdit_Result.returnPressed.connect(self.ui.Button_result.click)  # click on <Enter>

    # Все функции для ввода с кнопок
    # Все эти функции можно убрать в отдельный модуль потом

    def input_1(self):
        self.ui.lineEdit.insertPlainText("1")

    def input_2(self):
        self.ui.lineEdit.insertPlainText("2")

    def input_3(self):
        self.ui.lineEdit.insertPlainText("3")

    def input_4(self):
        self.ui.lineEdit.insertPlainText("4")

    def input_5(self):
        self.ui.lineEdit.insertPlainText("5")

    def input_6(self):
        self.ui.lineEdit.insertPlainText("6")

    def input_7(self):
        self.ui.lineEdit.insertPlainText("7")

    def input_8(self):
        self.ui.lineEdit.insertPlainText("8")

    def input_9(self):
        self.ui.lineEdit.insertPlainText("9")

    def input_0(self):
        self.ui.lineEdit.insertPlainText("0")

    def input_dot(self):
        self.ui.lineEdit.insertPlainText(".")

    def input_divide(self):
        self.ui.lineEdit.insertPlainText("/")

    def input_mult(self):
        self.ui.lineEdit.insertPlainText("*")

    def input_diff(self):
        self.ui.lineEdit.insertPlainText("-")

    def input_sum(self):
        self.ui.lineEdit.insertPlainText("+")

    def input_left_parenthesis(self):
        self.ui.lineEdit.insertPlainText(")")

    def input_right_parenthesis(self):
        self.ui.lineEdit.insertPlainText("(")



    def input_result(self):  # Функция вывода результата

        self.Input =self.ui.lineEdit.text() # Переменная содержащая строку из поля ввода

        """
        Функции для подсчета результата
        """

        self.ui.plainTextEdit_Result.appendPlainText.clear()
        self.ui.plainTextEdit_Result.appendPlainText(self.Result) # Для записи ответа используй переменную self.Result



if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
