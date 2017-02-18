from pyquery import PyQuery as pq
from . import Movie

class TntvillageWebpage:

  def __init__(self, html):
    self.html = pq(html)
    return

  def movies(self):
    rows = self.html("channel item")
    return map(self.__from_row, rows)

  def __from_row(self, row):
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
