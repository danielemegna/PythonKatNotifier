from . import UnitTestBase
from mock import MagicMock

from moviesnotifier import (
  MoviesNotifier, NotificationListener,
  MovieRepository, HtmlRetriever, Movie
)

class MoviesNotifierTest(UnitTestBase):

  searchUrl = "http://search.url/usearch"

  def setUp(self):
    self.moviesRepository = MovieRepository()
    self.notifier = NotificationListener()
    self.htmlRetriever = HtmlRetriever()
    self.moviesSearch = MagicMock()
    self.moviesNotifier = MoviesNotifier(self.moviesRepository, self.notifier, self.htmlRetriever, self.moviesSearch)

  def test_notifyNewFilmWithEmptyRepository(self):
    htmlMockFile = 'kat_page_example2.html'
    alreadyNotifiedMovies = []
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesSearch.toUrl.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.notifier.send.assert_called_once_with("Titolo del nuovo iTALiAN film")
    self.moviesRepository.add.assert_called_once_with(Movie("Titolo del nuovo iTALiAN film"))

  def test_notifyNewFilmWithFullRepository(self):
    htmlMockFile = 'kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesSearch.toUrl.assert_called_once_with()
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.notifier.send.assert_called_once_with("Nuovo iTALiAN film non notificato")
    self.moviesRepository.add.assert_called_once_with(Movie("Nuovo iTALiAN film non notificato"))

  def test_noNotificationWithNoNewFilms(self):
    htmlMockFile = 'kat_page_example3.html'
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina"),
      Movie("Nuovo iTALiAN film non notificato")
    ]
    self.__setupMocks(htmlMockFile, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesSearch.toUrl.assert_called_once_with()
    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(self.searchUrl)
    self.notifier.send.assert_not_called()
    self.moviesRepository.add.assert_not_called()

  
  def __setupMocks(self, htmlMockFile, alreadyNotifiedMovies):
    self.fakeRetrievedHtml = self._read_file(htmlMockFile)
    self.htmlRetriever.get = MagicMock(return_value=self.fakeRetrievedHtml)
    self.moviesRepository.alreadyNotified = MagicMock(return_value=alreadyNotifiedMovies)
    self.notifier.send = MagicMock()
    self.moviesRepository.add = MagicMock()
    self.moviesSearch.toUrl.return_value = self.searchUrl
