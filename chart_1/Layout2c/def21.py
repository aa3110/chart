from script21.chkbox_st import r1
from script21.chkbox_indr5 import r2
from script21.chkbox_set10 import r3
from script21.chkbox_set1 import r4

def c1(self):
  r1(self) 
  return self.statusBar().showMessage('done: chkbox_st')

def c2(self):
  r2(self)
  return self.statusBar().showMessage('done: chkbox_ind')

def c3(self):
  r3(self) 
  return self.statusBar().showMessage('done: plot size')

def c4(self):
  r4(self) 
  return self.statusBar().showMessage('done: settings')

def c5(self):
  from _another import AnotherWindow
  self.xa = AnotherWindow();self.xa.show()
  return self.statusBar().showMessage('done: AnotherWindow')