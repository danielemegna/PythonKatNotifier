import unittest
import os

from katnotifier import SqlLiteMovieRepository

class SqlLiteMovieRepositoryTest(unittest.TestCase):

  def setUp(self):
    currentDirectory = os.path.dirname(__file__)
    dbPath = os.path.join(currentDirectory, 'test.db')
    self.repository = SqlLiteMovieRepository(dbPath) 

  def test_alreadyNotified(self):
    movies = self.repository.alreadyNotified()
    self.assertEquals(2, len(movies))
    self.assertEquals("Titolo film notificato", movies[0].title)
    self.assertEquals("Altro film notificato", movies[1].title)
