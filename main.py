
from PySide6.QtWidgets import QApplication,QMainWindow
from UI.main_ui import Ui_MainWindow
from logic import Convert
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.trigger.clicked.connect(self.proccess)
    def proccess(self):
        self.fromm = self.ui.fromm.text()
        self.to = self.ui.to.text()
        self.value = self.ui.sum.text()
        self.result = Convert(self.fromm,self.to,self.value)
        self.ui.result.setText(str(round(self.result,2)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.setFixedSize(600,600)
    window.show()
    sys.exit(app.exec())