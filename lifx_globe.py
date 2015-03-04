from datetime import datetime

# from hsbk_color import HSBKColor


class LifxGlobe(object):
    def __init__(self, id, label, site_id, tags, on, color, last_seen, seconds_since_seen=None):
        self.id = id
        self.label = label
        self.site_id = site_id
        self.tags = tags
        self.on = on
        self.color = color
        self.last_seen = last_seen
        # self.seconds_since_seen = seconds_since_seen

    """
        [
            {
                "id":"d073d500ec68",
                "label":"Bedroom",
                "site_id":"4c4946585632",
                "tags":[],
                "on":true,
                "color":{
                    "hue":0.0,
                    "saturation":0.0,
                    "brightness":1.0,
                    "kelvin":9000
                },
                "last_seen":"2015-02-24T08:24:14.947+00:00",
                "seconds_since_seen":6.081347
            }
        ]
    """

    def seconds_since_seen(self):
        now = datetime.now()

        diff = now - self.last_seen
        return diff.seconds