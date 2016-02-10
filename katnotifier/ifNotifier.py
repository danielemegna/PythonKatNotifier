import json
import urllib2

class IFNotifier:

  def send(self, title):
    raise NotImplementedError("You're calling an abstract class!")


class HttpIFNotifier(IFNotifier):
    
  IF_MAKER_EVENT = "new_film_available"
  IF_MAKER_KEY = "g_t7YYx1cqoDKvOBiPssx8l5YBTI8OnWjhUiRKD5Zim"
  IF_MAKER_URL = "https://maker.ifttt.com/trigger/" + IF_MAKER_EVENT + "/with/key/" + IF_MAKER_KEY

  def send(self, title):
    data = json.dumps({ "value1" : title })
    request = urllib2.Request(IF_MAKER_URL, data, {'Content-Type': 'application/json', 'Content-Length': len(data)})
    f = urllib2.urlopen(request)
    response = f.read()
    f.close()
