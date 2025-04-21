import pyodbc
from dao import IVirtualArtGalleryDAO
from entity import Artwork,Gallery
from exceptions import UserNotFoundException
from exceptions import ArtworkNotfoundException
import datetime

class VirtualArtGalleryDAOImpl(IVirtualArtGalleryDAO):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_connection(self):
        return pyodbc.connect(self.connection_string)

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url)
            print("Artwork Table")
            print("______________")
            conn.commit()
            print("\n---Artwork Table ---")
            select_query = "SELECT * FROM Artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error occurred while adding artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def get_all_artworks(self) -> list:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Artwork"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Artwork(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error retrieving all artworks:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def update_artwork(self, artwork: Artwork):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE Artwork 
                SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ? 
                WHERE ArtworkID = ?
            """
            cursor.execute(query, artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id)
            conn.commit()
            print("\n--- Updated Artwork Table ---")
            select_query = "SELECT * FROM Artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error updating artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def remove_artwork(self, artwork_id: int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, artwork_id)
            conn.commit()
            print("\n---Artwork Table ---")
            select_query = "SELECT * FROM Artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error removing artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def search_artworks(self, keyword: str):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?"
            cursor.execute(query, f'%{keyword}%', f'%{keyword}%')
            rows = cursor.fetchall()
            return [Artwork(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error searching artworks:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (?, ?)"
            cursor.execute(query, user_id, artwork_id)
            conn.commit()
            print("\n---User Favourite Table ---")
            select_query = "SELECT * FROM User_Favorite_Artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error adding to favorites:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?"
            cursor.execute(query, user_id, artwork_id)
            conn.commit()
            print("\n---User Favourite Table ---")
            select_query = "SELECT * FROM User_Favorite_Artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error removing from favorites:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    def get_artwork_by_id(self, artwork_id: int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Artwork WHERE ArtworkID = ?"
            cursor.execute(query, artwork_id)
            row = cursor.fetchone()
            if not row:
                print("Artwork Not Found")
            return Artwork(*row)
        except pyodbc.Error as e:
            print("Error getting artwork by ID:", e)
            return None
        finally:
            cursor.close()
            conn.close()

    def get_user_favorite_artworks(self, user_id: int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT Artwork.ArtworkID, Artwork.Title, Artwork.Description, Artwork.CreationDate, Artwork.Medium, Artwork.ImageURL
                FROM Artwork
                JOIN User_Favorite_Artwork ON Artwork.ArtworkID = User_Favorite_Artwork.ArtworkID
                WHERE User_Favorite_Artwork.UserID = ?
            """
            cursor.execute(query, user_id)
            rows = cursor.fetchall()
            if not rows:
                raise UserNotFoundException(f"User with ID {user_id} not found.")
            return [Artwork(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error retrieving user's favorite artworks:", e)
            return []
        finally:
            cursor.close()
            conn.close()
    
    def add_gallery(self, gallery: Gallery):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO Gallery (Name,Description,Location,Curator,OpeningHours) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, gallery.name,gallery.description,gallery.location,gallery.curator,gallery.opening_hours)
            conn.commit()
            print("\n---Gallery Table ---")
            select_query = "SELECT * FROM Gallery"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error occurred while adding artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()
    
    def search_galleries(self,keyword:str):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Gallery WHERE Name LIKE ? OR Description LIKE ?"
            cursor.execute(query, f'%{keyword}%', f'%{keyword}%')
            rows = cursor.fetchall()
            return [Gallery(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error searching artworks:", e)
            return []
        finally:
            cursor.close()
            conn.close()
    
    def update_gallery(self,gallery:Gallery):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE Gallery 
                SET Name = ?, Description = ?, Location = ?, Curator = ?, OpeningHours = ? 
                WHERE GalleryID = ?
            """
            cursor.execute(query,gallery.name,gallery.description,gallery.location,gallery.curator,gallery.opening_hours,gallery.gallery_id)
            conn.commit()
            print("\n---Gallery Table ---")
            select_query = "SELECT * FROM Gallery"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error updating artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()
        
    def remove_gallery(self,gallery_id:int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM Gallery WHERE GalleryID = ?"
            cursor.execute(query, gallery_id)
            conn.commit()
            print("\n---Gallery Table ---")
            select_query = "SELECT * FROM Gallery"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return True
        except pyodbc.Error as e:
            print("Error removing artwork:", e)
            return False
        finally:
            cursor.close()
            conn.close()
    
    def get_gallery_by_id(self,galleryid:int):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Gallery WHERE GalleryID = ?"
            cursor.execute(query, galleryid)
            row = cursor.fetchone()
            if not row:
                print("Gallery Not Found")
            return Gallery(*row)
        except pyodbc.Error as e:
            print("Error getting Gallery by ID:", e)
            return None
        finally:
            cursor.close()
            conn.close()
    
    def get_all_galleries(self):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Gallery"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Gallery(*row) for row in rows]
        except pyodbc.Error as e:
            print("Error retrieving all artworks:", e)
            return []
        finally:
            cursor.close()
            conn.close()



        



