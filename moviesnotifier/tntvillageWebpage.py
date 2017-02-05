from pyquery import PyQuery as pq
from . import Movie

class TntvillageWebpage:

  def __init__(self, html):
    self.html = pq(html)
    return

  def movies(self):
    rows = self.html("tr.odd, tr.odd2")
    return map(self.__from_row, rows)

  def __from_row(self, row):
    row = pq(row)

    title = row("td:nth-child(2) a").text()
    seeds = row("td:nth-child(6) font").text()
    
    try:
      intSeeds = int(seeds)
    except ValueError:
      intSeeds = 0
    
    return Movie(title, intSeeds)

class TntvillageWebpageFactory:

  def __init__(self, htmlRetriever):
    self.htmlRetriever = htmlRetriever
    return

  def build(self):
    html = self.htmlRetriever.get("....")
    return TntvillageWebpage(html)
