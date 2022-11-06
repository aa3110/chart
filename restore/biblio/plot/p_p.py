import matplotlib.pyplot as plt

def plot_b2s(self,df='',*argv):
  for i2 in argv:
    df[i2][self.plr[0]:self.plr[1]].plot(linewidth=1.0)
    plt.legend(argv)
  return plt
