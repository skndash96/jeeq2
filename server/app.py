import random;
from db import DB, topics;
from flask import Flask, redirect, request, abort;

ERR400 = "Recieved inputs are not customary "

app = Flask(__name__)

@app.route("/")
def home():
  return redirect("/getq", 200)

@app.route("/getq")
def get_q():
  args = request.args;
  
  klas = args.get("klas", None)
  sub = args.get("sub", None)
  chap = args.get("chap", None)
  n = args.get("num", 1)
  code = None

  try:
    n = int(n)
    if klas:
      klas = int(klas)
    if sub:
      sub = int(sub)
    if chap:
      chap = int(chap)
      code = f"{klas}{sub}"
      if chap < 0 or chap > len(topics[code]):
        raise ValueError
  except (ValueError, KeyError):
    abort(400, ERR400)
  
  qs = []
  
  for i in range(n):
    if not klas:
      klas = random.randint(0,1)
    if not sub:
      sub = random.randint(0,2)
    
    data = DB.get(f"{klas}{sub}", None)
    
    if chap:
      d_start, d_end = topics[code][chap][1:]
      data = data[d_start:d_end]
    
    q_idx = random.randint(0, len(data))
    qs.append( data[q_idx] )
  
  return qs