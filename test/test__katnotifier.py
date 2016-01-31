import unittest
from mock import MagicMock

from katnotifier import KatNotifier
from katnotifier import IFNotifier
from katnotifier import MovieRepository
from katnotifier import HtmlRetriever

class KatNotifierTest(unittest.TestCase):

  def setUp(self):
    self.moviesRepository = MovieRepository()
    self.ifNotifier = IFNotifier()
    self.htmlRetriever = HtmlRetriever()
    self.katNotifier = KatNotifier(self.moviesRepository, self.ifNotifier, self.htmlRetriever)

  def test_notifyNewFilmWithEmptyRepository(self):
    self.ifNotifier.send = MagicMock();
    self.moviesRepository.alreadyNotified = MagicMock(return_value=[]);
    self.htmlRetriever.get = MagicMock(return_value=self.__read_file('test/kat_page_example2.html'));

    self.katNotifier.work()

    self.moviesRepository.alreadyNotified.assert_called_once_with()
    self.htmlRetriever.get.assert_called_once_with(
      "http://kat.cr/usearch/" +
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
      "?field=time_add&sorder=desc"
    )
    self.ifNotifier.send.assert_called_once_with("Titolo del nuovo iTALiAN film")

  def __read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html
