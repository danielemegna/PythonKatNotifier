import os

from moviesnotifier import HttpIFNotifier
from moviesnotifier import (
  MoviesNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintIFNotifier, HttpIFNotifier, IFNotifiersList, KatSearch
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

################################### BEGIN

ifNotifier = IFNotifiersList([
  HttpIFNotifier(),
  PrintIFNotifier()
])

moviesSearch = KatSearch()                \
  .include("italian")                     \
  .exclude("md cam telesync ts screener") \
  .inCategory("movies")                   \
  .withMinSeeds(200)                      \
  .orderBy("time_add", "desc")

dbPath = absolutePathFromRelative('production.db')
moviesRepository = SqlLiteMovieRepository(dbPath)
htmlRetriever = UrlLibHtmlRetriever()

moviesNotifier = MoviesNotifier(moviesRepository, ifNotifier, htmlRetriever, katSearch)
moviesNotifier.work()
