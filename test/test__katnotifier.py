import unittest
from mock import MagicMock

from katnotifier import KatNotifier
from katnotifier import IFNotifier

class KatNotifierTest(unittest.TestCase):

  def setUp(self):
    self.moviesRepository = "" #MovieRepository()
    self.ifNotifier = IFNotifier()
    self.htmlRetriever = "" #HtmlRetriever()
    self.katNotifier = KatNotifier(self.moviesRepository, self.ifNotifier, self.htmlRetriever)

  def test_notifyNewFilmWithEmptyRepository(self):
    self.ifNotifier.send = MagicMock();

    self.katNotifier.work()

    self.ifNotifier.send.assert_called_once_with("Titolo del nuovo film")

