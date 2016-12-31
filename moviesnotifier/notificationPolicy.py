class NotificationPolicy:

  def isInteresting(self, movie):
    raise NotImplementedError("You're calling an abstract class!")

class NotificationPolicyList(NotificationPolicy):

  def __init__(self, policies):
    self.policies = policies

  def isInteresting(self, movie):
    pass
    #for p in self.policies:

