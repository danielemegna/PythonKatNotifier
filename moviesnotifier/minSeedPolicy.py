from . import MovieFilterPolicy

class MinSeedPolicy(MovieFilterPolicy):

  def __init__(self, minSeedValue):
    self.minSeedValue = minSeedValue
  
  def isInteresting(self, movie):
    return movie.seeds >= self.minSeedValue

  def filter(self, movie):
    raise NotImplementedError("Not yet implemented!")
