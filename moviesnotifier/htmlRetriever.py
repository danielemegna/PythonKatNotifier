class HtmlRetriever:

  def get(self, url):
    raise NotImplementedError("You're calling an abstract class!")

import urllib2, ssl, gzip
from StringIO import StringIO
class UrlLibHtmlRetriever:

  def get(self, url):
    context = ssl._create_unverified_context()
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    req = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(req, context=context)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        return data
    return response.read()

