CREATE DATABASE  IF NOT EXISTS `cinemadb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cinemadb`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: cinemadb
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bookingID` int NOT NULL AUTO_INCREMENT,
  `userID` int DEFAULT NULL,
  `numberOfSeat` int NOT NULL,
  `bookingDate` date NOT NULL,
  `screeningID` int NOT NULL,
  `seatList` json DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `paymentID` int DEFAULT NULL,
  `status` enum('pending','paid','cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`bookingID`),
  KEY `customerID` (`userID`),
  KEY `screeningID` (`screeningID`),
  KEY `paymentID` (`paymentID`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`screeningID`) REFERENCES `screening` (`screeningID`),
  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`paymentID`) REFERENCES `payment` (`paymentID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon` (
  `couponID` int NOT NULL AUTO_INCREMENT,
  `expiryDate` date NOT NULL,
  `discount` decimal(10,2) NOT NULL,
  `couponCode` varchar(255) NOT NULL,
  PRIMARY KEY (`couponID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon`
--

LOCK TABLES `coupon` WRITE;
/*!40000 ALTER TABLE `coupon` DISABLE KEYS */;
INSERT INTO `coupon` VALUES (1,'2024-12-01',0.90,'AAAA'),(2,'2023-09-30',0.80,'BBBB');
/*!40000 ALTER TABLE `coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditcard`
--

DROP TABLE IF EXISTS `creditcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditcard` (
  `creditcardID` int NOT NULL AUTO_INCREMENT,
  `cardNumber` varchar(16) NOT NULL,
  `cardType` varchar(50) NOT NULL,
  `expiryDate` date NOT NULL,
  `nameOnCard` varchar(255) NOT NULL,
  `securityNumber` varchar(4) NOT NULL,
  PRIMARY KEY (`creditcardID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditcard`
--

LOCK TABLES `creditcard` WRITE;
/*!40000 ALTER TABLE `creditcard` DISABLE KEYS */;
/*!40000 ALTER TABLE `creditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `debitcard`
--

DROP TABLE IF EXISTS `debitcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `debitcard` (
  `debitcardID` int NOT NULL AUTO_INCREMENT,
  `cardNumber` varchar(16) NOT NULL,
  `bankName` varchar(255) NOT NULL,
  `nameOnCard` varchar(255) NOT NULL,
  PRIMARY KEY (`debitcardID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `debitcard`
--

