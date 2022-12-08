from tkinter import Tk,Checkbutton,Button,Spinbox,IntVar
from functools import partial
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
import random 
from p__init__ import plot_bb52s,pl_pix
from t__init__ import multisma,multibb,multiaroon,multicci,multirmx,multigap,multidema
from a_cha import cha
co1=('green','cyan','yellow','orange','purple')
fkt=[]

def r1(self):  
  ee=len(self.com3);e1=len(self.com1)
  var=[];[var.append([]) for i in range(3)]
  [fkt.append(eval(self.com3[i3])) for i3 in range(ee)]
  
  def st3(): 
    self.df=cha(self.df,self.sto2)
    func()
    return self.df
      
  def set_all():
    [var[0][i].set(0) for i in range(ee)]      
    [[var[j][i].set(self.sval[0]) for j in range(1,3)] for i in range(ee)]
    return var  
  
  def func():  
    p0,p1= self.plr[0],self.plr[1];t=[]
    x1=self.df['Date'][p0:p1].index.values   
    [t.append([]) for i in range(5)]
   
    def calc1():
      for i2 in range(ee):
        if var[0][i2].get() == 1: 
          for j2 in range(1,3): 
            t[0]=fkt[i2](self.df,'Close',var[j2][i2].get())             
            if i2<e1 : t[1]+=t[0] 
            if i2==e1 : t[2]+=t[0]
            if i2==e1+1 : t[3]+=t[0]
      for i in range(1,5): t[i]=list(set(t[i]))
            
    calc1()
   
    ax=[]; [ax.append([]) for i in range(5)]
      
    fig=plt.figure(figsize=(12,10),dpi=300); ax[0]=fig.add_subplot(111)
    for i in range(1,5): ax[i]=ax[0].twinx() 

    def pl_1(): 
      ax[0].plot(x1, self.df['Close'][p0:p1],color='blue')
      [ax[0].plot(x1, self.df[y0][p0:p1]) for y0 in t[1]]
    def pl_1a(): [[ax[i].plot(x1, self.df[y0][p0:p1],color=random.choice(co1)) for y0 in t[i]] for i in range(2,4)]
    def pl_1b(): [[ax[0].plot(x1, self.df[y0][p0:p1],color=random.choice(co1)) for y0 in t[i]] for i in range(2,4)]
    def dch1(): [ax[i].plot(x1, self.df[self.sto2[i]][p0:p1],color=co1[i]) for i in range(len(self.sto2))]
    def dch2(): [ax[0].plot(x1, self.df[self.sto2[i]][p0:p1],color=co1[i]) for i in range(len(self.sto2))]
     
    pl_1()  
    if bel1.get()==0: pl_1a()
    if bel1.get()==1: pl_1b()
    if ch1.get()==1: dch1()
    if ch2.get()==1: dch2()
     
    pic=pl_pix(plt);self.lab0.setPixmap(QPixmap(pic))
     
  app = Tk()
  [var[j].append(IntVar()) for j in range(3) for i in range(ee)] 
  bel1,ch1,ch2=IntVar(),IntVar(),IntVar()
    
  for i in range(ee):  
    Checkbutton(app, text=self.com3[i], variable=var[0][i], command=partial(func)).grid(row=i, column=0)
    [Spinbox(app, values=self.sval,width=5,textvariable=var[j][i],wrap=True).grid(row=i,column=j,padx=2,pady=2)  for j in range(1,3)]   
  Checkbutton(app, text='cha', variable=ch1, command=st3).grid(row=i+1, column=0)
  Checkbutton(app, text='cha2', variable=ch2, command=st3).grid(row=i+1, column=1)
 
  Checkbutton(app, text='below', variable=bel1,bg="yellow").grid(row=i+2, column=0)
  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=i+1, column=5)
  Button(app, text='reset', command = set_all,bg="cyan").grid(row=i+2, column=5)  
  app.mainloop() 