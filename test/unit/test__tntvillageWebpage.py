# -*- coding: utf-8 -*-

import unittest
from . import UnitTestBase
from moviesnotifier import TntvillageWebpage

class TntvillageWebpageTest(UnitTestBase):

  def setUp(self):
    html = self._read_file('tntvillage_example1.html')
    self.page = TntvillageWebpage(html)

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 20)

  def test_recognizeMovieTitles(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].title, "Le Onde del Destino (1996) [BDmux 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng]")
    self.assertEqual(movies[1].title, u"Mister Felicità (2017) [XviD - Ita Mp3]")
    self.assertEqual(movies[11].title, "Passengers 4K HDR (2016) [BDmux 2160p - H265 - Ita Eng Ac3 5.1 - MultiSub]")
    self.assertEqual(movies[19].title, "Il GGG - Il Grande Gigante Gentile (2016) [BDmux 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]")

  def test_recognizeSeeds(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].seeds, 1)
    self.assertEqual(movies[1].seeds, 77)
    self.assertEqual(movies[12].seeds, 46)
    self.assertEqual(movies[18].seeds, 107)
