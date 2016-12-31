from . import UnitTestBase
from mock import MagicMock

from moviesnotifier import (
  MoviesNotifier, NotificationListener,
  NotificationPolicy, MovieRepository,
  HtmlRetriever, Movie
)

class MoviesNotifierTest(UnitTestBase):

  searchUrl = "http://search.url/usearch"

  def setUp(self):
    self.moviesRepository = MovieRepository()
    self.notificationListener = NotificationListener()
    self.notificationPolicy = NotificationPolicy()
    self.webpageFactory = MagicMock()
    self.webpage = MagicMock()
    self.moviesNotifier = MoviesNotifier(
      self.moviesRepository,
      self.webpageFactory,
      self.notificationListener,
      self.notificationPolicy
    )

  def test_notifyNewFilmWithEmptyRepository(self):
    alreadyNotifiedMovies = []
    moviesFromWebpage = [Movie("Titolo del nuovo iTALiAN film", 44)]
    self.__setupMocks(moviesFromWebpage, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.notificationPolicy.isInteresting.assert_called_once_with(moviesFromWebpage[0])
    self.notificationListener.send.assert_called_once_with("Titolo del nuovo iTALiAN film")
    self.moviesRepository.add.assert_called_once_with(Movie("Titolo del nuovo iTALiAN film"))

  def test_notifyNewFilmWithFullRepository(self):
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina")
    ]
    moviesFromWebpage = [
      Movie("Film gia notificato", 66),
      Movie("Nuovo iTALiAN film non notificato", 40)
    ]
    self.__setupMocks(moviesFromWebpage, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.notificationListener.send.assert_called_once_with("Nuovo iTALiAN film non notificato")
    self.moviesRepository.add.assert_called_once_with(Movie("Nuovo iTALiAN film non notificato", 40))

  def test_noNotificationWithNoNewFilms(self):
    alreadyNotifiedMovies = [
      Movie("Film gia notificato"),
      Movie("Film notificato non piu presente nella pagina"),
      Movie("Nuovo iTALiAN film non notificato")
    ]
    moviesFromWebpage = [
      Movie("Film gia notificato", 430),
      Movie("Nuovo iTALiAN film non notificato", 134)
    ]

    self.__setupMocks(moviesFromWebpage, alreadyNotifiedMovies)

    self.moviesNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.notificationListener.send.assert_not_called()
    self.moviesRepository.add.assert_not_called()

  
  def __setupMocks(self, moviesFromWebpage, alreadyNotifiedMovies):
    self.moviesRepository.alreadyNotified = MagicMock(return_value=alreadyNotifiedMovies)
    self.notificationPolicy.isInteresting = MagicMock(return_value=True)
    self.notificationListener.send = MagicMock()
    self.moviesRepository.add = MagicMock()
    self.webpage.movies = MagicMock(return_value=moviesFromWebpage)
    self.webpageFactory.build = MagicMock(return_value=self.webpage)
