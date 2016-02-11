from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, PrintMovieRepository,
  PrintIFNotifier, UrlLibHtmlRetriever
)

moviesRepository = PrintMovieRepository()
ifNotifier = PrintIFNotifier()
htmlRetriever = UrlLibHtmlRetriever()
katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever)

katNotifier.work()
