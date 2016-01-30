import json
import urllib2

class IFNotifier:

  IF_MAKER_URL = "https://maker.ifttt.com/trigger/new_film_available/with/key/g_t7YYx1cqoDKvOBiPssx8l5YBTI8OnWjhUiRKD5Zim"

  def send(self, title):
    data = json.dumps({ "value1" : title })
    request = urllib2.Request(IF_MAKER_URL, data, {'Content-Type': 'application/json', 'Content-Length': len(data)})
    f = urllib2.urlopen(request)
    response = f.read()
    f.close()
