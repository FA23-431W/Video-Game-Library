CREATE TABLE Publisher (
    publisherID INT PRIMARY KEY,
    name VARCHAR(255),
    year DATE
);

CREATE TABLE Game (
    gameID INT PRIMARY KEY, 
    Title VARCHAR(255),
    mainCate VARCHAR(255),
    price DECIMAL(10,2),
    `release` DATE, 
    publisherID INT,
    FOREIGN KEY (publisherID) REFERENCES Publisher(publisherID)
);

CREATE TABLE Category (
    mainCate VARCHAR(255),
    subCate VARCHAR(255),
    PRIMARY KEY (mainCate),
    INDEX (subCate)
);

CREATE TABLE User (
    userID INT PRIMARY KEY, 
    name VARCHAR(255),
    password VARCHAR(255),
    wishlistID INT
);

CREATE TABLE WishlistUser (
    wishlistID INT PRIMARY KEY,
    userID INT,
    FOREIGN KEY (userID) REFERENCES User(userID)
);

CREATE TABLE WishlistGame (
    wishlistID INT PRIMARY KEY,
    gameID INT,
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);

CREATE TABLE Achievement (
    achievementID INT PRIMARY KEY,
    gameID INT,
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);

CREATE TABLE Community (
    communityID INT PRIMARY KEY,
    gameID INT,
    dashboardID INT,
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);

CREATE TABLE Dashboard (
    dashboardID INT PRIMARY KEY,
    post TEXT,
    Author VARCHAR(255),
    date DATE
);

CREATE TABLE Link (
    userID INT,
    gameID INT,
    wishlistID INT,
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    FOREIGN KEY (wishlistID) REFERENCES WishlistUser(wishlistID),
    PRIMARY KEY (userID, gameID, wishlistID)
);

CREATE TABLE Belongs (
    achievementID INT,
    gameID INT,
    FOREIGN KEY (achievementID) REFERENCES Achievement(achievementID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    PRIMARY KEY (achievementID, gameID)
);

CREATE TABLE GroupBy (
    gameID INT,
    subCate VARCHAR(255),
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    FOREIGN KEY (subCate) REFERENCES Category(subCate),
    PRIMARY KEY (gameID, subCate)
);

CREATE TABLE has (
    gameID INT,
    CommunityID INT,
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    FOREIGN KEY (CommunityID) REFERENCES Community(CommunityID),
    PRIMARY KEY (gameID, CommunityID)
);

CREATE TABLE includes (
    CommunityID INT,
    dashboardID INT,
    FOREIGN KEY (CommunityID) REFERENCES Community(CommunityID),
    FOREIGN KEY (dashboardID) REFERENCES Dashboard(dashboardID),
    PRIMARY KEY (CommunityID, dashboardID)
);

CREATE TABLE contains (
    gameID INT,
    wishlistID INT,
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    FOREIGN KEY (wishlistID) REFERENCES WishlistGame(wishlistID),
    PRIMARY KEY (gameID, wishlistID)
);
