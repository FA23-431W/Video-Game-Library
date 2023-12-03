<<<<<<< HEAD
CREATE TABLE Publisher (
    publisherID INT PRIMARY KEY,
    name VARCHAR(255),
    year VARCHAR(10)
);
CREATE TABLE Game (
    gameID INT PRIMARY KEY,
    publisherID INT,
    Title VARCHAR(255),
    mainCate VARCHAR(255),
    price DECIMAL(10, 2),
    `release` VARCHAR(10),
    FOREIGN KEY (publisherID) REFERENCES Publisher(publisherID)
);
CREATE TABLE Category (
    subCate VARCHAR(255),
    mainCate VARCHAR(255),
    INDEX (mainCate),
    PRIMARY KEY (subCate)
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
    wishlistID INT,
    gameID INT,
    FOREIGN KEY (wishlistID) REFERENCES WishlistUser(wishlistID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID),
    PRIMARY KEY (wishlistID, gameID)
);
CREATE TABLE Achievement (
    achievementID INT PRIMARY KEY,
    description TEXT,
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
    date VARCHAR(10),
    Author VARCHAR(255)
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
    FOREIGN KEY (subCate) REFERENCES Category(mainCate),
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
=======
-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: Game_Lib
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Achievement`
--

DROP TABLE IF EXISTS `Achievement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Achievement` (
  `achievementID` int NOT NULL,
  `description` text,
  `gameID` int DEFAULT NULL,
  PRIMARY KEY (`achievementID`),
  KEY `gameID` (`gameID`),
  CONSTRAINT `achievement_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Belongs`
--

DROP TABLE IF EXISTS `Belongs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Belongs` (
  `achievementID` int NOT NULL,
  `gameID` int NOT NULL,
  PRIMARY KEY (`achievementID`,`gameID`),
  KEY `gameID` (`gameID`),
  CONSTRAINT `belongs_ibfk_1` FOREIGN KEY (`achievementID`) REFERENCES `Achievement` (`achievementID`),
  CONSTRAINT `belongs_ibfk_2` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `subCate` varchar(255) NOT NULL,
  `mainCate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subCate`),
  KEY `mainCate` (`mainCate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Community`
--

DROP TABLE IF EXISTS `Community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Community` (
  `communityID` int NOT NULL AUTO_INCREMENT,
  `gameID` int DEFAULT NULL,
  PRIMARY KEY (`communityID`),
  KEY `gameID` (`gameID`),
  CONSTRAINT `community_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `contains`
--

DROP TABLE IF EXISTS `contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contains` (
  `gameID` int NOT NULL,
  `wishlistID` int NOT NULL,
  PRIMARY KEY (`gameID`,`wishlistID`),
  KEY `wishlistID` (`wishlistID`),
  CONSTRAINT `contains_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`),
  CONSTRAINT `contains_ibfk_2` FOREIGN KEY (`wishlistID`) REFERENCES `WishlistGame` (`wishlistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Dashboard`
--

DROP TABLE IF EXISTS `Dashboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dashboard` (
  `dashboardID` int NOT NULL AUTO_INCREMENT,
  `post` text,
  `date` varchar(10) DEFAULT NULL,
  `Author` varchar(255) DEFAULT NULL,
  `communityID` int DEFAULT NULL,
  PRIMARY KEY (`dashboardID`),
  KEY `communityID` (`communityID`)
) ENGINE=InnoDB AUTO_INCREMENT=1015 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Game`
--

DROP TABLE IF EXISTS `Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Game` (
  `gameID` int NOT NULL,
  `publisherID` int DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `mainCate` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `release` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`gameID`),
  KEY `publisherID` (`publisherID`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`publisherID`) REFERENCES `Publisher` (`publisherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GroupBy`
--

DROP TABLE IF EXISTS `GroupBy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GroupBy` (
  `gameID` int NOT NULL,
  `subCate` varchar(255) NOT NULL,
  PRIMARY KEY (`gameID`,`subCate`),
  KEY `subCate` (`subCate`),
  CONSTRAINT `groupby_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`),
  CONSTRAINT `groupby_ibfk_2` FOREIGN KEY (`subCate`) REFERENCES `Category` (`mainCate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `has`
--

DROP TABLE IF EXISTS `has`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `has` (
  `gameID` int NOT NULL,
  `CommunityID` int NOT NULL,
  PRIMARY KEY (`gameID`,`CommunityID`),
  KEY `CommunityID` (`CommunityID`),
  CONSTRAINT `has_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `includes`
--

DROP TABLE IF EXISTS `includes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `includes` (
  `CommunityID` int NOT NULL,
  `dashboardID` int NOT NULL,
  PRIMARY KEY (`CommunityID`,`dashboardID`),
  KEY `includes_ibfk_2` (`dashboardID`),
  CONSTRAINT `includes_ibfk_2` FOREIGN KEY (`dashboardID`) REFERENCES `Dashboard` (`dashboardID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Link`
--

DROP TABLE IF EXISTS `Link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Link` (
  `userID` int NOT NULL,
  `gameID` int NOT NULL,
  `wishlistID` int NOT NULL,
  PRIMARY KEY (`userID`,`gameID`,`wishlistID`),
  KEY `gameID` (`gameID`),
  KEY `wishlistID` (`wishlistID`),
  CONSTRAINT `link_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `User` (`userID`),
  CONSTRAINT `link_ibfk_2` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`),
  CONSTRAINT `link_ibfk_3` FOREIGN KEY (`wishlistID`) REFERENCES `WishlistUser` (`wishlistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Publisher`
--

DROP TABLE IF EXISTS `Publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Publisher` (
  `publisherID` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `year` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`publisherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `userID` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `wishlistID` int DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `WishlistGame`
--

DROP TABLE IF EXISTS `WishlistGame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WishlistGame` (
  `wishlistID` int NOT NULL,
  `gameID` int NOT NULL,
  PRIMARY KEY (`wishlistID`,`gameID`),
  KEY `gameID` (`gameID`),
  CONSTRAINT `wishlistgame_ibfk_1` FOREIGN KEY (`wishlistID`) REFERENCES `WishlistUser` (`wishlistID`),
  CONSTRAINT `wishlistgame_ibfk_2` FOREIGN KEY (`gameID`) REFERENCES `Game` (`gameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `WishlistUser`
--

DROP TABLE IF EXISTS `WishlistUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WishlistUser` (
  `wishlistID` int NOT NULL,
  `userID` int DEFAULT NULL,
  PRIMARY KEY (`wishlistID`),
  KEY `userID` (`userID`),
  CONSTRAINT `wishlistuser_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `User` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 13:43:05
>>>>>>> 04a4a3d (implement add to wishlist function)
