import urllib

class KatSearch:

  protocol = "http"
  katDomain = "kat.cr"

  def __init__(self, keywords):
    self.keywords = keywords

  def toUrl(self):
    return "{}://{}/usearch/{}".format(self.protocol, self.katDomain, urllib.quote(self.keywords))
