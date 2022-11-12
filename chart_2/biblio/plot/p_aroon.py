

def plot_aroon1(st1='CCI',st2='Closehigh',st3='Close',df=None):
  fig, ax = plt.subplots()
  
  t=df['Date'].index.values.astype(int)
  
  
  ax.set_xlabel('Date')
    
  color1 = 'tab:green'
  ax.set_ylabel(st1, color=color1)
  ax.plot(t[plr[0]:plr[1]], df[st1][plr[0]:plr[1]], color=color1,linewidth=1.0)
  ax.tick_params(axis='y', labelcolor=color1)
  
  color2 = 'tab:cyan'
  ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
  ax2.set_ylabel(st2, color=color2)  # we already handled the x-label with ax
  ax2.plot(t[plr[0]:plr[1]], df[st2][plr[0]:plr[1]], color=color2,linewidth=0.5)
  ax2.tick_params(axis='y', labelcolor=color2)
  
  fig.tight_layout()  # otherwise the right y-label is slightly clipped
  
  if st3!=0 :  
    color3 = 'tab:blue'
    ax3 = ax.twinx()
    ax3.set_ylabel(st3, color=color3)
    ax3.spines['right'].set_position(('outward', 40))
    ax3.plot(t[plr[0]:plr[1]], df[st3][plr[0]:plr[1]], color=color3,linewidth=1.0)
    ax3.tick_params(axis='y', labelcolor=color3)
    plt.savefig(dir_p+st1+st2+st3, dpi=100)
  else :
    plt.savefig(dir_p+st1+st2, dpi=100)  
  return