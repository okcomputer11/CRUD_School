-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: School
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `register` int NOT NULL AUTO_INCREMENT,
  `dni` varchar(10) NOT NULL,
  `class_division` varchar(3) NOT NULL,
  `first_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `day_birth` date DEFAULT NULL,
  `status` varchar(1) NOT NULL DEFAULT 'R',
  `sexo` varchar(1) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `line_phone` varchar(20) DEFAULT NULL,
  `movile_phone1` varchar(20) DEFAULT NULL,
  `movile_phone2` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`register`,`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'98.167.542','1-1','Manuel','Lopez','2001-12-21','R','M','None','None','None','None'),(2,'45.287.983','1-1','Julia','Gonzalez','2001-05-18','R','F','None','None','None','None'),(3,'56.298.177','1-1','Coloradito','Roberto','1983-10-29','R','D','None','None','None','None'),(5,'67.726.224','1-1','Ana','Garcia','2005-01-13','R','F','None','None','None','None'),(6,'67.983.080','1-2','Julian','Peralta','2001-08-23','','M','','','',''),(7,'67.982.132','1-2','Ramiro','Pons','1997-02-15','','M','','','',''),(8,'45.983.265','1-3','Manuel','Lopez','1999-04-17','','M','','','',''),(9,'73.929.772','1-2','Maria','Roza','2002-06-27','','F','','','',''),(10,'64.882.107','1-2','Lucrecia','Barros','2001-04-07','','F','','','',''),(11,'67.077.284','1-3','Brenda','Lopez','2004-09-30','','F','','','',''),(14,'29.278.122','4-4','Romina','Gimenez','1987-10-03','E','F','','','',''),(15,'57.904.049','1-2','Juana','Vitale','1997-09-02','','F','','','','');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-20 18:49:39
