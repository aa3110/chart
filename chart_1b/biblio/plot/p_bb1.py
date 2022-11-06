import matplotlib.pyplot as plt
from p_p import plot_b2s

def plot_bb52s(self,df='',*argv,**kwargs):
  plot_b2s(self,df,*argv)  
  plt.legend(['Close',argv,kwargs.values()])   
  return plt