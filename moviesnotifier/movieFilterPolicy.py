class MovieFilterPolicy:

  def isInteresting(self, movie):
    raise NotImplementedError("You're calling an abstract class!")
  def filter(self, movie):
    raise NotImplementedError("You're calling an abstract class!")

class MovieFilterPolicyList(MovieFilterPolicy):

  def __init__(self, policies):
    self.policies = policies
  def isInteresting(self, movie):
    raise NotImplementedError("Not yet implemented!")
    #for p in self.policies:
  def filter(self, movie):
    raise NotImplementedError("Not yet implemented!")