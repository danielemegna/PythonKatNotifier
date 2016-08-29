from . import UnitTestBase
from moviesnotifier import KatPage

class KatPageTest(UnitTestBase):

  def setUp(self):
    html = self._read_file('kat_page_example1.html')
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
