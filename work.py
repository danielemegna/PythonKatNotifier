import os

from moviesnotifier import (
  MoviesNotifier, SqlLiteMovieRepository, UrlLibHtmlRetriever,
  PrintNotificationListener, IFNotifier, NotificationListenerList,
  CorsaroneroWebpageFactory, TntvillageWebpageFactory,
  MinSeedPolicy, KeywordPolicy
)

def absolutePathFromRelative(relative):
  currentDirectory = os.path.dirname(__file__)
  return os.path.join(currentDirectory, relative)

################################### BEGIN

db = SqlLiteMovieRepository(absolutePathFromRelative('production.db'))
htmlRetriever = UrlLibHtmlRetriever()

notificationListeners = NotificationListenerList([
  IFNotifier(),
  PrintNotificationListener()
])

MoviesNotifier(
  db, CorsaroneroWebpageFactory(htmlRetriever),
  notificationListeners, MinSeedPolicy(500)
).work()

#MoviesNotifier(
#  db, TntvillageWebpageFactory(htmlRetriever),
#  notificationListeners, KeywordPolicy("masterchef")
#).work()
