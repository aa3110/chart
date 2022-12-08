from f__init__ import file_read

def cha(df='',s1=''): 
  for i in s1:
    da=file_read(i); df[i]=da['Close'] 
  return df