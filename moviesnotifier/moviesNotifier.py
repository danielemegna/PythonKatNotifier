class MoviesNotifier:
  
  def __init__(self, moviesRepository, webpageFactory, notificationListener, movieFilterPolicy):
    self.moviesRepository = moviesRepository
    self.webpageFactory = webpageFactory
    self.notificationListener = notificationListener
    self.movieFilterPolicy = movieFilterPolicy
    return
  
  def work(self):
    webpage = self.webpageFactory.build()
    actual = webpage.movies()
    alreadyNotified = self.moviesRepository.alreadyNotified()

    newMovies = set(actual) - set(alreadyNotified)
    interestingMovies = [m for m in newMovies if self.movieFilterPolicy.isInteresting(m)]

    for movie in interestingMovies:
      self.notificationListener.send(movie.title)
      self.moviesRepository.add(movie)

    return
