class IFNotifier:

  def send(self, message):
    raise NotImplementedError("You're calling an abstract class!")

class IFNotifiersList(IFNotifier):

  def __init__(self, notifiers):
    self.notifiers = notifiers

  def send(self, message):
    for n in self.notifiers:
      n.send(message)

class PrintIFNotifier(IFNotifier):

  def send(self, message):
    print "Notify:\t\t[" + message + "]"
