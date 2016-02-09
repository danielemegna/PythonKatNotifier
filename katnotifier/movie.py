class Movie:

  @classmethod
  def tags_to_array(self, tags):
    return map(self.from_tag, tags)

  @classmethod
  def from_tag(self, tag):
    if(tag.strong):
      tag.strong.unwrap()

    title = ''.join(tag.contents)
    return self(title)

  def __init__(self, title):
    self.title = title

  def __hash__(self):
    return hash(self.title)

  def __eq__(self, other):
    return self.title == other.title
