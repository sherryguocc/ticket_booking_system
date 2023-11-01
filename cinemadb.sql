CREATE DATABASE IF NOT EXISTS cinemadb;
USE cinemadb;
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movieID` INT AUTO_INCREMENT PRIMARY KEY,
  `title` varchar(255) NOT NULL,
  `description` text,
  `durationMins` int DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `releaseDate` date DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'showing'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2191 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seat`
--

DROP TABLE IF EXISTS `seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seat` (
  `seatID` int NOT NULL AUTO_INCREMENT,
  `hallID` int NOT NULL,
  `seatPosition` varchar(255) NOT NULL,
  PRIMARY KEY (`seatID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seat_allocation`
--

DROP TABLE IF EXISTS `seat_allocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seat_allocation` (
  `allocationID` int NOT NULL AUTO_INCREMENT,
  `screeningID` int NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  `seatNumber` int NOT NULL,
  `status` enum('booked','available') NOT NULL,
  PRIMARY KEY (`allocationID`),
  KEY `screeningID` (`screeningID`),
  CONSTRAINT `seat_allocation_ibfk_1` FOREIGN KEY (`screeningID`) REFERENCES `screening` (`screeningID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 16:06:29