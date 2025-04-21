create database virtualart;
use virtualart;
CREATE TABLE Artwork (
    ArtworkID INT IDENTITY(1,1) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    CreationDate DATE,
    Medium VARCHAR(100),
    ImageURL TEXT
);

-- Artist table
CREATE TABLE Artist (
    ArtistID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website TEXT,
    ContactInformation TEXT
);

-- User table
CREATE TABLE [User] (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    ProfilePicture TEXT,
    FavoriteArtworks VARCHAR(MAX) 
);



CREATE TABLE Gallery (
    GalleryID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Location VARCHAR(255),
    Curator INT REFERENCES Artist(ArtistID),
    OpeningHours TEXT
);


CREATE TABLE User_Favorite_Artwork (
    UserID INT REFERENCES [User](UserID),
    ArtworkID INT REFERENCES Artwork(ArtworkID),
    PRIMARY KEY (UserID, ArtworkID)
);


CREATE TABLE Artwork_Gallery (
    ArtworkID INT REFERENCES Artwork(ArtworkID),
    GalleryID INT REFERENCES Gallery(GalleryID),
    PRIMARY KEY (ArtworkID, GalleryID)
);

