from pyquery import PyQuery as pq

class Webpage:

  def __init__(self, html):
    self.html = pq(html)
    return

  def movies(self, filterPolicy = None):
    rows = self.html(self._rowsCssRule())
    movies = map(self._from_row, rows)

    if(filterPolicy is not None):
      return filterPolicy.filter(movies)
    
    return movies

  def _rowsCssRule(self):
    raise NotImplementedError("You're calling an abstract class!")

  def _from_row(self, row):
    raise NotImplementedError("You're calling an abstract class!")
