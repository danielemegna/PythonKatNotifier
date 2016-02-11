from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, SqlLiteMovieRepository, PrintIFNotifier,
  HttpIFNotifier, UrlLibHtmlRetriever
)

moviesRepository = SqlLiteMovieRepository('production.db')
ifNotifier = HttpIFNotifier()
htmlRetriever = UrlLibHtmlRetriever()
katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever)

katNotifier.work()
