from PIL import Image, ImageEnhance
from os import listdir
from urllib.request import urlretrieve;
import json, re;

d = json.load(open("url_tops.json", "r"));

def pics(klas, sub):
  code = f"{klas}{sub}"
  
  klas_url = ("xi", "xii")[klas]
  klas = ("11", "12")[klas]

  sub_url = ("phy", "chem", "math")[sub]
  sub = ("physics", "chemistry", "math")[sub]
  
  j = json.load(open(f'coll/{code}.json'))
  dled = []

  for chap in d[code]:
    for q in j:
      if q["topic"] == chap[0] and q["styles"] != "":
        names = re.findall(
          r'url\((.+?\.png)\)',
          q["styles"]
        )
        names = set(names)
        
        for name in names:
          if name in dled:
            continue
          
          try:
            url = "https://examsnet.github.io/cdn/img/jee/mains/chap/%s/%s/%s" % (sub_url, klas_url, name)
            
            urlretrieve(
              url,
              f'coll/pics{code}/{name}'
            )
            
            dled.append(name)
            print(name)
          except Exception as e:
            print(e, url)
            
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