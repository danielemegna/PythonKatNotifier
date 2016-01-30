class KatNotifier:
  
  def __init__(self, moviesRepository, ifNotifier, htmlRetriever):
    self.ifNotifier = ifNotifier
    return
  
  def work(self):
    self.ifNotifier.send("Titolo del nuovo film")
    return

