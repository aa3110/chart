from pathlib import Path
import os,sys

d1=("app","file","plot","trade","serie","const")
for i1 in d1:
  i1="biblio\\"+i1
  path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+"\\").parent.parent.parent, i1)
  if (path not in  sys.path) : sys.path.append(path)
  
i1="inout"
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+"\\").parent.parent.parent, i1)
if (path not in  sys.path) : sys.path.append(path)