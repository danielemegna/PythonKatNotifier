import unittest
from moviesnotifier import (TntvillageWebpage, UrlLibHtmlRetriever)

class TntvillageWebpageTest(unittest.TestCase):

  def setUp(self):
    htmlRetriever = UrlLibHtmlRetriever()
    source = htmlRetriever.get("http://www.tntvillage.scambioetico.org/src/releaselist.php")
    html = self._read_file(source)
    self.page = TntvillageWebpage(html)

  def xtest_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 20)
