import os

from moviesnotifier import (
  MoviesNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintNotificationListener, IFNotifier, NotificationListenerList,
  CorsaroneroWebpageFactory
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

################################### BEGIN

notificationListeners = NotificationListenerList([
  IFNotifier(),
  PrintNotificationListener()
])

moviesNotifier = MoviesNotifier(
  SqlLiteMovieRepository(absolutePathFromRelative('production.db')),
  CorsaroneroWebpageFactory(UrlLibHtmlRetriever()),
  notificationListeners
)
moviesNotifier.work()
