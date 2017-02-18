import unittest
from moviesnotifier import (TntvillageWebpageFactory, UrlLibHtmlRetriever)

class TntvillageWebpageTest(unittest.TestCase):

  def setUp(self):
    factory = TntvillageWebpageFactory(UrlLibHtmlRetriever())
    self.page = factory.build()

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 20)
