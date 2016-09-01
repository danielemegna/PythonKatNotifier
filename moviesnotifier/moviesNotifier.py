from . import KatPage

class MoviesNotifier:
  
  def __init__(self, moviesRepository, notificationListener, htmlRetriever, moviesSearch):
    self.notificationListener = notificationListener
    self.moviesRepository = moviesRepository
    self.htmlRetriever = htmlRetriever
    self.moviesSearch = moviesSearch
    return
  
  def work(self):
    searchUrl = self.moviesSearch.toUrl()
    html = self.htmlRetriever.get(searchUrl)

    page = KatPage(html)

    actual = page.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()
    toNotify = set(actual) - set(alreadyNotified)

    for movie in toNotify:
      self.notificationListener.send(movie.title)
      self.moviesRepository.add(movie)

    return

