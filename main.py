from katnotifier import HttpIFNotifier
from katnotifier import (
  KatNotifier, SqlLiteMovieRepository,
  PrintIFNotifier, UrlLibHtmlRetriever
)

moviesRepository = SqlLiteMovieRepository('test/integration/test.db')
ifNotifier = PrintIFNotifier()
htmlRetriever = UrlLibHtmlRetriever()
katNotifier = KatNotifier(moviesRepository, ifNotifier, htmlRetriever)

#katNotifier.work()

