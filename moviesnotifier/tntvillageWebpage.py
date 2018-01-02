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
  ANY_CATEGORY = '0'
  TV_SERIES_CATEGORY = '1'
  MUSIC_CATEGORY = '2'
  EBOOKS_CATEGORY = '2'
  FILM_CATEGORY = '4'

  def __init__(self, htmlRetriever):
    self.htmlRetriever = htmlRetriever
    return

  def build(self):
    category = self.FILM_CATEGORY
    resultCount = '40'
    url = "http://www.tntvillage.scambioetico.org/rss.php?c=" + category + "&p=" + resultCount
    html = self.htmlRetriever.get(url)
    return TntvillageWebpage(html)
