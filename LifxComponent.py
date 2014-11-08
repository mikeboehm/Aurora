from AbstractLight import AbstractLight


class LifxComponent(AbstractLight):
    settings = ''
    light_group = ''

    def __init__(self):
        pass

    def toggle_reading_lights(self):
        if self.reading_light_on:
            self.reading_light_on = False
        else:
            self.reading_light_on = True

    def fade(self, end_colour, duration):
        pass
