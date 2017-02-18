import unittest
from moviesnotifier import (CorsaroneroWebpageFactory, UrlLibHtmlRetriever)

class CorsaroneroWebpageTest(unittest.TestCase):

  def setUp(self):
    factory = CorsaroneroWebpageFactory(UrlLibHtmlRetriever())
    self.page = factory.build()

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 40)
