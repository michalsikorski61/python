import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

# loader = QUiLoader()
# app = QApplication(sys.argv)

# window = loader.load("mainwindows.ui", None)
# window.show()
# app.exec()

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        #initialize widgets
        self.window = QWidget()
        self.window.btn_lower = QPushButton()
        
        #load ui
        loader = QUiLoader()
        self.window = loader.load("mainwindows.ui",self)
        #connect signals
        self.window.btn_lower.clicked.connect(self.test)
        
        #show
        self.show()
     
    @Slot()
    def test(self):
        print("lalala")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())