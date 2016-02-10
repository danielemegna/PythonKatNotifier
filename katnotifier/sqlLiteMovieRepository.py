import sqlite3

from . import MovieRepository
from . import Movie

class SqlLiteMovieRepository(MovieRepository):

  def __init__(self, dbPath):
    self.dbPath = dbPath

  def alreadyNotified(self):
    return self.__getMoviesByQuery("select * from Movies")

  def __getMoviesByQuery(self, query):
    connection = self.__openConnection()
    rows = connection.execute(query)
    movies =  self.__dbRowsToMovies(rows)
    self.__closeConnection(connection)
    return movies

  def __openConnection(self):
    return sqlite3.connect(self.dbPath)

  def __closeConnection(self, connection):
    connection.close()

  def __dbRowsToMovies(self, rows):
    return map(lambda row: Movie(row[0]), rows)
