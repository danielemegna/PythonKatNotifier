import unittest
from bs4 import BeautifulSoup

class KatPage:

  def __init__(self, html):
    self.html = html
    self.soup = BeautifulSoup(html, 'html.parser')
    return

  def movies(self):
    links = self.__extract_movie_links()
    self.__sanitize_movie_links(links)
    return self.__movie_links_to_titles_array(links)

  def __movie_links_to_titles_array(self, links):
    movies = []
    for movie in links:
      movies.append(''.join(movie.contents))
    return movies

  def __sanitize_movie_links(self, links):
    for movie in self.__extract_movie_links():
      movie.strong.unwrap()

  def __extract_movie_links(self):
    return self.soup.find_all("a", class_="cellMainLink")


class KatPageTest(unittest.TestCase):

  def setUp(self):
    html = self.__read_file('test/katPage.html')
    self.page = KatPage(html)

  def test_recognizeCorrectlyNumberOfMovies(self):
    movies = self.page.movies()
    self.assertEqual(len(movies), 12)

  def test_readCorrectlyMovieTitles(self):
    movies = self.page.movies()
    self.assertEqual(movies[0], # todo -> this will be 'movies[0].title'
      "Son Of A Gun (2014) BRrip XviD - Italian English Ac3 5 1 Sub ita eng MIRCrew"
    );
    self.assertEqual(movies[1],
      "Lo Stagista Inaspettato-The Intern 2015 iTALiAN BRRip XviD BLUWORLD"
    );
    self.assertEqual(movies[7],
      "Inside Out 2015 iTALiAN BDRip XviD-TRL[MT] avi"
    );

  def __read_file(self, path):
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html


if __name__ == '__main__':
  unittest.main()
