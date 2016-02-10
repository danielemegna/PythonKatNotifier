import unittest
import os

class UnitTestBase(unittest.TestCase):

  def _read_file(self, filename):
    currentDirectory = os.path.dirname(__file__)
    path = os.path.join(currentDirectory, filename)
    file = open(path, 'r')
    html = file.read()
    file.close()
    return html

from test__katNotifier import KatNotifierTest
from test__katPage import KatPageTest
from test__movie import MovieTest
