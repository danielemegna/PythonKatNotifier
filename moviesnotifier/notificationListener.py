class NotificationListener:

  def send(self, message):
    raise NotImplementedError("You're calling an abstract class!")

class NotificationListenerList(NotificationListener):

  def __init__(self, notifiers):
    self.notifiers = notifiers

  def send(self, message):
    for n in self.notifiers:
      n.send(message)

class PrintNotificationListener(NotificationListener):

  def send(self, message):
    print "Notify:\t\t[" + message + "]"
