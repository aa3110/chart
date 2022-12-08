from t_sma import sma

def dema(df=None,a1='Close',val1=None):
  b1='dema'+str(val1);b2='tema'+str(val1);b3='qema'+str(val1)
  df[b1]=sma(df,a1,val1)
  df[b2]=sma(df,b1,val1)
  df[b3]=sma(df,b2,val1)
  return df[b1],df[b2],df[b3]

def multidema(df=None,a1='Close',*va):
  k1=[]
  for value in va:
    for i2 in range(3): j=(dema(df,a1,value)[i2]).name;k1.append(j) 
  return k1