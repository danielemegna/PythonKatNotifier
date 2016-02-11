import unittest
import os
import shutil

from katnotifier import SqlLiteMovieRepository
from katnotifier import Movie

class SqlLiteMovieRepositoryTest(unittest.TestCase):
  
  def setUp(self):
    dbPath = self.__absolutePathFromRelative('test.db')
    tempDbPath = self.__absolutePathFromRelative('temp.db')
    shutil.copyfile(dbPath, tempDbPath)
    self.repository = SqlLiteMovieRepository(tempDbPath) 
 
  def tearDown(self):
    tempDbPath = self.__absolutePathFromRelative('temp.db')
    os.remove(tempDbPath) 

  def test_alreadyNotified(self):
    movies = self.repository.alreadyNotified()
    self.assertEquals(2, len(movies))
    self.assertEquals("Titolo film notificato", movies[0].title)
    self.assertEquals("Altro film notificato", movies[1].title)

  def test_add(self):
    movies = self.repository.add(Movie("Nuovo film da inserire"))
    
    movies = self.repository.alreadyNotified()
    self.assertEquals(3, len(movies))
    self.assertEquals(Movie("Nuovo film da inserire"), movies[2])

  def __absolutePathFromRelative(self, relativePath):
    dirPath = os.path.dirname(__file__)
    return os.path.join(dirPath, relativePath)
    
