from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

def ql(self,tab1,p1,w,h,i):
  a1='self.lab' + str(i)
  
  v1 = {}  
  v1[a1] = QLabel(tab1)  
  v1[a1].setGeometry(0, 50, w, h)
  v1[a1].setPixmap(QPixmap(p1))
  v1[a1].setScaledContents(True)
  globals().update(v1)
  return v1[a1]