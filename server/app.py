import random;
from db import DB, topics;
from flask import Flask, redirect, request, abort;
from flask_cors import CORS;

ERR400 = "Recieved inputs are not customary "

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return redirect("/getq", 200)

@app.route("/getq")
def get_q():
  args = request.args;
  
  klas = args.get("klas", None) or None
  sub = args.get("sub", None) or None
  chap = args.get("chap", None) or None
  n = args.get("num", 1)
  code = None

  try:
    n = int(n)
    if klas:
      klas = max(0, min(int(klas), 1))
    if sub:
      sub = max(0, min(int(sub), 2))
    if chap:
      code = f"{klas}{sub}"
      chap = max(0, min(int(chap), len(topics[code]) - 1))
  except (ValueError, KeyError):
    abort(400, ERR400)
  
  qs = []
  
  for i in range(n):
    if klas == None :
      klas = random.randint(0,1)
    if sub == None:
      sub = random.randint(0,2)
    
    data = DB.get(f"{klas}{sub}", None)
    
    if chap:
      [d_start, d_end] = topics[code][chap][1]
      data = data[d_start:d_end]
    
    q_idx = random.randint(0, len(data)-1)
    qs.append( data[q_idx] )
  
  return qs