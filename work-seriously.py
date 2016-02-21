import os

from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintIFNotifier, HttpIFNotifier, IFNotifiersList
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

################################### BEGIN

ifNotifier = IFNotifiersList([
  HttpIFNotifier(),
  PrintIFNotifier()
])

katSearch = KatSearch()                   \
  .include("italian")                     \
  .exclude("md cam telesync ts screener") \
  .inCategory("movies")                   \
  .withMinSeeds(200)                      \
  .orderBy("time_add", "desc")

dbPath = absolutePathFromRelative('production.db')
moviesRepository = SqlLiteMovieRepository(dbPath)
htmlRetriever = UrlLibHtmlRetriever()

katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever, katSearch)
katNotifier.work()
