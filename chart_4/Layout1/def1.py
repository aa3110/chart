from script1.chkbox_stock import r0
from script1.chkbox_fkt import r1
from script1.chkbox_update import r2

def c0(self): r0(self)
def c1(self): r1(self)  
def c2(self): r2(self)  

def c3(self):
  from _another import AnotherWindow
  self.xa = AnotherWindow();self.xa.show()
  return self.statusBar().showMessage('done: AnotherWindow')