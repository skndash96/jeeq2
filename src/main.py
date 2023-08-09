import re;
import json;
from urllib.request import urlopen;
from urllib.error import HTTPError, URLError;
from get import klas_codes, sub_codes, get_url, get_json;
from errors import *;
import traceback;

def run():
  d = json.load(
    open("topics.json", "r")
  );
  
  klas, sub = 0, 2
  
  chaps = d[klas_codes[klas]][sub_codes[sub]]
  
  datas = []
  
  for chap, [topic, total] in enumerate(chaps):
    info = (klas, sub, chap, topic)
    
    for ques in range(1, total+1):
      try:
        data = get_q(info, ques)
      
        if data != None:
          datas.append(change(info, data))
      except Exception:
        pass
      finally:
        print(f'{klas} {sub} {chap:02} {ques:03}', end='\r')
        
    open("coll/%d%d.json" % (klas, sub), "w").write(
      json.dumps(datas)
    )
  
  
  print("Completed for class %s, subject %s" % (klas, sub))

def get_q(info, ques):
  try:
    url = get_url(*info, ques)
    data = get_json(url)
    
    return data
    
  except (HTTPError, URLError) as error:
    write_err(info, ques)
    print("Urllib error: %s", error.reason)
    
  except (NoData, NoSuchTopic, NoCssForImage) as error:
    write_err(info, ques)
    error.log()
  
  except Exception as e:
    write_err(info, ques)
    print(traceback.format_exc())

def write_err(info, ques):
  open("coll/e.txt", "a").write(
    "{0} {1} {2} {4} {3}\n".format(*info, ques)
  )

def change(info, data):
  data = data["hasPart"]
  data = {k: data[k] for k in {
    "text",
    "encodingFormat",
    "suggestedAnswer",
    "acceptedAnswer",
    "styles"
  }}
  
  data["id"] = "{0}{1}{2}".format(*info)
  data["topic"] = info[3]
  
  return data
  
run()
  