from . import UnitTestBase
from moviesnotifier import Movie

class MovieTest(UnitTestBase):

  def test_equalityViaAssert(self):
    m1 = Movie("Primo film", 42)
    m2 = Movie("Secondo film", 50)
    m3 = Movie("Primo film", 42)
    m4 = Movie("Secondo film", 100)

    self.assertEquals(m1, m1)
    self.assertEquals(m1, m3)
    self.assertEquals(m2, m4)
    self.assertNotEquals(m1, m2)
    self.assertNotEquals(m2, m3)

  def test_equalityViaEqualSign(self):
    m1 = Movie("Primo film", 42)
    m2 = Movie("Secondo film", 50)
    m3 = Movie("Primo film", 42)
    m4 = Movie("Secondo film", 100)

    self.assertTrue(m1 == m1)
    self.assertTrue(m1 == m3)
    self.assertTrue(m2 == m4)
    self.assertFalse(m1 == m2)
    self.assertFalse(m2 == m3)
