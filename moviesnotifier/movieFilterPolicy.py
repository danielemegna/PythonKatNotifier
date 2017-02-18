class MovieFilterPolicy:

  def filter(self, movies):
    return [m for m in movies if self._isInteresting(m)]
  def _isInteresting(self, movie):
    raise NotImplementedError("You're calling an abstract class!")
