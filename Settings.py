class Settings(object):
    def __init__(self, JsonClient):
        self.url = 'http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false'
        self.JsonClient = JsonClient
        self.settings = self.refresh_settings()
        
    def get_settings(self):
        return self.settings
    
    def set_settings(self, settings):
        self.settings = settings
    
    def refresh_settings(self):
        settings = self.JsonClient.get(self.url)
        self.set_settings(settings)
        return settings

    def get_alarms(self):
        pass