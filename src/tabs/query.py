from PyQt5.QtWidgets import QWidget

class QueryTab(QWidget) :
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self): ...
    
    def add_one_entry(self): ...