class NoData(Exception):
  def __init__(self, url):
    self.url = url
  
  def log(self):
    print("No data was found for %s" % self.url)

class NoSuchTopic(Exception):
  def __init__(self, info):
    self.info = info
  
  def log(self):
    print("No such topic was found in json:\nclass: %s\nsubject: %s\ntopic: %s" % self.info)

class NoCssForImage(Exception):
  def __init__(self, url):
    self.url = url
  
  def log(self):
    print("No css code was found for existing span images %s" % self.url)