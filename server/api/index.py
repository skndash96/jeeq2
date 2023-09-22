import random, os, json, re;
from flask import Flask, request, abort;
from flask_cors import CORS;

ERR400 = "Recieved inputs are not customary "

topics = json.load(open("topics.json"))
Db = {
  "00": json.load(open("coll/00.json")),
  "01": json.load(open("coll/01.json")),
  "02": json.load(open("coll/02.json")),
  "10": json.load(open("coll/10.json")),
  "11": json.load(open("coll/11.json")),
  "12": json.load(open("coll/12.json"))
}

app = Flask(__name__)
CORS(app)

# @app.before_request
def middle():
  sessions = []
  
  headers = request.headers
  print(rewrequest.headers['Authorization'])
  
  try:
    cred, tokn = re.split(' ', headers.get("Authorization", ""))
    
    print("cred", cred, "token", token)
    
    if tokn:
      pass
    else:
      abort(400, "No Authorization")
  
  except Exception as e:
    abort(400, "Unable to parse Authorization")
  
  # response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
  # response.headers['Content-Security-Policy'] = "default-src 'self'"
  # response.headers['X-Content-Type-Options'] = 'nosniff'
  

@app.route("/")
def home():
  return "Hello, people! Btw, this isn't where you should be."

@app.route("/getq")
def get_q():
  args = request.args;
  
  klas = args.get("klas") or None
  sub = args.get("sub") or None
  chap = args.get("chap") or None
  n = args.get("num", 1)
  qno = args.get("qno") or None
  code = None

  try:
    n = int(n)
    
    if qno:
      qno = int(qno)
    if klas:
      klas = max(0, min(int(klas), 1))
    if sub:
      sub = max(0, min(int(sub), 2))
    if n > 90:
      raise ValueError()
    if chap:
      code = f"{klas}{sub}"
      
      chap = random.choice(
        re.split(",", chap)
      )
      
      chap = max(0, min(int(chap), len(topics[code]) - 1))
    
  except (ValueError, KeyError):
    abort(400, ERR400)
  
  qs = []
  
  for i in range(n):
    if klas == None :
      klas = random.randint(0,1)
    if sub == None:
      sub = random.randint(0,2)
    
    data = Db.get(f"{klas}{sub}", None)
    
    if chap != None:
      [d_start, d_end] = topics[code][chap][1]
      data = data[d_start:d_end]
    
    if qno:
      q_idx = qno + n
      if q_idx > len(data) - 1:
        break
    else:
      q_idx = random.randint(0, len(data)-1)
    
    q = data[q_idx]
    if qno:
      q["qno"] = qno+n
    
    qs.append( q )
  
  return qs
