class HtmlRetriever:

  def get(self, url):
    raise NotImplementedError("You're calling an abstract class!")

import urllib2, ssl, gzip
from StringIO import StringIO
class UrlLibHtmlRetriever:

  def get(self, url):
    context = ssl._create_unverified_context()
    response = urllib2.urlopen(url, context=context)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        return data
    return response.read()

