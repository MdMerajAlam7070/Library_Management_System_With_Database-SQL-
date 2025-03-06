CREATE DATABASE  IF NOT EXISTS `mydata` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydata`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `Member_Type` varchar(45) DEFAULT NULL,
  `Roll_No` varchar(45) NOT NULL,
  `ID_No` varchar(45) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `Surname` varchar(45) DEFAULT NULL,
  `Loc_Address` varchar(45) DEFAULT NULL,
  `Perm_Address` varchar(45) DEFAULT NULL,
  `Pin_Code` varchar(45) DEFAULT NULL,
  `Mobile_No` varchar(45) DEFAULT NULL,
  `Book_Id` varchar(45) DEFAULT NULL,
  `Book_Title` varchar(45) DEFAULT NULL,
  `Auther_Name` varchar(45) DEFAULT NULL,
  `Date_Borrowed` varchar(45) DEFAULT NULL,
  `Date_Due` varchar(45) DEFAULT NULL,
  `Days_On_Book` varchar(45) DEFAULT NULL,
  `Late_Return_Fine` varchar(45) DEFAULT NULL,
  `Date_Over_Due` varchar(45) DEFAULT NULL,
  `Actual_Price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Roll_No`,`ID_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('Student','2102161520036','908708917737','Md Meraj ','Alam','Parichowk','Darbhanga(Bihar)1','847233','7070950617','BKID05454','Knowledge of Relation with Database','Meraj Khan','2025-03-02','2025-03-17','15','Rs.50','No','Rs.1200'),('Student','2102161520037','908708917738','Md Meraj 1','Alam','Parichowk','Darbhanga(Bihar)1','847233','7070950617','BKID05454','Knowledge of Relation with Database','Meraj Khan','2025-03-02','2025-03-17','15','Rs.50','No','Rs.1200'),('Student','2102161520044','908708917563','Altaf','Alam','Parichowk','Darbhanga(Bihar)1','847233','7070950617','BKID05454','Knowledge of Relation with Database','Meraj Khan','2025-03-02','2025-03-17','15','Rs.50','No','Rs.1200');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-06 13:18:42
