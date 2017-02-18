from . import MovieFilterPolicy

class MinSeedPolicy(MovieFilterPolicy):

  def __init__(self, minSeedValue):
    self.minSeedValue = minSeedValue
  
  def _isInteresting(self, movie):
    return movie.seeds >= self.minSeedValue
