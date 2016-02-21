from . import UnitTestBase
from mock import MagicMock

from katnotifier import (
  KatNotifier, IFNotifier,
  MovieRepository, HtmlRetriever, Movie
)

class KatNotifierTest(UnitTestBase):

  searchUrl = "http://kat.cr/usearch"

  def setUp(self):
    self.moviesRepository = MovieRepository()
    self.ifNotifier = IFNotifier()
    self.htmlRetriever = HtmlRetriever()
    self.katSearch = MagicMock();
    self.katNotifier = KatNotifier(self.moviesRepository, self.ifNotifier, self.htmlRetriever, self.katSearch)

  def test_notifyNewFilmWithEmptyRepository(self):
    htmlMockFile = 'kat_page_example2.html'
    alreadyNotifiedMovies = []
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.katSearch.toUrl.assert_called_once_with()
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.ifNotifier.send.assert_called_once_with("Titolo del nuovo iTALiAN film")
    self.moviesRepository.add.assert_called_once_with(Movie("Titolo del nuovo iTALiAN film"))

  def test_notifyNewFilmWithFullRepository(self):
    htmlMockFile = 'kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.katSearch.toUrl.assert_called_once_with()
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.ifNotifier.send.assert_called_once_with("Nuovo iTALiAN film non notificato")
    self.moviesRepository.add.assert_called_once_with(Movie("Nuovo iTALiAN film non notificato"))

  def test_noNotificationWithNoNewFilms(self):
    htmlMockFile = 'kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina"),
      Movie("Nuovo iTALiAN film non notificato")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.katNotifier.work()

    self.katSearch.toUrl.assert_called_once_with()
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.ifNotifier.send.assert_not_called()
    self.moviesRepository.add.assert_not_called()

  
  def __setupMocks(self, htmlMockFile, alreadyNotifiedMovies):
    self.htmlRetriever.get = MagicMock(return_value=self._read_file(htmlMockFile))
    self.moviesRepository.alreadyNotified = MagicMock(return_value=alreadyNotifiedMovies)
    self.ifNotifier.send = MagicMock()
    self.moviesRepository.add = MagicMock()
    self.katSearch.toUrl.return_value = self.searchUrl