LOCK TABLES `debitcard` WRITE;
/*!40000 ALTER TABLE `debitcard` DISABLE KEYS */;
/*!40000 ALTER TABLE `debitcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hall`
--

DROP TABLE IF EXISTS `hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hall` (
  `hallID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `totalSeats` int NOT NULL,
  `listOfSeat` json NOT NULL,
  PRIMARY KEY (`hallID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hall`
--

LOCK TABLES `hall` WRITE;
/*!40000 ALTER TABLE `hall` DISABLE KEYS */;
INSERT INTO `hall` VALUES (1,'Hall One',120,'[\"seat1-1\", \"seat1-2\", \"seat1-3\", \"seat1-4\", \"seat1-5\", \"seat1-6\", \"seat1-7\", \"seat1-8\", \"seat1-9\", \"seat1-10\", \"seat1-11\", \"seat1-12\", \"seat2-1\", \"seat2-2\", \"seat2-3\", \"seat2-4\", \"seat2-5\", \"seat2-6\", \"seat2-7\", \"seat2-8\", \"seat2-9\", \"seat2-10\", \"seat2-11\", \"seat2-12\", \"seat3-1\", \"seat3-2\", \"seat3-3\", \"seat3-4\", \"seat3-5\", \"seat3-6\", \"seat3-7\", \"seat3-8\", \"seat3-9\", \"seat3-10\", \"seat3-11\", \"seat3-12\", \"seat4-1\", \"seat4-2\", \"seat4-3\", \"seat4-4\", \"seat4-5\", \"seat4-6\", \"seat4-7\", \"seat4-8\", \"seat4-9\", \"seat4-10\", \"seat4-11\", \"seat4-12\", \"seat5-1\", \"seat5-2\", \"seat5-3\", \"seat5-4\", \"seat5-5\", \"seat5-6\", \"seat5-7\", \"seat5-8\", \"seat5-9\", \"seat5-10\", \"seat5-11\", \"seat5-12\", \"seat6-1\", \"seat6-2\", \"seat6-3\", \"seat6-4\", \"seat6-5\", \"seat6-6\", \"seat6-7\", \"seat6-8\", \"seat6-9\", \"seat6-10\", \"seat6-11\", \"seat6-12\", \"seat7-1\", \"seat7-2\", \"seat7-3\", \"seat7-4\", \"seat7-5\", \"seat7-6\", \"seat7-7\", \"seat7-8\", \"seat7-9\", \"seat7-10\", \"seat7-11\", \"seat7-12\", \"seat8-1\", \"seat8-2\", \"seat8-3\", \"seat8-4\", \"seat8-5\", \"seat8-6\", \"seat8-7\", \"seat8-8\", \"seat8-9\", \"seat8-10\", \"seat8-11\", \"seat8-12\", \"seat9-1\", \"seat9-2\", \"seat9-3\", \"seat9-4\", \"seat9-5\", \"seat9-6\", \"seat9-7\", \"seat9-8\", \"seat9-9\", \"seat9-10\", \"seat9-11\", \"seat9-12\", \"seat10-1\", \"seat10-2\", \"seat10-3\", \"seat10-4\", \"seat10-5\", \"seat10-6\", \"seat10-7\", \"seat10-8\", \"seat10-9\", \"seat10-10\", \"seat10-11\", \"seat10-12\"]'),(2,'Hall Two',90,'[\"seat1-1\", \"seat1-2\", \"seat1-3\", \"seat1-4\", \"seat1-5\", \"seat1-6\", \"seat1-7\", \"seat1-8\", \"seat1-9\", \"seat1-10\", \"seat2-1\", \"seat2-2\", \"seat2-3\", \"seat2-4\", \"seat2-5\", \"seat2-6\", \"seat2-7\", \"seat2-8\", \"seat2-9\", \"seat2-10\", \"seat3-1\", \"seat3-2\", \"seat3-3\", \"seat3-4\", \"seat3-5\", \"seat3-6\", \"seat3-7\", \"seat3-8\", \"seat3-9\", \"seat3-10\", \"seat4-1\", \"seat4-2\", \"seat4-3\", \"seat4-4\", \"seat4-5\", \"seat4-6\", \"seat4-7\", \"seat4-8\", \"seat4-9\", \"seat4-10\", \"seat5-1\", \"seat5-2\", \"seat5-3\", \"seat5-4\", \"seat5-5\", \"seat5-6\", \"seat5-7\", \"seat5-8\", \"seat5-9\", \"seat5-10\", \"seat6-1\", \"seat6-2\", \"seat6-3\", \"seat6-4\", \"seat6-5\", \"seat6-6\", \"seat6-7\", \"seat6-8\", \"seat6-9\", \"seat6-10\", \"seat7-1\", \"seat7-2\", \"seat7-3\", \"seat7-4\", \"seat7-5\", \"seat7-6\", \"seat7-7\", \"seat7-8\", \"seat7-9\", \"seat7-10\", \"seat8-1\", \"seat8-2\", \"seat8-3\", \"seat8-4\", \"seat8-5\", \"seat8-6\", \"seat8-7\", \"seat8-8\", \"seat8-9\", \"seat8-10\", \"seat9-1\", \"seat9-2\", \"seat9-3\", \"seat9-4\", \"seat9-5\", \"seat9-6\", \"seat9-7\", \"seat9-8\", \"seat9-9\", \"seat9-10\"]'),(3,'Hall Three',110,'[\"seat1-1\", \"seat1-2\", \"seat1-3\", \"seat1-4\", \"seat1-5\", \"seat1-6\", \"seat1-7\", \"seat1-8\", \"seat1-9\", \"seat1-10\", \"seat1-11\", \"seat2-1\", \"seat2-2\", \"seat2-3\", \"seat2-4\", \"seat2-5\", \"seat2-6\", \"seat2-7\", \"seat2-8\", \"seat2-9\", \"seat2-10\", \"seat2-11\", \"seat3-1\", \"seat3-2\", \"seat3-3\", \"seat3-4\", \"seat3-5\", \"seat3-6\", \"seat3-7\", \"seat3-8\", \"seat3-9\", \"seat3-10\", \"seat3-11\", \"seat4-1\", \"seat4-2\", \"seat4-3\", \"seat4-4\", \"seat4-5\", \"seat4-6\", \"seat4-7\", \"seat4-8\", \"seat4-9\", \"seat4-10\", \"seat4-11\", \"seat5-1\", \"seat5-2\", \"seat5-3\", \"seat5-4\", \"seat5-5\", \"seat5-6\", \"seat5-7\", \"seat5-8\", \"seat5-9\", \"seat5-10\", \"seat5-11\", \"seat6-1\", \"seat6-2\", \"seat6-3\", \"seat6-4\", \"seat6-5\", \"seat6-6\", \"seat6-7\", \"seat6-8\", \"seat6-9\", \"seat6-10\", \"seat6-11\", \"seat7-1\", \"seat7-2\", \"seat7-3\", \"seat7-4\", \"seat7-5\", \"seat7-6\", \"seat7-7\", \"seat7-8\", \"seat7-9\", \"seat7-10\", \"seat7-11\", \"seat8-1\", \"seat8-2\", \"seat8-3\", \"seat8-4\", \"seat8-5\", \"seat8-6\", \"seat8-7\", \"seat8-8\", \"seat8-9\", \"seat8-10\", \"seat8-11\", \"seat9-1\", \"seat9-2\", \"seat9-3\", \"seat9-4\", \"seat9-5\", \"seat9-6\", \"seat9-7\", \"seat9-8\", \"seat9-9\", \"seat9-10\", \"seat9-11\", \"seat10-1\", \"seat10-2\", \"seat10-3\", \"seat10-4\", \"seat10-5\", \"seat10-6\", \"seat10-7\", \"seat10-8\", \"seat10-9\", \"seat10-10\", \"seat10-11\"]'),(4,'Hall Four',80,'[\"seat1-1\", \"seat1-2\", \"seat1-3\", \"seat1-4\", \"seat1-5\", \"seat1-6\", \"seat1-7\", \"seat1-8\", \"seat1-9\", \"seat1-10\", \"seat2-1\", \"seat2-2\", \"seat2-3\", \"seat2-4\", \"seat2-5\", \"seat2-6\", \"seat2-7\", \"seat2-8\", \"seat2-9\", \"seat2-10\", \"seat3-1\", \"seat3-2\", \"seat3-3\", \"seat3-4\", \"seat3-5\", \"seat3-6\", \"seat3-7\", \"seat3-8\", \"seat3-9\", \"seat3-10\", \"seat4-1\", \"seat4-2\", \"seat4-3\", \"seat4-4\", \"seat4-5\", \"seat4-6\", \"seat4-7\", \"seat4-8\", \"seat4-9\", \"seat4-10\", \"seat5-1\", \"seat5-2\", \"seat5-3\", \"seat5-4\", \"seat5-5\", \"seat5-6\", \"seat5-7\", \"seat5-8\", \"seat5-9\", \"seat5-10\", \"seat6-1\", \"seat6-2\", \"seat6-3\", \"seat6-4\", \"seat6-5\", \"seat6-6\", \"seat6-7\", \"seat6-8\", \"seat6-9\", \"seat6-10\", \"seat7-1\", \"seat7-2\", \"seat7-3\", \"seat7-4\", \"seat7-5\", \"seat7-6\", \"seat7-7\", \"seat7-8\", \"seat7-9\", \"seat7-10\", \"seat8-1\", \"seat8-2\", \"seat8-3\", \"seat8-4\", \"seat8-5\", \"seat8-6\", \"seat8-7\", \"seat8-8\", \"seat8-9\", \"seat8-10\"]');
/*!40000 ALTER TABLE `hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movieID` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text,
  `durationMins` int DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `releaseDate` date DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'showing',
  PRIMARY KEY (`movieID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'Barbie','A family-friendly animated film.',120,'English','2023-05-12','USA','Animation','showing'),(2,'Super Mario Bros: The Movie','An adventure comedy featuring iconic video game characters.',105,'English','2023-06-21','USA','Adventure','showing'),(3,'Auburn Hammer','A mystery thriller with unexpected twists.',135,'English','2023-04-05','USA','Thriller','showing'),(4,'Guardians of the Galaxy Vol. 3','Action-packed space adventure with beloved characters.',140,'English','2023-07-28','USA','Action','showing'),(5,'Fast & Furious 10','High-octane action and racing.',130,'English','2023-08-18','USA','Action','showing'),(6,'Spider-Man: Across the Multiverse','An animated journey through different dimensions.',115,'English','2023-06-14','USA','Animation','showing'),(7,'Crimson River','A thrilling crime drama set in a bustling city.',125,'Mandarin','2023-03-02','China','Crime','showing'),(8,'Wandering Earth 2','A sequel to the sci-fi epic.',150,'Mandarin','2023-07-07','China','Science Fiction','showing'),(9,'The Little Mermaid','A live-action adaptation of the classic fairy tale.',130,'English','2023-05-26','USA','Fantasy','showing'),(10,'Mission: Impossible 7 - Reckoning (Part 1)','Ethan Hunt returns for a high-stakes mission.',135,'English','2023-07-14','USA','Action','showing');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `notificationID` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `content` text NOT NULL,
  `userID` int DEFAULT NULL,
  PRIMARY KEY (`notificationID`),
  KEY `customerID` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `paymentID` int NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `couponID` int DEFAULT NULL,
  `creditCardID` int DEFAULT NULL,
  `debitCardID` int DEFAULT NULL,
  `status` enum('received','refund') NOT NULL DEFAULT 'received',
  PRIMARY KEY (`paymentID`),
  KEY `couponID` (`couponID`),
  KEY `creditCardID` (`creditCardID`),
  KEY `debitCardID` (`debitCardID`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`couponID`) REFERENCES `coupon` (`couponID`),
  CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`creditCardID`) REFERENCES `creditcard` (`creditcardID`),
  CONSTRAINT `payment_ibfk_3` FOREIGN KEY (`debitCardID`) REFERENCES `debitcard` (`debitcardID`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `screening`
--

DROP TABLE IF EXISTS `screening`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `screening` (
  `screeningID` int NOT NULL AUTO_INCREMENT,
  `movieID` int NOT NULL,
  `date` date NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  `hallID` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `status` varchar(255) DEFAULT 'showing',
  PRIMARY KEY (`screeningID`),
  KEY `movieID` (`movieID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `screening`
--

LOCK TABLES `screening` WRITE;
/*!40000 ALTER TABLE `screening` DISABLE KEYS */;
/*!40000 ALTER TABLE `screening` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `screeningseat`
--

DROP TABLE IF EXISTS `screeningseat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `screeningseat` (
  `screeningSeatID` int NOT NULL AUTO_INCREMENT,
  `screeningID` int DEFAULT NULL,
  `seatNumber` varchar(255) DEFAULT NULL,
  `HallID` int DEFAULT NULL,
  `status` enum('available','reserved','booked') DEFAULT NULL,
  PRIMARY KEY (`screeningSeatID`),
  KEY `screeningID` (`screeningID`),
  KEY `HallID` (`HallID`),
  CONSTRAINT `screeningseat_ibfk_1` FOREIGN KEY (`screeningID`) REFERENCES `screening` (`screeningID`),
  CONSTRAINT `screeningseat_ibfk_2` FOREIGN KEY (`HallID`) REFERENCES `hall` (`hallID`)
) ENGINE=InnoDB AUTO_INCREMENT=2971 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `screeningseat`
--

LOCK TABLES `screeningseat` WRITE;
/*!40000 ALTER TABLE `screeningseat` DISABLE KEYS */;
/*!40000 ALTER TABLE `screeningseat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','staff','customer') NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` text,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin1','$2b$12$/uXx3cpwmnqGqyurJxGoY.Ki82ZgqctKrNmsVy.h0qBeE6GwGDfTi','admin','Sherry','1234567890','Auckland','sherry@email.com'),(2,'staff1','$2b$12$/uXx3cpwmnqGqyurJxGoY.Ki82ZgqctKrNmsVy.h0qBeE6GwGDfTi','staff','Chaz','1234567899','Auckland','chaz@email.com'),(3,'customer1','$2b$12$/uXx3cpwmnqGqyurJxGoY.Ki82ZgqctKrNmsVy.h0qBeE6GwGDfTi','customer','Shinny','1234567888','Auckland','shinny@email.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-03 21:08:06
