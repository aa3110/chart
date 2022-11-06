import path_def.pat1
from PyQt5.QtWidgets import QTabWidget,QWidget
from a__init__ import qtb,ql
from c__init__ import para,nb,sval,sto1,plr,start
from f__init__ import file_read
import pandas as pd

pic1="p1.png"
pic2="copyright.png"
pic3="p3.png"

def initUI(self):
  self.resize(1600, 800)
  
  self.tabs = QTabWidget()
  self.tabs.setMovable(True)
  
  self.tab1,self.tab2 = QWidget(),QWidget()
  self.tabs.addTab(self.tab1,"Chart");self.tabs.addTab(self.tab2,"Help")         
  self.setCentralWidget(self.tabs)
  
  self.lab1=ql(self,self.tab1,pic1,1900,900,1);self.lab1.move(-150, -50)  
  self.btn1=qtb(self,self.tab1,self.c1,1)
  self.btn2=qtb(self,self.tab1,self.c2,2)
  self.btn3=qtb(self,self.tab1,self.c3,3)
 
  self.lab2=ql(self,self.tab2,pic3,1900,900,1);self.lab2.move(-150, -50)
  self.lab2=ql(self,self.tab2,pic2,200,150,2);self.lab2.move(1380, 630)
  self.btn4=qtb(self,self.tab2,self.c4,4)
  self.btn5=qtb(self,self.tab2,self.c5,5)
  
  # data 
  self.df=''
  self.para,self.nb,self.sval,self.sto1,self.plr,self.start=para,nb,sval,sto1,plr,start
  self.sel1=0
  self.da2=file_read('c_com5')   
  