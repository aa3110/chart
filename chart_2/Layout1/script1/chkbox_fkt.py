from tkinter import Tk,Checkbutton,Button,Spinbox,IntVar
from functools import partial
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from p__init__ import plot_bb52s,pl_pix
from t__init__ import multisma,multibb,multiaroon,multicci,multirmx,multigap

fkt=[]

def r2(self):  
  ee=len(self.da2)
  
  for i3 in range(ee): fkt.append(eval(self.da2['name'][i3]))  
  var=[];[var.append([]) for i in range(3)] 
 
   
  def set_all():
    [var[0][i].set(0) for i in range(ee)]      
    [[var[j][i].set(self.sval[0]) for j in range(1,3)] for i in range(ee)]
    return var  
  
  def func(i):
    
    x1=self.df['Date'][self.plr[0]:self.plr[1]].index.values
    p0= self.plr[0]; p1= self.plr[1]
    t=[];[t.append([]) for i in range(4)]    
  
    for i2 in range(ee):      
      if var[0][i2].get() == 1: 
        for j2 in range(1,3): 
          t[0]=fkt[i2](self.df,'Close',var[j2][i2].get())           
          if i2<4 : t[1]+=t[0]
          if i2==4 : t[2]+=t[0]
          if i2==5: t[3]+=t[0] 
    for i in range(1,4): t[i]=list(set(t[i]))      
          
    fig = plt.figure(figsize=(12,10),dpi=300)
    ax1 = fig.add_subplot(111); ax2 = ax1.twinx() ; ax3 = ax1.twinx()   
    
    ax1.plot(x1, self.df['Close'][p0:p1]) 
    [ax1.plot(x1, self.df[y0][p0:p1]) for y0 in t[1]]
    if m1.get()==1:
      [ax1.plot(x1, self.df[y0][p0:p1]) for y0 in t[2]]
      [ax1.plot(x1, self.df[y0][p0:p1]) for y0 in t[3]] 
    else:
      [ax2.plot(x1, self.df[y0][p0:p1]) for y0 in t[2]]
      [ax3.plot(x1, self.df[y0][p0:p1]) for y0 in t[3]] 
         
    pic=pl_pix(plt);self.lab1.setPixmap(QPixmap(pic))
     
  app = Tk()  
  [var[j].append(IntVar()) for j in range(3) for i in range(ee)] 
  m1=IntVar() 
    
  for i in range(ee):    
    Checkbutton(app, text=self.da2['name'][i], variable=var[0][i], command=partial(func, i)).grid(row=i, column=0)
    [Spinbox(app, values=self.sval,width=5,textvariable=var[j][i],wrap=True).grid(row=i,column=j,padx=2,pady=2)  for j in range(1,3)]   
  #error
  Checkbutton(app, text='below', variable=m1,bg="yellow").grid(row=7, column=0)
  Button(app, text='Quit', command=app.destroy,bg="red").grid(row=6, column=5)
  Button(app, text='reset', command = set_all,bg="cyan").grid(row=7, column=5)  
  app.mainloop() 