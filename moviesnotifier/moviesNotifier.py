class MoviesNotifier:
  
  def __init__(self, moviesRepository, webpageFactory, notificationListener, notificationPolicy):
    self.moviesRepository = moviesRepository
    self.webpageFactory = webpageFactory
    self.notificationListener = notificationListener
    self.notificationPolicy = notificationPolicy
    return
  
  def work(self):
    webpage = self.webpageFactory.build()
    actual = webpage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()

    newMovies = set(actual) - set(alreadyNotified)
    interestingMovies = [m for m in newMovies if self.notificationPolicy.isInteresting(m)]

    for movie in interestingMovies:
      self.notificationListener.send(movie.title)
      self.moviesRepository.add(movie)

    return
