def multigap(df=None,a1='Close',*va):
  a2='Open'; df[a1+a2]=((df[a1]-df[a2])*2)+df['Close'] 
  return [a1+a2]