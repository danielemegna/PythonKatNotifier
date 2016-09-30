from bs4 import BeautifulSoup
from . import Movie

class Webpage:

  def __init__(self, html):
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    tags = self.soup.select("a.tab")
    return map(self.__from_tag, tags)

  def __from_tag(self, tag):
    if(tag.strong):
      tag.strong.unwrap()

    title = ''.join(tag.contents).encode('ascii', 'ignore')
    return Movie(title)
