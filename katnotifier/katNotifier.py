from . import KatPage
from . import KatSearch

class KatNotifier:
  
  def __init__(self, moviesRepository, ifNotifier, htmlRetriever):
    self.ifNotifier = ifNotifier
    self.moviesRepository = moviesRepository
    self.htmlRetriever = htmlRetriever
    return
  
  def work(self):
    katSearch = KatSearch()                   \
      .include("italian")                     \
      .exclude("md cam telesync ts screener") \
      .inCategory("movies")                   \
      .withMinSeeds(200)                      \
      .orderBy("time_add", "desc")

    searchUrl = katSearch.toUrl()
    html = self.htmlRetriever.get(searchUrl)

    katPage = KatPage(html)

    actual = katPage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()
    toNotify = set(actual) - set(alreadyNotified)

    for movie in toNotify:
      self.ifNotifier.send(movie.title)
      self.moviesRepository.add(movie)

    return

