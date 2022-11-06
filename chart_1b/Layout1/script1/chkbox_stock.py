from tkinter import Tk, Checkbutton, IntVar,Button
from functools import partial
from a__init__ import stock_read

def r1(self): 
  
  def func(i):
      if var1[i].get() == 1: self.df=stock_read('',self.sto1[i],self.sel1)
                                
  def set_all(value): [v.set(value) for v in var1]
    
  var1 = []  
  app = Tk()
  
  lis1=self.sto1
  
  for i,fu in enumerate(lis1):
    var1.append(IntVar())
    Checkbutton(app, text=f'{fu} {i}', variable=var1[i], pady=0, command=partial(func, i)).grid(row=i%3, column=i//3)
      
  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=2, column=i+1)
  Button(app, text='reset', command = partial(set_all, False),bg="cyan").grid(row=3, column=i+1)
   
  app.mainloop()