import json
import urllib2

from . import NotificationListener

class IFNotifier(NotificationListener):
    
  IF_MAKER_EVENT = "new_film_available"
  IF_MAKER_KEY = "g_t7YYx1cqoDKvOBiPssx8l5YBTI8OnWjhUiRKD5Zim"
  IF_MAKER_URL = "https://maker.ifttt.com/trigger/" + IF_MAKER_EVENT + "/with/key/" + IF_MAKER_KEY

  def send(self, message):
    data = json.dumps({ "value1" : message })
    request = urllib2.Request(
      self.IF_MAKER_URL,
      data,
      {'Content-Type': 'application/json', 'Content-Length': len(data)}
    )
    f = urllib2.urlopen(request)
    response = f.read()
    f.close()
