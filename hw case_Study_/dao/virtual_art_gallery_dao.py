# dao/virtual_art_gallery_dao.py

from abc import ABC, abstractmethod
from entity import Artwork

class IVirtualArtGalleryDAO(ABC):
    @abstractmethod
    def add_artwork(self, artwork: Artwork):
        pass
    
    @abstractmethod
    def update_artwork(self, artwork: Artwork):
        pass
    
    @abstractmethod
    def remove_artwork(self, artwork_id: int):
        pass
    
    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int):
        pass
    
    @abstractmethod
    def search_artworks(self, keyword: str):
        pass
    
    @abstractmethod
    def add_artwork_to_favorite(self, user_id: int, artwork_id: int):
        pass
    
    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int):
        pass
    
    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int):
        pass
    
    @abstractmethod
    def get_all_artworks(self):
        pass

    @abstractmethod 
    def add_gallery(self):
        pass

    @abstractmethod
    def search_galleries(self):
        pass

    @abstractmethod
    def update_gallery(self):
        pass

    @abstractmethod
    def remove_gallery(self):
        pass

    @abstractmethod
    def get_gallery_by_id(self):
        pass

    @abstractmethod
    def get_all_galleries(self):
        pass
    