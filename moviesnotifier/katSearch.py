import urllib

class KatSearch:

  def __init__(self):
    self.protocol = "http"
    self.katDomain = "kat.cr"
    self.includedWords = []
    self.excludedWords = []
    self.category = None
    self.minSeeds = None
    self.orderByField = None

  def include(self, words):
    self.includedWords += words.split()
    return self

  def exclude(self, words):
    self.excludedWords += words.split()
    return self

  def inCategory(self, category):
    self.category = category
    return self

  def withMinSeeds(self, minSeeds):
    self.minSeeds = minSeeds
    return self

  def orderBy(self, field, order):
    self.orderByField = (field, order)
    return self

  def toUrl(self):
    if(len(self.includedWords) > 0):
      keywords = " ".join(self.includedWords) + " "
    if(len(self.excludedWords) > 0):
      keywords += " ".join(map(lambda word: "-"+word, self.excludedWords)) + " "
      
    if(self.category is not None):
      keywords += "category:" + self.category + " "
    if(self.minSeeds is not None):
      keywords += "seeds:" + str(self.minSeeds) + " "

    keywords = keywords.strip()
    keywords = urllib.quote(keywords)

    orderClause = ""
    if(self.orderByField is not None):
      orderClause = "?field={}&sorder={}".format(*self.orderByField)
        

    return "{}://{}/usearch/{}/{}".format(self.protocol, self.katDomain, keywords, orderClause)
