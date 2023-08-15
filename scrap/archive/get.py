from urllib.request import urlopen;
import json;
import re;
from socket import timeout;
from errors import *;

#3333333333333333333333333333333333333


def get_url(klas, sub, chap, topic, qn):
  klas_codes = ("11", "12")
  sub_codes = ("physics", "chemistry", "math")

  try:
    title = "-".join(re.split(
      "\s+",
      topic
    )).lower()
    
    url = f"https://examsnet.com/test/jee-main-{sub_codes[sub]}-class-{klas_codes[klas]}--{title}--questions/q-{qn}/"
    
    return url
  except (KeyError, IndexError) as error:
    raise NoSuchTopic((klas, sub, topic))


#3333333333333333333333333333333333333

def get_json(url):
  res = urlopen(url, timeout=20).read().decode('utf-8')
  
  data = None
  
  # find question json script
  j = re.findall(r'<script type=".+?">([\s\S]+?)</script>', res, re.MULTILINE)
  for x in j:
    if "hasPart" in x:
      data = json.loads(x)
      break
  
  if data == None or "text" not in data["hasPart"]: 
    raise NoData(url)
  
  # find sprites if any in the question markup
  sprites = re.findall(
    r'<span class="sprite\s+(.+?)\s*"',
    data["hasPart"]["text"]
  )
  
  # find css file for sprites
  css = re.findall(
    '<link.*?href=[\'\"](.*?examsnet\.github\.io.*?)[\'\"].*?>',
    res,
    re.MULTILINE
  )
  
  # read css file and extract sprite position
  if len(css) != 0:
    styles = urlopen(css[-1], timeout=10).read().decode('utf-8')
    
    data["hasPart"]["styles"] = ""
    
    for img in sprites:
      data["hasPart"]["styles"] += "\n".join(re.findall(
        f'{img}.+?{{.+?\}}',
        styles,
        re.MULTILINE
      )) + "\n"
      
  elif len(sprites) != 0:
    raise NoCssForImage(url)
  
  return data
  
  
#33333333333333333333
