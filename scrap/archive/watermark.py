from PIL import Image, ImageEnhance
from os import listdir

def watermark(code):
  paths = listdir(f"coll/pics{code}")
  print(paths)
  
  for path in paths:
    path = f'coll/pics{code}/{path}'
    i = Image.open(path).convert('RGBA')
    
    i = ImageEnhance.Brightness(i).enhance(1.1)
    i.save(path)
    
    i = Image.open(path)
    i = ImageEnhance.Contrast(i).enhance(5)
    
    i.save(path)
    print("done", path)

watermark("12")