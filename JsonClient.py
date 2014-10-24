import urllib, json
class JsonClient(object):
    def get(self, url):
        response = urllib.urlopen(url);
        data = json.loads(response.read())
        
        return data