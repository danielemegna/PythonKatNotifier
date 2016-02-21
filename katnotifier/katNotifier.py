from . import KatPage
from . import KatSearch

class KatNotifier:
  
  def __init__(self, moviesRepository, ifNotifier, htmlRetriever, katSearch):
    self.ifNotifier = ifNotifier
    self.moviesRepository = moviesRepository
    self.htmlRetriever = htmlRetriever
    self.katSearch = katSearch
    return
  
  def work(self):
    searchUrl = self.katSearch.toUrl()
    html = self.htmlRetriever.get(searchUrl)

    katPage = KatPage(html)

    actual = katPage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()
    toNotify = set(actual) - set(alreadyNotified)

    for movie in toNotify:
      self.ifNotifier.send(movie.title)
      self.moviesRepository.add(movie)

    return

