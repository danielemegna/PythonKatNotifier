import urllib

class KatSearch:

  protocol = "http"
  katDomain = "kat.cr"

  def __init__(self):
    self.includedWords = []
    self.excludedWords = []
    self.category = None
    self.minSeeds = None

  def include(self, word):
    self.includedWords.append(word)
    return self

  def exclude(self, word):
    self.excludedWords.append(word)
    return self

  def inCategory(self, category):
    self.category = category
    return self

  def withMinSeeds(self, minSeeds):
    self.minSeeds = minSeeds
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
    return "{}://{}/usearch/{}".format(self.protocol, self.katDomain, keywords)
