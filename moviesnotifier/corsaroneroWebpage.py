from pyquery import PyQuery as pq
from . import Movie

class CorsaroneroWebpage:

  def __init__(self, html):
    self.html = pq(html)
    return

  def movies(self, filterPolicy = None):
    rows = self.html("tr.odd, tr.odd2")
    movies = map(self.__from_row, rows)

    if(filterPolicy is not None):
      return filterPolicy.filter(movies)

    return movies

  def __from_row(self, row):
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
    html = self.htmlRetriever.get("http://ilcorsaronero.info/cat/1")
    return CorsaroneroWebpage(html)
