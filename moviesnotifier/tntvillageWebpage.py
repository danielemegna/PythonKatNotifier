import re
from pyquery import PyQuery as pq
from . import Movie, Webpage

class TntvillageWebpage(Webpage):

  def _rowsCssRule(self):
    return "channel item"

  def _from_row(self, row):
    row = pq(row)
    title = row("title").text()
    seeders = self._seeders_from(row)
    return Movie(title, seeders)

  def _seeders_from(self, row):
    description = row("description").text()
    seedersSearch = re.search(r'Torrent Data: Seeders\<b\> ([0-9]+)', description)
    if seedersSearch: return int(seedersSearch.group(1))
    else: return 1

class TntvillageWebpageFactory:

  def __init__(self, htmlRetriever):
    self.htmlRetriever = htmlRetriever
    return

  def build(self):
    html = self.htmlRetriever.get("http://www.tntvillage.scambioetico.org/rss.php?c=0&p=20")
    return TntvillageWebpage(html)
