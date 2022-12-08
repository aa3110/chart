import matplotlib.pyplot as plt

def plot_bb52s(self,df='',*argv):
  [df[i2][self.plr[0]:self.plr[1]].plot(linewidth=0.5) for i2 in argv] 
  # plt.legend(['Close',argv])   
  return plt