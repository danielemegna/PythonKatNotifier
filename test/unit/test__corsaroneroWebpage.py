from . import UnitTestBase
from moviesnotifier import CorsaroneroWebpage

class CorsaroneroWebpageTest(UnitTestBase):

  def setUp(self):
    html = self._read_file('corsaronero_example1.html')
    self.page = CorsaroneroWebpage(html)

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 40)

  def test_recognizeMovieTitles(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].title, "Pintus@Forum 2014 iTA AAC HDTV 720p x264 iCV-CreW")
    self.assertEqual(movies[1].title, "Storia di fantasmi cinesi - Trilogy (2003-07).H264.Ital..")
    self.assertEqual(movies[20].title, "I.cinque.segreti.del.deserto.1943.DVDRip.XviD.AC3.Ita.E..")
    self.assertEqual(movies[39].title, "The Hidden - Lalieno 1987 WEB-DL 720p Ita Eng x265-NAHO..")

  def test_recognizeSeeds(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].seeds, 53)
    self.assertEqual(movies[1].seeds, 79)
    self.assertEqual(movies[15].seeds, 0)
    self.assertEqual(movies[20].seeds, 31)
    self.assertEqual(movies[39].seeds, 53)

  def test_correctlyAppliesFilterPolicy(self):
    policy = ExamplePolicy()
    movies = self.page.movies(policy)
    self.assertEqual(len(movies), 20)

from moviesnotifier import NotificationPolicy
class ExamplePolicy(NotificationPolicy):
  def filter(self, movies):
    return [m for m in movies if self.isInteresting(m)]
  def isInteresting(self, movie):
    return movie.seeds >= 42
