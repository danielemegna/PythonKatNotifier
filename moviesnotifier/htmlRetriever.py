class HtmlRetriever:

  def get(self, url):
    raise NotImplementedError("You're calling an abstract class!")

import urllib2
import gzip
from StringIO import StringIO
class UrlLibHtmlRetriever:

  def get(self, url):
    response = urllib2.urlopen(url)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        return data
    return response.read()

