
class User:
    def __init__(self, user_id, username, password, email, first_name, last_name, date_of_birth, profile_picture, favorite_artworks):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._profile_picture = profile_picture
        self._favorite_artworks = favorite_artworks

   
    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def profile_picture(self):
        return self._profile_picture

    @property
    def favorite_artworks(self):
        return self._favorite_artworks

    
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    @email.setter
    def email(self, email):
        self._email = email

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @profile_picture.setter
    def profile_picture(self, profile_picture):
        self._profile_picture = profile_picture

    @favorite_artworks.setter
    def favorite_artworks(self, favorite_artworks):
        self._favorite_artworks = favorite_artworks