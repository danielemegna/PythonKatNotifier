from pyquery import PyQuery as pq
from . import Movie
from . import Webpage

class TntvillageWebpage(Webpage):

  def _rowsCssRule(self):
    return "channel item"

  def _from_row(self, row):
    row = pq(row)
    title = row("title").text()
    return Movie(title, 1)

class TntvillageWebpageFactory:

  def __init__(self, htmlRetriever):
    self.htmlRetriever = htmlRetriever
    return

  def build(self):
    html = self.htmlRetriever.get("http://www.tntvillage.scambioetico.org/rss.php?c=0&p=20")
    return TntvillageWebpage(html)
