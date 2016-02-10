from . import KatPage

class KatNotifier:
  
  def __init__(self, moviesRepository, ifNotifier, htmlRetriever):
    self.ifNotifier = ifNotifier
    self.moviesRepository = moviesRepository
    self.htmlRetriever = htmlRetriever
    return
  
  def work(self):
    html = self.htmlRetriever.get(
      "http://kat.cr/usearch/" +
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
      "?field=time_add&sorder=desc"
    )

    katPage = KatPage(html)
    actual = katPage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()
    toNotify = set(actual) - set(alreadyNotified)

    for movie in toNotify:
      self.ifNotifier.send(movie.title)
      self.moviesRepository.add(movie)

    return

