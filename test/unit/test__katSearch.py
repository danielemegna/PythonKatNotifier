from . import UnitTestBase
from katnotifier import KatSearch

#"http://kat.cr/usearch/" +
#"italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
#"?field=time_add&sorder=desc"

class KatSearchTest(UnitTestBase):

  def test_simpleKatSearch(self):
    search = KatSearch()  \
      .include("myTitle")
    expected = "http://kat.cr/usearch/myTitle"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_multiKeywordsSearch(self):
    search = KatSearch() \
      .include("searched movie title")
    expected = "http://kat.cr/usearch/searched%20movie%20title"

    actual = search.toUrl()
    self.assertEquals(expected, actual)

  def test_excludeSomeWords(self):
    search = KatSearch()  \
      .include("italian") \
      .exclude("md")      \
      .exclude("cam")
    expected = "http://kat.cr/usearch/italian%20-md%20-cam"

    actual = search.toUrl()
    self.assertEquals(expected, actual)
