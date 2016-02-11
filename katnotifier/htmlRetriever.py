class HtmlRetriever:

  def get(self, url):
    raise NotImplementedError("You're calling an abstract class!")

import urllib2
class UrlLibHtmlRetriever:

  def get(self, url):
    response = urllib2.urlopen(url)
    return response.read()

