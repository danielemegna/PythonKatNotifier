from . import UnitTestBase
from moviesnotifier import KatSearch

class KatSearchTest(UnitTestBase):

  def test_simpleKatSearch(self):
    search = KatSearch()  \
      .include("myTitle")
    expected = "http://kat.cr/usearch/myTitle/"

    self.assertEquals(expected, search.toUrl())

  def test_multiKeywordsSearch(self):
    search = KatSearch() \
      .include("searched movie title")
    expected = "http://kat.cr/usearch/searched%20movie%20title/"

    self.assertEquals(expected, search.toUrl())

  def test_excludeSomeWords(self):
    search = KatSearch()  \
      .include("italian") \
      .exclude("md")      \
      .exclude("cam")
    expected = "http://kat.cr/usearch/italian%20-md%20-cam/"

    self.assertEquals(expected, search.toUrl())

  def test_searchInCategory(self):
    search = KatSearch()  \
      .include("italian") \
      .inCategory("movies")
    expected = "http://kat.cr/usearch/italian%20category%3Amovies/"

    self.assertEquals(expected, search.toUrl())

  def test_withMinSeed(self):
    search = KatSearch()  \
      .include("italian") \
      .withMinSeeds(200)
    expected = "http://kat.cr/usearch/italian%20seeds%3A200/"

    self.assertEquals(expected, search.toUrl())

  def test_sortResultsBy(self):
    search = KatSearch()  \
      .include("italian") \
      .orderBy("time_add", "desc")
    expected = "http://kat.cr/usearch/italian/?field=time_add&sorder=desc"

    self.assertEquals(expected, search.toUrl())

  def test_includeAndExcludeAcceptMultipleWords(self):
    search = KatSearch()                      \
      .include("italian movie")               \
      .exclude("md cam telesync ts screener")

    expected = "http://kat.cr/usearch/" + \
      "italian%20movie%20-md%20-cam%20-telesync%20-ts%20-screener/"

    self.assertEquals(expected, search.toUrl())

  def test_finalAcceptanceTest(self):
    search = KatSearch()                      \
      .include("italian")                     \
      .exclude("md cam telesync ts screener") \
      .inCategory("movies")                   \
      .withMinSeeds(200)                      \
      .orderBy("time_add", "desc")

    expected = "http://kat.cr/usearch/" + \
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" + \
      "?field=time_add&sorder=desc"

    self.assertEquals(expected, search.toUrl())
