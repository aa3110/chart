from PyQt5.QtWidgets import QToolButton

def qtb(self,tab1,co1,i):    
  a1='self.btn' + str(i)
  
  v1 = {}  
  v1[a1] = QToolButton(tab1)
  v1[a1].move(i*100-100,20)
  v1[a1].setText("chkbox_"+str(i))
  v1[a1].clicked.connect(co1)
  globals().update(v1) 
  return v1[a1]