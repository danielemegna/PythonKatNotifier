import os

from moviesnotifier import (
  MoviesNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintNotificationListener, IFNotifier, NotificationListenerList, KatSearch
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

################################### BEGIN

notificationListeners = NotificationListenerList([
  IFNotifier(),
  PrintNotificationListener()
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

moviesNotifier = MoviesNotifier(moviesRepository, notificationListeners, htmlRetriever, moviesSearch)
moviesNotifier.work()
