class MovieRepository:

  def alreadyNotified(self):
    raise NotImplementedError("You're calling an abstract class!")

  def add(self, movie):
    raise NotImplementedError("You're calling an abstract class!")

class PrintMovieRepository(MovieRepository):

  def alreadyNotified(self):
    print "(asked for alreadyNotified)"
    return []

  def add(self, movie):
    print "Add to repo:\t[" + movie.title + "]"
