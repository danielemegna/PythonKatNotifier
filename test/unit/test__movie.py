from . import UnitTestBase
from moviesnotifier import Movie

class MovieTest(UnitTestBase):

  def test_equalityViaAssert(self):
    m1 = Movie("Primo film")
    m2 = Movie("Secondo film")

    self.assertEquals(m1, m1)
    self.assertNotEquals(m1, m2)

  def test_equalityViaEqualSign(self):
    m1 = Movie("Primo film")
    m2 = Movie("Secondo film")

    self.assertTrue(m1 == m1)
    self.assertFalse(m1 == m2)
