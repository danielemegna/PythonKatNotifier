import urllib

class KatSearch:

  protocol = "http"
  katDomain = "kat.cr"

  def __init__(self):
    self.includedWords = []
    self.excludedWords = []

  def include(self, word):
    self.includedWords.append(word)
    return self

  def exclude(self, word):
    self.excludedWords.append(word)
    return self

  def toUrl(self):
    keywords = " ".join(self.includedWords)
    keywords += " "
    keywords += " ".join(map(lambda word: "-"+word, self.excludedWords))
    keywords = keywords.strip()
    keywords = urllib.quote(keywords)
    return "{}://{}/usearch/{}".format(self.protocol, self.katDomain, keywords)
