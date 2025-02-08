from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.login_line_edit = None
        
        self.setup()
    
    def setup(self):
        width = 400
        pix_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\PECET\\Pictures\\angry_graphy_gumis.png").scaled(240,240)
        pix_label.setPixmap(pixmap)
        pix_label.move((width - 240)/2,50)
        
        self.login_line_edit = QLineEdit("Login", self)
        self.login_line_edit.setFixedWidth(200)
        self.login_line_edit.move(100,350)
        
        pass_line_edit = QLineEdit("Password", self)
        pass_line_edit.setFixedWidth(200)
        pass_line_edit.move(100,390)
        
        submit_btn = QPushButton("Submit",self)
        submit_btn.move((width - submit_btn.size().width())/2,420)
        submit_btn.clicked.connect(self.submit) #without brackets to prevent autotrigger
        
        quit_btn = QPushButton("Quit", self)
        quit_btn.move(320,570) #  x,y
        quit_btn.clicked.connect(QApplication.instance().quit)
        self.setFixedSize(width, 600) #width, height
        self.setWindowTitle("Login Window")

        self.show()
    
    def submit(self):
        print(self.login_line_edit.text())
    
    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self,"Close App","Do you want to close?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication([])
    
    # login window
    login_window = LoginWindow()
    
    app.exec() # run program