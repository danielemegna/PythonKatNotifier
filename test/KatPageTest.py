import unittest
from bs4 import BeautifulSoup

class KatPage:

  def __init__(self, html):
    self.html = html
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    return self.soup.find_all("a", class_="cellMainLink")

class KatPageTest(unittest.TestCase):

  def test_recognizeCorrectlyNumberOfMovies(self):
    html = self.read_file('test/katPage.html')
    page = KatPage(html) 
    movies = page.movies()
    self.assertEqual(len(movies), 12)

  def read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html


if __name__ == '__main__':
  unittest.main()
