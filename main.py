import webbrowser, resources

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import (Qt,
                         QPropertyAnimation,
                         QPoint,
                         QParallelAnimationGroup)

from PyQt5.QtWidgets import (QMainWindow,
                            QApplication,
                            QPushButton,
                            QHBoxLayout,
                            QVBoxLayout,
                            QWidget,
                            QLineEdit,
                            QPlainTextEdit,
                            QScrollBar)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.windowUI()
        self.toStyles()
        self.PlainEdit()
        self.Placeholder_answer()
        self.Buttons()

        self.WidgetPanel = QWidget(self)
        self.WidgetPanel.setStyleSheet("background-color: #1E1E1E")
        self.WidgetPanel.setGeometry(-300, 0, 300, 700)

        self.CloseButton = QPushButton("✕", self)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(self.toStyles)
        self.CloseButton.setGeometry(-300, 30, 30, 30)
        self.CloseButton.clicked.connect(self.PanelClose)

        self.TelegramButton = QPushButton("Telegram", self)
        self.TelegramButton.setObjectName("TelegramButton")
        self.TelegramButton.setStyleSheet(self.toStyles)
        self.TelegramButton.setGeometry(-300, 100, 200, 30)
        self.TelegramButton.clicked.connect(self.openTelegramWebBrowser)

        self.GitHubButton = QPushButton("GitHub", self)
        self.GitHubButton.setObjectName("GitHubButton")
        self.GitHubButton.setStyleSheet(self.toStyles)
        self.GitHubButton.setGeometry(-300, 150, 200, 30)
        self.GitHubButton.clicked.connect(self.openGitHubWebBrowser)




        self.anim_group = QParallelAnimationGroup()
        self.AnimationPanel = QPropertyAnimation(self.WidgetPanel, b"pos")
        self.AnimationTelegramButton = QPropertyAnimation(self.TelegramButton, b"pos")
        self.AnimationGitHubButton = QPropertyAnimation(self.GitHubButton, b"pos")
        self.AnimationCloseButton = QPropertyAnimation(self.CloseButton, b"pos")

    def windowUI(self):
        self.setWindowTitle("Scrambler Calculator")
        self.setStyleSheet("background-color: black")
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/icons/ico.png"), QIcon.Selected, QIcon.On)
        self.setWindowIcon(self.icon)

    def toStyles(self):
        self.toStyles = """
            QPushButton {
                color: white;
                background-color: transparent;
                font-size: 20px;
                border: none;
                border-radius: 50px

            }
            QPushButton::pressed {
                font-size: 18px;
                background-color: #090708;
            }
            QPushButton::hover {
                background-color: #090708;
            }
            QPushButton#But_sub_div_add {
                color: green;
                background-color: transparent;
                font-size: 25px;
                border-radius: 50px
            }
            QPushButton#But_sub_div_add:pressed{
                font-size: 20px;
                background-color: #090708;
            }
            QPushButton#But_sub_div_add:hover{
                background-color: #090708;
            }

            QPushButton#But_addition {
                color: green;
                background-color: transparent;
                font-size: 35px;
                border-radius: 50px
            }
            QPushButton#But_addition:pressed{
                font-size: 20px;
                background-color: #090708;
            }
            QPushButton#But_addition:hover{
                background-color: #090708;
            }
            QPushButton#But_clear {
                color: red;
                font-size: 25px;
            }
            QPushButton#But_clear:pressed {
                font-size: 20px;
            }
            QPushButton#But_clear:hover {
                background-color: #090708;
            }
            QPushButton#But_result {
                font-size: 25px;
                background-color: green;
            }
            QPushButton#But_one_clear_symbol {
                color: green;
                background-color: transparent;
                font-size: 25px;
                border-radius: 50px
            }
            QPushButton#But_one_clear_symbol:hover{
                background-color: #090708;
            }
            QPushButton#But_one_clear_symbol:pressed{
                font-size: 20px;
            }
            QPushButton#TelegramButton {
                color: #fff;
                background-color: #208FFF;
                font-size: 18px;
                border-radius: 5px;
            }

            QPushButton#TelegramButton:hover {
                background-color: #46A0FC;
                font-size: 19px;
            }

            QPushButton#TelegramButton:pressed {
                background-color: #208FFF
            }
            QPushButton#GitHubButton {
                color: #fff;
                background-color: #080B0F;
                font-size: 16px;
                font: bold;
                border-radius: 5px;
            }

            QPushButton#GitHubButton:hover {
                background-color: #12151A;
                font-size: 17px;
            }

            QPushButton#GitHubButton:pressed {
                background-color: #080B0F
            }
            QPushButton#CloseButton {
                color: #fff;
                font-size: 20px;
                border-radius: 10;
            }
            QPushButton#CloseButton:hover {
                background-color: #2F2F32
            }
            QPlainTextEdit {
                border: none;
                margin: 10px;
                font-size: 25px;
                color: white;
            }
            QLineEdit#placeholder_answer_input{
                border: none;
                color: grey;
                margin: 10px;
                font-size: 20px;
            }
            QLineEdit#placeholder_answer_input:hover{
                color: silver;
            }
            QScrollBar:vertical {
                background: purple;
                width: 7px;
                margin: 0px 0px 0px 0px;
                min-height: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #5852D6;
                border-radius: 2px;
                min-height: 20px;
            }
            QScrollBar::add-page:vertical{
                background: #7874D1;
            }
            QScrollBar::sub-page:vertical{
                background: #6963DB;
            }
        """


    def Placeholder_answer(self):
        self.placeholder_answer_input = QLineEdit(self)
        self.placeholder_answer_input.setPlaceholderText("Answer")
        self.placeholder_answer_input.setGeometry(0, 95, 450, 40)
        self.placeholder_answer_input.setObjectName("placeholder_answer_input")
        self.placeholder_answer_input.setStyleSheet(self.toStyles)
        self.placeholder_answer_input.setReadOnly(True)

    def PlainEdit(self):
        self.scrolls = QScrollBar(self)
        self.scrolls.setStyleSheet(self.toStyles)
        self.scrolls.setWindowOpacity(1.0)
        self.scrolls.setSingleStep(1)


        self.input = QPlainTextEdit(self)
        self.input.adjustSize()
        self.input.setVerticalScrollBar(self.scrolls)
        self.input.setGeometry(0, 35, 450, 100)
        self.input.setStyleSheet(self.toStyles)
        self.input.setReadOnly(True)
        self.input.textChanged.connect(lambda: self.inputPlane())


    def inputPlane(self):


        if len(self.input.toPlainText()) >= 50:
            self.input.setStyleSheet("""QPlainTextEdit {
                border: none;
                margin: 10px;
                font-size: 20px;
                color: white;
            }""")

        if len(self.input.toPlainText()) <= 50:
            self.input.setStyleSheet("""QPlainTextEdit {
                border: none;
                margin: 10px;
                font-size: 25px;
                color: white;
            }""")

        if self.input.toPlainText() == "":
            self.But_one_clear_symbol.setStyleSheet("""QPushButton#But_one_clear_symbol {
                color: green;
                background-color: transparent;
                font-size: 25px;
                border-radius: 50px
            }
            QPushButton#But_one_clear_symbol:hover{
                background-color: #090708;
            }
            QPushButton#But_one_clear_symbol:pressed{
                font-size: 20px;
            }""")
            self.placeholder_answer_input.setText("")
            self.placeholder_answer_input.setStyleSheet("""QLineEdit#placeholder_answer_input{
                border: none;
                color: grey;
                margin: 10px;
                font-size: 20px;
            }
            QLineEdit#placeholder_answer_input:hover{
                color: silver;
            }""")

        if self.input.toPlainText() != "":
            self.But_one_clear_symbol.setStyleSheet("""QPushButton#But_one_clear_symbol {
                color: orange;
                background-color: transparent;
                font-size: 25px;
                border-radius: 50px
            }
            QPushButton#But_one_clear_symbol:hover{
                background-color: #090708;
            }
            QPushButton#But_one_clear_symbol:pressed{
                font-size: 20px;
            }""")

    def Buttons(self):

        self.OpenPanelButton = QPushButton("≡", self)
        self.OpenPanelButton.setStyleSheet(self.toStyles)
        self.OpenPanelButton.setGeometry(10, 590, 100, 100)
        self.OpenPanelButton.setToolTip("Open Panel")
        self.OpenPanelButton.clicked.connect(self.PanelOpen)


        self.But_zero = QPushButton('0', self)
        self.But_zero.setStyleSheet(self.toStyles)
        self.But_zero.setGeometry(120, 590, 200, 100)
        self.But_zero.clicked.connect(lambda: self.clickeds('0'))

        self.But_one = QPushButton('1', self)
        self.But_one.setStyleSheet(self.toStyles)
        self.But_one.setGeometry(10, 480, 100, 100)
        self.But_one.clicked.connect(lambda: self.clickeds('1'))

        self.But_two = QPushButton('2', self)
        self.But_two.setStyleSheet(self.toStyles)
        self.But_two.setGeometry(120, 480, 100, 100)
        self.But_two.clicked.connect(lambda: self.clickeds('2'))

        self.But_three = QPushButton('3', self)
        self.But_three.setStyleSheet(self.toStyles)
        self.But_three.setGeometry(230, 480, 100, 100)
        self.But_three.clicked.connect(lambda: self.clickeds('3'))


        self.But_four = QPushButton('4', self)
        self.But_four.setStyleSheet(self.toStyles)
        self.But_four.setGeometry(10, 370, 100, 100)
        self.But_four.clicked.connect(lambda: self.clickeds('4'))


        self.But_five = QPushButton('5', self)
        self.But_five.setStyleSheet(self.toStyles)
        self.But_five.setGeometry(120, 370, 100, 100)
        self.But_five.clicked.connect(lambda: self.clickeds('5'))


        self.But_six = QPushButton('6', self)
        self.But_six.setStyleSheet(self.toStyles)
        self.But_six.setGeometry(230, 370, 100, 100)
        self.But_six.clicked.connect(lambda: self.clickeds('6'))


        self.But_seven = QPushButton('7', self)
        self.But_seven.setStyleSheet(self.toStyles)
        self.But_seven.setGeometry(10, 260, 100, 100)
        self.But_seven.clicked.connect(lambda: self.clickeds('7'))


        self.But_eight = QPushButton('8', self)
        self.But_eight.setStyleSheet(self.toStyles)
        self.But_eight.setGeometry(120, 260, 100, 100)
        self.But_eight.clicked.connect(lambda: self.clickeds('8'))


        self.But_nine = QPushButton('9', self)
        self.But_nine.setStyleSheet(self.toStyles)
        self.But_nine.setGeometry(230, 260, 100, 100)
        self.But_nine.clicked.connect(lambda: self.clickeds('9'))



        self.But_clear = QPushButton('C', self)
        self.But_clear.setStyleSheet(self.toStyles)
        self.But_clear.setObjectName('But_clear')
        self.But_clear.setGeometry(10, 150, 200, 100)
        self.But_clear.clicked.connect(lambda: self.clickeds('C'))
        self.But_clear.setToolTip("Очистить")

        self.But_division = QPushButton('÷', self)
        self.But_division.setStyleSheet(self.toStyles)
        self.But_division.setObjectName('But_sub_div_add')
        self.But_division.setGeometry(230, 150, 100, 100)
        self.But_division.clicked.connect(lambda: self.clickeds('/'))
        self.But_division.setToolTip("Деление")

        self.But_multiplication  = QPushButton('×', self)
        self.But_multiplication.setStyleSheet(self.toStyles)
        self.But_multiplication.setObjectName('But_sub_div_add')
        self.But_multiplication.setGeometry(340, 260, 100, 100)
        self.But_multiplication.clicked.connect(lambda: self.clickeds('*'))
        self.But_multiplication.setToolTip("Умножение")

        self.But_addition  = QPushButton('-', self)
        self.But_addition.setStyleSheet(self.toStyles)
        self.But_addition.setObjectName('But_addition')
        self.But_addition.setGeometry(340, 370, 100, 100)
        self.But_addition.clicked.connect(lambda: self.clickeds('-'))
        self.But_addition.setToolTip("Минус")

        self.But_subtraction = QPushButton('+', self)
        self.But_subtraction.setStyleSheet(self.toStyles)
        self.But_subtraction.setObjectName('But_sub_div_add')
        self.But_subtraction.setGeometry(340, 480, 100, 100)
        self.But_subtraction.clicked.connect(lambda: self.clickeds('+'))
        self.But_subtraction.setToolTip("Плюс")

        self.But_one_clear_symbol = QPushButton('<', self)
        self.But_one_clear_symbol.setStyleSheet(self.toStyles)
        self.But_one_clear_symbol.setObjectName('But_one_clear_symbol')
        self.But_one_clear_symbol.setGeometry(340, 150, 100, 100)
        self.But_one_clear_symbol.clicked.connect(lambda: self.clickeds('<'))

        self.But_result = QPushButton('=', self)
        self.But_result.setStyleSheet(self.toStyles)
        self.But_result.setObjectName('But_result')
        self.But_result.setGeometry(340, 590, 100, 100)
        self.But_result.clicked.connect(lambda: self.clickeds('='))
        self.But_result.setToolTip("Равно")

        self.line = QPushButton('', self)
        self.line.setStyleSheet("background-color: silver; border: none;")
        self.line.setGeometry(10, 140, 430, 2)


    def clickeds(self, res):
        if res == "<":
            if self.input.toPlainText() != "":
                self.input.setPlainText(self.input.toPlainText()[:-1])
            else:
                pass

        if res == "C":
            self.input.setPlainText('')

        if res == "=":
            if self.input.toPlainText() != "":
                if not self.input.toPlainText()[-1] in "+-÷×*":
                    self.numpy_function(self.input.toPlainText())
                else:
                    pass
            else:
                pass

        if len(self.input.toPlainText()) >= 150:
            self.input.setPlainText(self.input.toPlainText())


        else:
            if res == '0':
                if self.input.toPlainText() != "":
                    self.input.setPlainText(self.input.toPlainText()+res)
                else:
                    pass

            elif res == '1':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '2':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '3':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '4':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '5':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '6':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '7':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '8':
                self.input.setPlainText(self.input.toPlainText()+res)

            elif res == '9':
                self.input.setPlainText(self.input.toPlainText()+res)



            elif res == "+":

                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+res)
                    else:
                        pass
                else:
                    pass

            elif res == "-":

                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+res)
                    else:
                        pass
                else:
                    pass


            elif res == "*":

                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+"×")
                    else:
                        pass
                else:
                    pass

            elif res == "/":

                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+"÷")
                    else:
                        pass
                else:
                    pass

            elif res == "":

                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+res)
                    else:
                        pass
                else:
                    pass

            elif res == "**":
                if len(self.input.toPlainText()) >= 15:
                    pass
                elif self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.input.setPlainText(self.input.toPlainText()+res)
                    else:
                        pass
                else:
                    pass

            elif res == "=":
                if self.input.toPlainText() != "":
                    if not self.input.toPlainText()[-1] in "+-÷×*":
                        self.numpy_function(self.input.toPlainText())
                    else:
                        pass
                else:
                    pass
            else:
                pass

    def numpy_function(self, answer):
        result = str(eval(self.input.toPlainText().replace("÷", "/").replace("×", "*")))
        self.placeholder_answer_input.setText(result) # not recommendet 'eval' or 'ast.litera_eval' use methot

    def PanelOpen(self):
        self.AnimationPanel.setEndValue(QPoint(0, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(50, 100))
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(50, 150))
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(250, 30))
        self.AnimationCloseButton.setDuration(180)

        self.input.setEnabled(False)
        self.placeholder_answer_input.setEnabled(False)
        self.But_three.setEnabled(False)
        self.But_six.setEnabled(False)
        self.But_nine.setEnabled(False)
        self.But_division.setEnabled(False)
        self.But_multiplication.setEnabled(False)
        self.But_addition.setEnabled(False)
        self.But_subtraction.setEnabled(False)
        self.But_result.setEnabled(False)
        self.But_one_clear_symbol.setEnabled(False)

        self.anim_group.addAnimation(self.AnimationPanel)
        self.anim_group.addAnimation(self.AnimationTelegramButton)
        self.anim_group.addAnimation(self.AnimationGitHubButton)
        self.anim_group.addAnimation(self.AnimationCloseButton)
        self.anim_group.start()

    def PanelClose(self):
        self.AnimationPanel.setEndValue(QPoint(-300, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(-300, 100))
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(-300, 150))
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(-300, 30))
        self.AnimationCloseButton.setDuration(180)

        self.input.setEnabled(True)
        self.placeholder_answer_input.setEnabled(True)
        self.But_three.setEnabled(True)
        self.But_six.setEnabled(True)
        self.But_nine.setEnabled(True)
        self.But_division.setEnabled(True)
        self.But_multiplication.setEnabled(True)
        self.But_addition.setEnabled(True)
        self.But_subtraction.setEnabled(True)
        self.But_result.setEnabled(True)
        self.But_one_clear_symbol.setEnabled(True)

        self.anim_group.addAnimation(self.AnimationPanel)
        self.anim_group.addAnimation(self.AnimationTelegramButton)
        self.anim_group.addAnimation(self.AnimationGitHubButton)
        self.anim_group.addAnimation(self.AnimationCloseButton)
        self.anim_group.start()



    def openTelegramWebBrowser(self):
        webbrowser.open('https://t.me/ProgramsCreator/')

    def openGitHubWebBrowser(self):
        webbrowser.open('https://github.com/Shedrjoinzz')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(450, 700)
    window.show()
    sys.exit(app.exec_())
