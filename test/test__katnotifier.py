import unittest
from mock import MagicMock

from katnotifier import KatNotifier
from katnotifier import IFNotifier
from katnotifier import MovieRepository
from katnotifier import HtmlRetriever
from katnotifier import Movie

class KatNotifierTest(unittest.TestCase):

  def setUp(self):
    self.moviesRepository = MovieRepository()
    self.ifNotifier = IFNotifier()
    self.htmlRetriever = HtmlRetriever()
    self.katNotifier = KatNotifier(self.moviesRepository, self.ifNotifier, self.htmlRetriever)

  def test_notifyNewFilmWithEmptyRepository(self):
    htmlMockFile = 'test/kat_page_example2.html'
    alreadyNotifiedMovies = []
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(
      "http://kat.cr/usearch/" +
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
      "?field=time_add&sorder=desc"
    )
    self.ifNotifier.send.assert_called_once_with("Titolo del nuovo iTALiAN film")

  def test_notifyNewFilmWithFullRepository(self):
    htmlMockFile = 'test/kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(
      "http://kat.cr/usearch/" +
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
      "?field=time_add&sorder=desc"
    )
    self.ifNotifier.send.assert_called_once_with("Nuovo iTALiAN film non notificato")

  def test_noNotificationWithNoNewFilms(self):
    htmlMockFile = 'test/kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina"),
      Movie("Nuovo iTALiAN film non notificato")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(
      "http://kat.cr/usearch/" +
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
      "?field=time_add&sorder=desc"
    )
    self.ifNotifier.send.assert_not_called()

  
  def __setupMocks(self, htmlMockFile, alreadyNotifiedMovies):
    self.htmlRetriever.get = MagicMock(return_value=self.__read_file(htmlMockFile))
    self.moviesRepository.alreadyNotified = MagicMock(return_value=alreadyNotifiedMovies)
    self.ifNotifier.send = MagicMock()

  def __read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html
