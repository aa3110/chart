import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#import path_def.pat1
import path_def.pat2

class MW(QMainWindow):
    def __init__(self):
      super().__init__() ; self.initUI()
      
    from initUI21 import initUI  
    from def21 import c1,c2,c3,c4,c5
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MW() ; win.show()
  sys.exit(app.exec_())