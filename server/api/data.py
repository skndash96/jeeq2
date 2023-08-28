import json;

topics = json.load(open("topics.json"))
Db = {
  "00": json.load(open("coll/00.json")),
  "01": json.load(open("coll/01.json")),
  "02": json.load(open("coll/02.json")),
  "10": json.load(open("coll/10.json")),
  "11": json.load(open("coll/11.json")),
  "12": json.load(open("coll/12.json"))
}