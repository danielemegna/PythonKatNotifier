class MovieFilterPolicy:

  def filter(self, movies):
    return [m for m in movies if self._isInteresting(m)]
  def _isInteresting(self, movie):
    raise NotImplementedError("You're calling an abstract class!")

class MovieFilterPolicyList(MovieFilterPolicy):

  def __init__(self, policies):
    self.policies = policies
  def filter(self, movies):
    raise NotImplementedError("Not yet implemented!")
  def _isInteresting(self, movie):
    raise NotImplementedError("Not yet implemented!")
    #for p in self.policies:
