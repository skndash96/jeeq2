import re;
import json;
from urllib.request import urlopen;
from urllib.error import HTTPError, URLError;
from get import get_url, get_json;
from errors import *;
import traceback;

########################################

def iter_chap(info, rng):
  (klas, sub, chap, topic) = info
  qs = []
  
  for ques in rng:
    try:
      url = get_url(*info, ques)
      data = get_json(url)
      
      if data != None:
        qs.append(change(info, data))
        
    except TimeoutError:
      write_err(info, ques)
      print("Request timeout")
      
    except (HTTPError, URLError) as error:
      write_err(info, ques)
      print("Urllib error: %s", error.reason)
      
    except (NoData, NoSuchTopic, NoCssForImage) as error:
      write_err(info, ques)
      error.log()
      
    except Exception as e:
      write_err(info, ques)
      print(traceback.format_exc())
   
    except Exception:
      pass
    
    finally:
      print(f'{klas} {sub} {chap:02} {ques:03}', end='\r')
    
  return qs

########################################


def write_err(info, ques):
  open("coll/e.txt", "a").write(
    "{0} {1} {2} {4} {3}\n".format(*info, ques)
  )

########################################


def change(info, q):
  q = q["hasPart"]
  q = {k: q[k] for k in {
    "text",
    "encodingFormat",
    "suggestedAnswer",
    "acceptedAnswer",
    "styles"
  }}
  
  q["id"] = "{0}{1}{2}".format(*info) #take first 3 tuple items: klas, sub, chap
  q["topic"] = info[3]
  
  return q

########################################
