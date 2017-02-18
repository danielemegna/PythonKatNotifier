from . import MovieFilterPolicy

class KeywordPolicy(MovieFilterPolicy):

  def __init__(self, word):
    self.word = word
  
  def _isInteresting(self, movie):
    return self.word.lower() in movie.title.lower() 
