from . import UnitTestBase
from katnotifier import KatSearch

class KatSearchTest(UnitTestBase):

  def test_simpleKatSearch(self):
    search = KatSearch()  \
      .include("myTitle")
    expected = "http://kat.cr/usearch/myTitle/"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_multiKeywordsSearch(self):
    search = KatSearch() \
      .include("searched movie title")
    expected = "http://kat.cr/usearch/searched%20movie%20title/"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_excludeSomeWords(self):
    search = KatSearch()  \
      .include("italian") \
      .exclude("md")      \
      .exclude("cam")
    expected = "http://kat.cr/usearch/italian%20-md%20-cam/"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_searchInCategory(self):
    search = KatSearch()  \
      .include("italian") \
      .inCategory("movies")
    expected = "http://kat.cr/usearch/italian%20category%3Amovies/"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_withMinSeed(self):
    search = KatSearch()  \
      .include("italian") \
      .withMinSeeds(200)
    expected = "http://kat.cr/usearch/italian%20seeds%3A200/"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_sortResultsBy(self):
    search = KatSearch()  \
      .include("italian") \
      .orderBy("time_add", "desc")
    expected = "http://kat.cr/usearch/italian/?field=time_add&sorder=desc"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_finalAcceptanceTest(self):
    search = KatSearch()    \
      .include("italian")   \
      .exclude("md")        \
      .exclude("cam")       \
      .exclude("telesync")  \
      .exclude("ts")        \
      .exclude("screener")  \
      .inCategory("movies") \
      .withMinSeeds(200)    \
      .orderBy("time_add", "desc")

    expected = "http://kat.cr/usearch/" + \
      "italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" + \
      "?field=time_add&sorder=desc"

    actual = search.toUrl()
    self.assertEquals(expected, actual)
