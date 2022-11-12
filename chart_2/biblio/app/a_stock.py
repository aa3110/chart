from pathlib import Path
import os
from f__init__ import file_read

path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")
 
def stock_read(df='',stock='SIE',sel=0):
  df=file_read(stock)  
  return df