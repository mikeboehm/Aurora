__author__ = 'mike'


class Lifx(object):
    def __init__(self, LifxClient):
        """
        :param LifxClient: LifxClient
        """
        self.client = LifxClient

    def dawn(self):
        pass

    def sunrise(self):
        pass

    def shutoff(self):
        pass
    
    def readinglights_on(self):
        pass

    def readinglights_off(self):
        pass

    def readinglights_toggle(self):
        response = self.client.toggle()
        if response:
            return True

