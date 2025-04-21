
class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_information):
        self._artist_id = artist_id
        self._name = name
        self._biography = biography
        self._birth_date = birth_date
        self._nationality = nationality
        self._website = website
        self._contact_information = contact_information

    
    @property
    def artist_id(self):
        return self._artist_id

    @property
    def name(self):
        return self._name

    @property
    def biography(self):
        return self._biography

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def nationality(self):
        return self._nationality

    @property
    def website(self):
        return self._website

    @property
    def contact_information(self):
        return self._contact_information

    
    @artist_id.setter
    def artist_id(self, artist_id):
        self._artist_id = artist_id

    @name.setter
    def name(self, name):
        self._name = name

    @biography.setter
    def biography(self, biography):
        self._biography = biography

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    @website.setter
    def website(self, website):
        self._website = website

    @contact_information.setter
    def contact_information(self, contact_information):
        self._contact_information = contact_information
    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, " \
               f"Creation Date: {self.creation_date}, Medium: {self.medium}, Image URL: {self.image_url}"