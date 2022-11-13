import matplotlib.pyplot as plt
import io
from PIL import Image
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

def pl_pix(plt=''):
  buf = io.BytesIO(); plt.savefig(buf, format='png')
  buf.seek(0); im = Image.open(buf)
  qim = ImageQt(im); pix=QPixmap.fromImage(qim) 
  return pix