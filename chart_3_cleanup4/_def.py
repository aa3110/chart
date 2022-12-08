def a0(): print('34')
def a1(): print('dsfs')
def a2(): print('121')
def a3(): print('yxc')
# a = [None] * 4


def w1(n1=1):  
  a = [None] * n1
  for i in range(n1): a[i]='a'+str(i)+'()'
  [eval(a[i]) for i in range(n1)]

w1(2)
