class Movie:

  @classmethod
  def tags_to_array(self, tags):
    movies = []
    for tag in tags:
      movie = self.from_tag(tag)
      movies.append(movie)
    return movies

  @classmethod
  def from_tag(self, tag):
    tag.strong.unwrap()
    title = ''.join(tag.contents)
    return self(title)

  def __init__(self, title):
    self.title = title
