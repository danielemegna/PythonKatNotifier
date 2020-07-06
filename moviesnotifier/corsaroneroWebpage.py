from pyquery import PyQuery as pq
from . import Movie
from . import Webpage

class CorsaroneroWebpage(Webpage):

  def _rowsCssRule(self):
    return "tr.odd, tr.odd2"

  def _from_row(self, row):
    row = pq(row)
    title = row("td:nth-child(2) a").text()
    seeds = row("td:nth-child(6) font").text()
    
    try:
      intSeeds = int(seeds)
    except ValueError:
      intSeeds = 0
    
    return Movie(title, intSeeds)

class CorsaroneroWebpageFactory:

  def __init__(self, htmlRetriever):
    self.htmlRetriever = htmlRetriever
    return

  def build(self):
    html = self.htmlRetriever.get("https://ilcorsaronero.link/cat/1")
    return CorsaroneroWebpage(html)
