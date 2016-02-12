import os

from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintIFNotifier, HttpIFNotifier, IFNotifiersList
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

ifNotifier = IFNotifiersList([
  HttpIFNotifier(),
  PrintIFNotifier()
])

dbPath = absolutePathFromRelative('production.db')
moviesRepository = SqlLiteMovieRepository(dbPath)
htmlRetriever = UrlLibHtmlRetriever()

katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever)
katNotifier.work()

