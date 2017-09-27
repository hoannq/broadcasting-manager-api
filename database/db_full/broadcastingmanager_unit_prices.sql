-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: broadcastingmanager
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
-- Table structure for table `unit_prices`
--

DROP TABLE IF EXISTS `unit_prices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unit_prices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `broadcasting_hours` varchar(2) NOT NULL,
  `renew` smallint(6) NOT NULL,
  `power_type` varchar(2) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `machine_location_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `unit_prices_machine_location_id_6fdbb152_fk_machine_locations_id` (`machine_location_id`),
  CONSTRAINT `unit_prices_machine_location_id_6fdbb152_fk_machine_locations_id` FOREIGN KEY (`machine_location_id`) REFERENCES `machine_locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_prices`
--

LOCK TABLES `unit_prices` WRITE;
/*!40000 ALTER TABLE `unit_prices` DISABLE KEYS */;
INSERT INTO `unit_prices` VALUES (1,'19',1,'10',89000,1),(2,'19',1,'5',73000,1),(3,'19',1,'2',59000,1),(4,'19',0,'10',83000,1),(5,'19',0,'5',68000,1),(6,'19',0,'2',53000,1),(7,'24',1,'10',93000,1),(8,'24',1,'5',77000,1),(9,'24',1,'2',62000,1),(10,'24',0,'10',85000,1),(11,'24',0,'5',69000,1),(12,'24',0,'2',55000,1),(13,'19',1,'10',91000,2),(14,'19',1,'5',75000,2),(15,'19',1,'2',61000,2),(16,'19',0,'10',84000,2),(17,'19',0,'5',69000,2),(18,'19',0,'2',54000,2),(19,'24',1,'10',96000,2),(20,'24',1,'5',80000,2),(21,'24',1,'2',65000,2),(22,'24',0,'10',86000,2),(23,'24',0,'5',71000,2),(24,'24',0,'2',56000,2),(25,'19',1,'10',94000,3),(26,'19',1,'5',79000,3),(27,'19',1,'2',64000,3),(28,'19',0,'10',86000,3),(29,'19',0,'5',71000,3),(30,'19',0,'2',56000,3),(31,'24',1,'10',100000,3),(32,'24',1,'5',84000,3),(33,'24',1,'2',70000,3),(34,'24',0,'10',88000,3),(35,'24',0,'5',73000,3),(36,'24',0,'2',58000,3),(37,'19',1,'10',95000,4),(38,'19',1,'5',78000,4),(39,'19',1,'2',62000,4),(40,'19',0,'10',89000,4),(41,'19',0,'5',72000,4),(42,'19',0,'2',56000,4),(43,'24',1,'10',98000,4),(44,'24',1,'5',80000,4),(45,'24',1,'2',64000,4),(46,'24',0,'10',90000,4),(47,'24',0,'5',73000,4),(48,'24',0,'2',57000,4),(49,'19',1,'10',97000,5),(50,'19',1,'5',80000,5),(51,'19',1,'2',64000,5),(52,'19',0,'10',90000,5),(53,'19',0,'5',73000,5),(54,'19',0,'2',57000,5),(55,'24',1,'10',101000,5),(56,'24',1,'5',83000,5),(57,'24',1,'2',67000,5),(58,'24',0,'10',91000,5),(59,'24',0,'5',75000,5),(60,'24',0,'2',59000,5);
/*!40000 ALTER TABLE `unit_prices` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-21  8:34:48
