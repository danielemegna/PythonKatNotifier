import unittest
from katnotifier import Movie

class MovieTest(unittest.TestCase):

  def test_equality(self):
    m1 = Movie("Primo film")
    m2 = Movie("Secondo film")

    self.assertEquals(m1, m1)
    self.assertNotEquals(m1, m2)
