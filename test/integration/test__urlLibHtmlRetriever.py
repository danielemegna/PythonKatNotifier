import unittest
from moviesnotifier import (UrlLibHtmlRetriever)

class UrlLibHtmlRetrieverTest(unittest.TestCase):

  def setUp(self):
    self.retriever = UrlLibHtmlRetriever()

  def test_retrieveHtml(self):
    url = "http://example.com/"
    html = self.retriever.get(url)
    self.assertIn("<h1>Example Domain</h1>", html)
