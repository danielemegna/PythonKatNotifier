from bs4 import BeautifulSoup
from . import Movie

class KatPage:

  def __init__(self, html):
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    tags = self.__extract_movie_tags()
    return Movie.tags_to_array(tags)

  def __extract_movie_tags(self):
    return self.soup.find_all("a", class_="cellMainLink")


