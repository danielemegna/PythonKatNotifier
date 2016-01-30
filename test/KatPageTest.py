import unittest
from bs4 import BeautifulSoup

class KatPage:

  def __init__(self, html):
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    tags = self.__extract_movie_tags()
    return Movie.tags_to_array(tags)

  def __extract_movie_tags(self):
    return self.soup.find_all("a", class_="cellMainLink")


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


#################################################


class KatPageTest(unittest.TestCase):

  def setUp(self):
    html = self.__read_file('test/katPage.html')
    self.page = KatPage(html)

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 12)

  def test_readCorrectlyMovieTitles(self):
    movies = self.page.movies()
    self.assertEqual(movies[0].title, # todo -> this will be 'movies[0].title'
      "Son Of A Gun (2014) BRrip XviD - Italian English Ac3 5 1 Sub ita eng MIRCrew"
    );
    self.assertEqual(movies[1].title,
      "Lo Stagista Inaspettato-The Intern 2015 iTALiAN BRRip XviD BLUWORLD"
    );
    self.assertEqual(movies[7].title,
      "Inside Out 2015 iTALiAN BDRip XviD-TRL[MT] avi"
    );

  def __read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html


if __name__ == '__main__':
  unittest.main()
