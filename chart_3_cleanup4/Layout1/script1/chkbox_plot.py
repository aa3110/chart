from functools import partial
from tkinter import Tk,Button,Spinbox,IntVar

def r2(self):
  var=[];[var.append([]) for i in range(2)]
  
  def set_all(): 
    var[0].set(500);var[1].set(700) 
    return var
  
  def plr2():     
    for i in range(2): self.plr[i]=int(var[i].get())    
          
  app = Tk();app.geometry("130x100");app.title("plot range")
  for j in range(2): var[j]=IntVar()
  
  var=set_all()
  [Spinbox(app, from_=0,to=800,increment=10,width=5,textvariable=var[i1],command=plr2,wrap=True).grid(row=1,column=i1+1,padx=10,pady=10) for i1 in range(2)]
   
  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=2, column=2)
  Button(app, text='reset', command = set_all,bg="cyan").grid(row=3, column=2)
 
  app.mainloop()