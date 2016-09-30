class Movie:

  def __init__(self, title, seeds=0):
    self.title = title
    self.seeds = seeds

  def __hash__(self):
    return hash(self.title) + hash(self.seeds)

  def __eq__(self, other):
    return self.title == other.title and self.seeds == other.seeds
