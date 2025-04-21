
class Gallery:
    def __init__(self, gallery_id, name, description, location, curator, opening_hours):
        self._gallery_id = gallery_id
        self._name = name
        self._description = description
        self._location = location
        self._curator = curator
        self._opening_hours = opening_hours

    
    @property
    def gallery_id(self):
        return self._gallery_id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def location(self):
        return self._location

    @property
    def curator(self):
        return self._curator

    @property
    def opening_hours(self):
        return self._opening_hours

    
    @gallery_id.setter
    def gallery_id(self, gallery_id):
        self._gallery_id = gallery_id

    @name.setter
    def name(self, name):
        self._name = name

    @description.setter
    def description(self, description):
        self._description = description

    @location.setter
    def location(self, location):
        self._location = location

    @curator.setter
    def curator(self, curator):
        self._curator = curator

    @opening_hours.setter
    def opening_hours(self, opening_hours):
        self._opening_hours = opening_hours
    
    def __str__(self):
        return f"  Name: {self.name}, Description: {self.description}, " \
               f"Location: {self.location}, Curator: {self.curator}, Opening Hours: {self.opening_hours}"