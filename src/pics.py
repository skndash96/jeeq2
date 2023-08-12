from iter import iter_chap;
from urllib.request import urlretrieve;
import json, re;

d = json.load(open("topics.json", "r"));

def pics(klas, sub):
  code = f"{klas}{sub}"
  
  klas_url = ("xi", "xii")[klas]
  klas = ("11", "12")[klas]

  sub_url = ("phy", "chem", "math")[sub]
  sub = ("physics", "chemistry", "math")[sub]
  
  j = json.load(open(f'coll/{code}.json'))

  for chap in d[klas][sub]:
    for q in j:
      if q["topic"] == chap[0] and q["styles"] != "":
        names = re.findall(
          r'url\((.+?\.png)\)',
          q["styles"]
        )
        names = set(names)
        
        if len(names) == 0:
          continue
        
        for name in names:
          try:
            url = "https://examsnet.github.io/cdn/img/jee/mains/chap/%s/%s/%s" % (sub_url, klas_url, name)
            
            urlretrieve(
              url,
              f'coll/pics{code}/{name}'
            )
            
            print(name)
            
          except Exception as e:
            print(e, url)
        
        break