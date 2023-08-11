from iter import iter_chap;
import json;

def main():
  klas, sub, chap = 0,0,0
  rng, topic = [], ""
  
  file = "coll/%s%s.json" % (klas, sub)
  
  qs = iter_chap((
    klas, sub, chap,
    topic
  ), rng)
  
  print(len(qs))
  
  data = json.load(open(file))
  
  print(len(data))
  data.extend(qs)
  print(len(data))
  
  json.dump(data, open(file, "w"))
  
  print(f"saved at {file}")

main()