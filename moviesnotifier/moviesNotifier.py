from . import KatPage

class MoviesNotifier:
  
  def __init__(self, moviesRepository, webpageFactory, notificationListener):
    self.moviesRepository = moviesRepository
    self.webpageFactory = webpageFactory
    self.notificationListener = notificationListener
    return
  
  def work(self):
    webpage = self.webpageFactory.build()
    actual = webpage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()
    toNotify = set(actual) - set(alreadyNotified)

    for movie in toNotify:
      self.notificationListener.send(movie.title)
      self.moviesRepository.add(movie)

    return
