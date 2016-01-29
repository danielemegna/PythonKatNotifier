import unittest
from bs4 import BeautifulSoup

class KatPage:

  def __init__(self, html):
    self.html = html
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    found = self.soup.find_all("a", class_="cellMainLink")

    movies = []
    for movie in found:
      movie.strong.unwrap()
      movies.append(''.join(movie.contents))

    return movies


class KatPageTest(unittest.TestCase):

  def test_recognizeCorrectlyNumberOfMovies(self):
    html = self.read_file('test/katPage.html')
    page = KatPage(html)
    movies = page.movies()
    self.assertEqual(len(movies), 12)

  def test_readCorrectlyMovieTitles(self):
    html = self.read_file('test/katPage.html')
    page = KatPage(html)
    movies = page.movies()
    self.assertEqual(movies[0], # todo -> this will be 'movies[0].title'
      "Son Of A Gun (2014) BRrip XviD - Italian English Ac3 5 1 Sub ita eng MIRCrew"
    );

  def read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html


if __name__ == '__main__':
  unittest.main()
