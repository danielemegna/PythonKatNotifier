import sqlite3

from . import MovieRepository
from . import Movie

class SqlLiteMovieRepository(MovieRepository):

  def __init__(self, dbPath):
    self.connection = sqlite3.connect(dbPath)

  def alreadyNotified(self):
    rows = self.connection.execute("select title from Movies")
    return self.__dbRowsToMovies(rows)

  def __dbRowsToMovies(self, rows):
    return map(lambda row: Movie(row[0]), rows)
