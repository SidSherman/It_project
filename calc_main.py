import sys
from calc_interface import *
from calculte import *
from matrix import *
from converters import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        QtWidgets.QWidget.setFocus(self.ui.lineEdit)

        self.ui.action_2.triggered.connect(lambda: self.changer_calc(0))
        self.ui.action_3.triggered.connect(lambda: self.changer_calc(1))
        self.ui.action_5.triggered.connect(lambda: self.close())
        self.ui.action_6.triggered.connect(lambda: self.changer_calc(3))
        self.ui.action.triggered.connect(lambda: self.changer_calc(2))
        self.ui.groupBox.setVisible(False)

        self.ui.frame_res.setVisible(False)

        self.ui.label_name_func.setText("Введите число")
        self.ui.label_name_res.setText("Ответ")
        self.ui.comboBox_matrix_1_collums.addItems([str(i) for i in range(1,8)])
        self.ui.comboBox_matrix_1_rows.addItems([str(i) for i in range(1,8)])
        self.ui.comboBox_matrix_2_collums.addItems([str(i) for i in range(1,8)])
        self.ui.comboBox_matrix_2_rows.addItems([str(i) for i in range(1,8)])

        self.ui.comboBox_matrix_1_collums.currentIndexChanged.connect(lambda: self.set_matrix("cb1c"))
        self.ui.comboBox_matrix_2_collums.currentIndexChanged.connect(lambda: self.set_matrix("cb2c"))
        self.ui.comboBox_matrix_1_rows.currentIndexChanged.connect(lambda: self.set_matrix("cb1r"))
        self.ui.comboBox_matrix_2_rows.currentIndexChanged.connect(lambda: self.set_matrix("cb2r"))

        self.ui.comboBox_result.currentIndexChanged.connect(self.change_func)

        self.ui.comboBox_result.addItems(["Умножение матрицы на число",\
                                          "Возведение матрицы в степень", \
                                         "Умножение матриц",\
                                         "Сложение матриц", \
                                          "Вычитание матриц",
                                         "Треугольный вид", \
                                          "Транспонирование",\
                                          "Диагональный вид",\
                                          "Обратная матрица",\
                                         "Определитель матрицы",\
                                         "Ранг матрицы",\
                                         ])

        self.ui.tableWidget_matrix_1.setRowCount(1)
        self.ui.tableWidget_matrix_1.setColumnCount(1)
        self.ui.tableWidget_matrix_2.setRowCount(1)
        self.ui.tableWidget_matrix_2.setColumnCount(1)

        self.ui.listWidget.addItems(["Валюта",\
                                     "Температура", \
                                     'Длина', \
                                     'Площадь', \
                                     'Время',\
                                     "Масса",\
                                     'Скорость',\
                                     'Объем'])

        self.ui.listWidget.itemClicked.connect(self.set_comboboxes)

        self.ui.con_change.clicked.connect(self.con_change)
        #self.ui.comboBox_con_input.currentIndexChanged.connect(self.con_change)
        #self.ui.comboBox_con_output.currentIndexChanged.connect(self.con_change)

        self.ui.tableWidget_matrix_1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_matrix_1.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_matrix_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_matrix_2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_matrix_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_matrix_3.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.ui.frame_two_matrix.setVisible(False)

        self.ui.lineEdit_con_input.textEdited.connect(self.con_result)
        self.ui.Button_clean_matrix.clicked.connect(self.clean_matrix)
        self.ui.Button_result_martix.clicked.connect(self.result_matrix)

        '''
        Кнопки ввода
        '''
        self.ui.Button_1.clicked.connect(lambda: self.inputline(self.ui.Button_1.text()))
        self.ui.Button_2.clicked.connect(lambda: self.inputline(self.ui.Button_2.text()))
        self.ui.Button_3.clicked.connect(lambda:self.inputline(self.ui.Button_3.text()))
        self.ui.Button_4.clicked.connect(lambda:self.inputline(self.ui.Button_4.text()))
        self.ui.Button_5.clicked.connect(lambda:self.inputline(self.ui.Button_5.text()))
        self.ui.Button_6.clicked.connect(lambda:self.inputline(self.ui.Button_6.text()))
        self.ui.Button_7.clicked.connect(lambda:self.inputline(self.ui.Button_7.text()))
        self.ui.Button_8.clicked.connect(lambda:self.inputline(self.ui.Button_8.text()))
        self.ui.Button_9.clicked.connect(lambda:self.inputline(self.ui.Button_9.text()))
        self.ui.Button_0.clicked.connect(lambda:self.inputline(self.ui.Button_0.text()))
        self.ui.Button_divide.clicked.connect(lambda:self.inputline(self.ui.Button_divide.text()))
        self.ui.Button_mult.clicked.connect(lambda:self.inputline(self.ui.Button_mult.text()))
        self.ui.Button_dot.clicked.connect(lambda:self.inputline(self.ui.Button_dot.text()))
        self.ui.Button_diff.clicked.connect(lambda:self.inputline(self.ui.Button_diff.text()))
        self.ui.Button_sum.clicked.connect(lambda:self.inputline(self.ui.Button_sum.text()))
        self.ui.Button_left_parenthesis.clicked.connect(lambda:self.inputline(self.ui.Button_left_parenthesis.text()))
        self.ui.Button_right_parenthesis.clicked.connect(lambda:self.inputline(self.ui.Button_right_parenthesis.text()))
        self.ui.Button_sqrt.clicked.connect(lambda: self.inputline(self.ui.Button_sqrt.text()))
        self.ui.Button_faqtorial.clicked.connect(lambda: self.inputline(self.ui.Button_faqtorial.text()))
        self.ui.Button_sin.clicked.connect(lambda: self.inputline(self.ui.Button_sin.text()))
        self.ui.Button_cos.clicked.connect(lambda: self.inputline(self.ui.Button_cos.text()))
        self.ui.Button_tan.clicked.connect(lambda: self.inputline(self.ui.Button_tan.text()))
        self.ui.Button_pi.clicked.connect(lambda: self.inputline(self.ui.Button_pi.text()))
        self.ui.Button_e.clicked.connect(lambda: self.inputline(self.ui.Button_e.text()))
        self.ui.Button_log.clicked.connect(lambda: self.inputline(self.ui.Button_log.text()))
        self.ui.Button_dec.clicked.connect(lambda: self.inputline(self.ui.Button_dec.text()))
        self.ui.Button_grad.clicked.connect(lambda: self.inputline(self.ui.Button_grad.text()))
        self.ui.Button_backspace.clicked.connect(self.ui.lineEdit.backspace)
        self.ui.Button_left.clicked.connect(lambda:self.ui.lineEdit.cursorBackward(False))
        self.ui.Button_right.clicked.connect(lambda:self.ui.lineEdit.cursorForward(False))

        self.ui.Button_clean.clicked.connect(self.clear_text)

        # кнопка вывода '=' и привязка к клавише enter
        self.ui.Button_result.clicked.connect(self.output_result)
        self.ui.Button_result.setAutoDefault(True)  # click on <Enter>
        self.ui.lineEdit.returnPressed.connect(self.ui.Button_result.click)  # click on <Enter>

        self.select_simbols = {"48": "0", "49": "1",
                          "50": "2", "51":"3", "52":"4", "53": "5", \
                          "54": "6", "55": "7", "56": "8", "57": "9", \
                          "45": "-", "43": "+", "41": ")", "40": "(", "46": ".", \
                          "42": "*", "47": "/", "33": "!", "124": "|", "94": "^", "69": "e"}

        self.exeption_input = {"sin":"sin()","cos":"cos()","tan":"tan()","log":"log( , )", "n!":"!", "1/x":"(1/)"}

        self.comboboxes = {"Валюта": list(dict_currencies.keys()),'Температура':list_temperatures,\
                           'Длина':list(dict_lengths.keys()),'Площадь':(dict_squares.keys()),\
            'Время':list(dict_times.keys()),'Масса':(dict_masses.keys()),'Скорость':(dict_speeds.keys()),'Объем':(dict_volumes.keys())}

    def con_change(self):
        temp = self.ui.comboBox_con_input.currentIndex()
        self.ui.comboBox_con_input.setCurrentIndex(self.ui.comboBox_con_output.currentIndex())
        self.ui.comboBox_con_output.setCurrentIndex(temp)
        temp =  self.ui.lineEdit_con_input.text()
        self.ui.lineEdit_con_input.setText(self.ui.lineEdit_con_output.text())
        self.ui.lineEdit_con_output.setText(temp)

    def set_comboboxes(self):
        self.ui.comboBox_con_input.clear()
        self.ui.comboBox_con_output.clear()
        self.ui.comboBox_con_input.addItems(self.comboboxes[self.ui.listWidget.currentItem().text()])
        self.ui.comboBox_con_output.addItems(self.comboboxes[self.ui.listWidget.currentItem().text()])
        self.ui.lineEdit_con_input.clear()
        self.ui.lineEdit_con_output.clear()

    def clean_matrix(self):
        self.ui.tableWidget_matrix_1.clear()
        self.ui.tableWidget_matrix_2.clear()
        self.ui.tableWidget_matrix_2.clear()
        self.ui.lineEdit_enter_num_matrix.clear()
        self.ui.lineEdit_result_matrix.clear()

    def con_result(self):
        try:
            if self.ui.lineEdit_con_input.text() != "":
                if self.ui.listWidget.currentRow() == 0:
                    self.ui.lineEdit_con_output.setText(currency(dict_currencies[self.ui.comboBox_con_input.currentText()], \
                                                        dict_currencies[self.ui.comboBox_con_output.currentText()], \
                                                        int(self.ui.lineEdit_con_input.text())))
                if self.ui.listWidget.currentRow() == 1:
                    self.ui.lineEdit_con_output.setText(str(temperature(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        float(self.ui.lineEdit_con_input.text()))))
                if self.ui.listWidget.currentRow() == 2:
                    print(int(self.ui.lineEdit_con_input.text()))
                    print(dict_lengths[self.ui.comboBox_con_input.currentText()])
                    self.ui.lineEdit_con_output.setText(str(lengths(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text()))))
                if self.ui.listWidget.currentRow() == 3:
                    self.ui.lineEdit_con_output.setText(str(squares(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text()))))
                if self.ui.listWidget.currentRow() == 4:
                    self.ui.lineEdit_con_output.setText(times(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text())))
                if self.ui.listWidget.currentRow() == 5:
                    self.ui.lineEdit_con_output.setText(masses(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text())))
                if self.ui.listWidget.currentRow() == 6:
                    self.ui.lineEdit_con_output.setText(speeds(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text())))
                if self.ui.listWidget.currentRow() == 7:
                    self.ui.lineEdit_con_output.setText(volumes(self.ui.comboBox_con_input.currentText(), \
                                                        self.ui.comboBox_con_output.currentText(), \
                                                        int(self.ui.lineEdit_con_input.text())))
            else: self.ui.lineEdit_con_output.clear()

        except ValueError:
            self.ui.statusbar.showMessage('Проверьте корректность ввода', 5000)

    def change_func(self):
        self.ui.frame_res.setVisible(False)
        self.ui.frame_enter_number.setEnabled(False)

        self.ui.frame_two_matrix.setEnabled(False)
        self.ui.groupBox.setEnabled(False)


        if self.ui.comboBox_result.currentIndex() in [2,3,4]:
            self.ui.frame_two_matrix.setEnabled(True)

            self.ui.frame_enter_number.setEnabled(False)
            self.ui.frame_res.setVisible(False)

        if  self.ui.comboBox_result.currentIndex() == 5:
            self.ui.groupBox.setVisible(True)
            self.ui.groupBox.setEnabled(True)
            self.ui.frame_res.setVisible(False)
            self.ui.frame_enter_number.setVisible(False)



        if self.ui.comboBox_result.currentIndex() == 0 or self.ui.comboBox_result.currentIndex() == 1:
            self.ui.frame_enter_number.setVisible(True)
            self.ui.frame_enter_number.setEnabled(True)
            self.ui.groupBox.setVisible(False)


        if self.ui.comboBox_result.currentIndex() == 9 or self.ui.comboBox_result.currentIndex() == 10:
            self.ui.frame_res.setVisible(True)
            self.ui.tableWidget_matrix_3.setVisible(False)

    def result_matrix(self):
        try:
            matrix_1 = []
            for i in range(self.ui.tableWidget_matrix_1.rowCount()):
                matrix_1.append([])
                for j in range(self.ui.tableWidget_matrix_1.columnCount()):
                    matrix_1[i].append(int(self.ui.tableWidget_matrix_1.item(i, j).text()))

            if self.ui.comboBox_result.currentIndex() == 2:
                matrix_2 = []
                if self.ui.tableWidget_matrix_1.columnCount() == self.ui.tableWidget_matrix_2.rowCount():
                    for i in range(self.ui.tableWidget_matrix_2.rowCount()):
                        matrix_2.append([])
                        for j in range(self.ui.tableWidget_matrix_2.columnCount()):
                            matrix_2[i].append(int(self.ui.tableWidget_matrix_2.item(i, j).text()))
                    matrix_result = mult_by_matrix(matrix_1, matrix_2)
                    self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                    self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))

                    for i in range(len(matrix_result)):
                        for j in range(len(matrix_result[i])):
                            item = QtWidgets.QTableWidgetItem()
                            item.setText(str(matrix_result[i][j]))
                            self.ui.tableWidget_matrix_3.setItem(i, j, item)
                else:
                    self.ui.statusbar.showMessage(
                        "Количество столбцов первой матрицы не совпадает с количеством столцов второй матрицы!", 3000)

            if self.ui.comboBox_result.currentIndex() == 3:
                if self.ui.tableWidget_matrix_1.columnCount() == self.ui.tableWidget_matrix_2.columnCount() and \
                        self.ui.tableWidget_matrix_1.rowCount() == self.ui.tableWidget_matrix_2.rowCount():

                    matrix_2 = []
                    for i in range(self.ui.tableWidget_matrix_2.rowCount()):
                        matrix_2.append([])
                        for j in range(self.ui.tableWidget_matrix_2.columnCount()):
                            matrix_2[i].append(int(self.ui.tableWidget_matrix_2.item(i, j).text()))
                    matrix_result = matrix_sum(matrix_1, matrix_2)
                    self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                    self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))

                    for i in range(len(matrix_result)):
                        for j in range(len(matrix_result[i])):
                            item = QtWidgets.QTableWidgetItem()
                            item.setText(str(matrix_result[i][j]))
                            self.ui.tableWidget_matrix_3.setItem(i, j, item)
                else:
                    self.ui.statusbar.showMessage(
                        "Введите матрицы одинаковых размеров", 3000)

            if self.ui.comboBox_result.currentIndex() == 0:
                matrix_result = mult_by_number(matrix_1, int(self.ui.lineEdit_enter_num_matrix.text()))
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 1:
                matrix_result = matrix_pow(matrix_1, int(self.ui.lineEdit_enter_num_matrix.text()))
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 4:
                if self.ui.radio_treagle_up.isChecked():
                    arg = 0
                else:
                    arg = 1

                matrix_result = to_triangle(matrix_1, arg)
                print(matrix_result)
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 5:
                matrix_result = transpose(matrix_1)
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 6:
                matrix_result = to_diagonal(matrix_1)
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 7:
                matrix_result = inverse(matrix_1)
                self.ui.tableWidget_matrix_3.setRowCount(len(matrix_result))
                self.ui.tableWidget_matrix_3.setColumnCount(len(matrix_result[0]))
                for i in range(len(matrix_result)):
                    for j in range(len(matrix_result[i])):
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(matrix_result[i][j]))
                        self.ui.tableWidget_matrix_3.setItem(i, j, item)

            if self.ui.comboBox_result.currentIndex() == 8:
                result = determinant(matrix_1)
                self.ui.lineEdit_result_matrix.setText(str(result))

            if self.ui.comboBox_result.currentIndex() == 9:
                result = get_rank(matrix_1)
                self.ui.lineEdit_result_matrix.setText(str(result))

        except AttributeError:
            self.ui.statusbar.showMessage('Проверьте корректность ввода', 5000)
        except SyntaxError:
            self.ui.statusbar.showMessage('Проверьте корректность ввода', 5000)




    def set_matrix(self, combo_box):
        if combo_box == "cb1c":
            self.ui.tableWidget_matrix_1.setColumnCount(self.ui.comboBox_matrix_1_collums.currentIndex()+1)
        if combo_box == "cb2c":
            self.ui.tableWidget_matrix_2.setColumnCount(self.ui.comboBox_matrix_2_collums.currentIndex()+1)
        if combo_box == "cb1r":
            self.ui.tableWidget_matrix_1.setRowCount(self.ui.comboBox_matrix_1_rows.currentIndex()+1)
        if combo_box == "cb2r":
            self.ui.tableWidget_matrix_2.setRowCount(self.ui.comboBox_matrix_2_rows.currentIndex()+1)
        if combo_box == "cbres":
            self.ui.tableWidget_matrix_3.setColumnCount(self.ui.comboBox_matrix_1_collums.currentIndex())


    def changer_calc(self, x):
        self.ui.stackedWidget.setCurrentIndex(x)
        if x == 1 :
            self.setFixedSize(735, 661)
        if x == 0:
            self.setFixedSize(450, 425)
        if x ==2:
            self.setFixedSize(485, 200)



    def clear_text(self):
        self.ui.plainTextEdit_Result.clear()
        self.ui.lineEdit.clear()

    def inputline(self, x):
        if x in self.exeption_input:
            if x == "1/x":
                self.ui.lineEdit.setText(func(self.ui.lineEdit.text()))
            else:
                self.ui.lineEdit.insert(self.exeption_input[x])
                if x in ["sin","cos", "tan"]:
                    self.ui.lineEdit.cursorBackward(False)

        else:
            self.ui.lineEdit.insert(x)



    def keyReleaseEvent(self, e):
        if QtWidgets.QWidget.hasFocus(self.ui.lineEdit) == False:
            if e.key() == QtCore.Qt.Key_Enter:
                self.output_result()
            if e.key() == QtCore.Qt.Key_Backspace:
                self.ui.lineEdit.backspace()
            if e.key() == QtCore.Qt.Key_Space:
                pass
            if str(e.key()) in self.select_simbols:
                self.ui.lineEdit.insert(self.select_simbols[str(e.key())])


    def output_result(self):  # Функция вывода результата

        self.Input = self.ui.lineEdit.text() # Переменная содержащая строку из поля ввода

        """
        Функции для подсчета результата
        """
        try:
            self.ui.statusbar.clearMessage()
            self.Result = calculate(self.Input)
            self.ui.plainTextEdit_Result.clear()
            self.ui.plainTextEdit_Result.appendPlainText(str(self.Result))
        except SyntaxError:
            self.ui.statusbar.showMessage("Выражение не валидно!")
        except ZeroDivisionError:
            self.ui.statusbar.showMessage("Деление на ноль!")



if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.setFixedSize(450, 425)
    myapp.show()
    sys.exit(app.exec_())