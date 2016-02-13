from . import UnitTestBase
from katnotifier import KatSearch

#"http://kat.cr/usearch/" +
#"italian%20-md%20-cam%20-telesync%20-ts%20-screener%20category%3Amovies%20seeds%3A200/" +
#"?field=time_add&sorder=desc"

class KatSearchTest(UnitTestBase):

  def test_simpleKatSearch(self):
    search = KatSearch("myTitle")
    actual = search.toUrl()
    expected = "http://kat.cr/usearch/myTitle"
    self.assertEquals(expected, actual)

  def test_multiKeywordsSearch(self):
    search = KatSearch("searched movie title")
    actual = search.toUrl()
    expected = "http://kat.cr/usearch/searched%20movie%20title"
    self.assertEquals(expected, actual)
