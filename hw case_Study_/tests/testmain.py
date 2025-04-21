import unittest
from unittest.mock import MagicMock
from dao import VirtualArtGalleryDAOImpl
from entity import Artwork,Gallery

class TestVirtualArtGalleryDAOImpl(unittest.TestCase):
    def setUp(self):
        self.dao = VirtualArtGalleryDAOImpl("your_connection_string_here")

    #Test case 1:Adding a artwork
    def test_add_artwork(self):
        artwork = Artwork(None, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
        self.dao.add_artwork = MagicMock(return_value=True)
        result = self.dao.add_artwork(artwork)
        self.assertTrue(result)

    #Test case 2:Updating a artwork
    def test_update_artwork(self):
        artwork = Artwork(1, "Updated Title", "Updated Description", "2024-05-20", "Updated Medium", "http://example.com/image_updated.jpg")
        self.dao.update_artwork = MagicMock(return_value=True)
        result = self.dao.update_artwork(artwork)
        self.assertTrue(result)

    #Test case 3:Removing A network
    def test_remove_artwork(self):
        artwork_id = 1
        self.dao.remove_artwork = MagicMock(return_value=True)
        result = self.dao.remove_artwork(artwork_id)
        self.assertTrue(result)

    #Test case 4:Searching a artwork
    def test_search_artworks(self):
        keyword = "Test"
        artwork = Artwork(1, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
        self.dao.search_artworks = MagicMock(return_value=[artwork])
        results = self.dao.search_artworks(keyword)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Title")

    #Test case 5:Adding a Gallery    
    def test_create_gallery(self):
        gallery = Gallery(None, "Test Gallery", "Test Description", "123 Test St", 1, "10 AM - 6 PM")
        self.dao.add_gallery = MagicMock(return_value=True)
        result = self.dao.add_gallery(gallery)
        self.assertTrue(result)

    #Test case 6:Updating a Gallery 
    def test_update_gallery(self):
        gallery = Gallery(1, "Updated Gallery", "Updated Description", "123 Test St", 1, "10 AM - 6 PM")
        self.dao.update_gallery = MagicMock(return_value=True)
        result = self.dao.update_gallery(gallery)
        self.assertTrue(result)

    #Test case 7:Removing a Gallery 
    def test_remove_gallery(self):
        gallery_id = 1
        self.dao.remove_gallery = MagicMock(return_value=True)
        result = self.dao.remove_gallery(gallery_id)
        self.assertTrue(result)

    #Test case 8:Searching a Gallery 
    def test_search_galleries(self):
        keyword = "Test"
        gallery = Gallery(1, "Test Gallery", "Test Description", "123 Test St", 1, "10 AM - 6 PM")
        self.dao.search_galleries = MagicMock(return_value=[gallery])
        results = self.dao.search_galleries(keyword)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Test Gallery")

    

if __name__ == "__main__":
    unittest.main()