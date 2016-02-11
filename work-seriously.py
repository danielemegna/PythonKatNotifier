from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, SqlLiteMovieRepository,
  HttpIFNotifier, UrlLibHtmlRetriever
)

moviesRepository = SqlLiteMovieRepository()
ifNotifier = HttpIFNotifier()
htmlRetriever = UrlLibHtmlRetriever()
katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever)

katNotifier.work()
