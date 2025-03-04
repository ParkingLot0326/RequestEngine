from PyQt5.QtWidgets import *

from Method import Method

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.setWindowTitle("Hello World!")
        self.setFixedSize(500, 500)
        
        self.main_layout = QGridLayout(self)
        self.setStyleSheet(
            """
            QLineEdit {
                border: 1px solid black;
                height: 20px;
            }
            """
            )
        
        self.url_input = QLineEdit()
        self.submit_btn = QPushButton("Submit")
        
        self.input2 = QLineEdit()
        
        self.form = QFormLayout()
        self.form.addRow("Query", self.input2)
        
        self.tabbar = QTabBar()
        self.tabbar.addTab("headers")
        self.tabbar.addTab("body")
        self.tabbar.addTab("query")
        
        self.methodSelecter = QComboBox()
        self.methodSelecter.addItems(Method.__members__)
        
        self.main_layout.addWidget(self.methodSelecter, 0, 0, 1, 1)
        self.main_layout.addWidget(self.url_input, 0, 1, 1, 1)
        self.main_layout.addWidget(self.submit_btn, 0, 2, 1, 1)
        
        self.main_layout.addWidget(self.tabbar, 1, 0, 1, 2)
        self.main_layout.addLayout(self.form, 2, 0, 1, 2)
        
        self.main_layout = QVBoxLayout()
        # self.main_layout.addWidget(self.input1)
        # self.main_layout.addWidget(self.input2)
        
        