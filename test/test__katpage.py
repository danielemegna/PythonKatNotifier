import unittest
from katnotifier import KatPage

class KatPageTest(unittest.TestCase):

  def setUp(self):
    html = self.__read_file('test/kat_page_example1.html')
    self.page = KatPage(html)

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 12)

  def test_readCorrectlyMovieTitles(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].title,
      "Son Of A Gun (2014) BRrip XviD - Italian English Ac3 5 1 Sub ita eng MIRCrew"
    );
    self.assertEqual(movies[1].title,
      "Lo Stagista Inaspettato-The Intern 2015 iTALiAN BRRip XviD BLUWORLD"
    );
    self.assertEqual(movies[7].title,
      "Inside Out 2015 iTALiAN BDRip XviD-TRL[MT] avi"
    );

  def __read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html
