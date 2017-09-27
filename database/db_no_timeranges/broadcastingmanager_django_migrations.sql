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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-09-21 01:36:38.879663'),(2,'auth','0001_initial','2017-09-21 01:36:39.548844'),(3,'admin','0001_initial','2017-09-21 01:36:39.751002'),(4,'admin','0002_logentry_remove_auto_add','2017-09-21 01:36:39.775879'),(5,'areas','0001_initial','2017-09-21 01:36:39.806914'),(6,'contenttypes','0002_remove_content_type_name','2017-09-21 01:36:39.903163'),(7,'auth','0002_alter_permission_name_max_length','2017-09-21 01:36:39.967456'),(8,'auth','0003_alter_user_email_max_length','2017-09-21 01:36:40.024539'),(9,'auth','0004_alter_user_username_opts','2017-09-21 01:36:40.042653'),(10,'auth','0005_alter_user_last_login_null','2017-09-21 01:36:40.088577'),(11,'auth','0006_require_contenttypes_0002','2017-09-21 01:36:40.093964'),(12,'auth','0007_alter_validators_add_error_messages','2017-09-21 01:36:40.110738'),(13,'auth','0008_alter_user_username_max_length','2017-09-21 01:36:40.168447'),(14,'televisions','0001_initial','2017-09-21 01:36:40.204470'),(15,'basestations','0001_initial','2017-09-21 01:36:40.316343'),(16,'broadcasts','0001_initial','2017-09-21 01:36:40.419828'),(17,'broadcastingstatus','0001_initial','2017-09-21 01:36:40.511989'),(18,'machinelocations','0001_initial','2017-09-21 01:36:40.542815'),(19,'unitprices','0001_initial','2017-09-21 01:36:40.640010'),(20,'contracts','0001_initial','2017-09-21 01:36:40.964292'),(21,'sessions','0001_initial','2017-09-21 01:36:41.008068'),(22,'timeranges','0001_initial','2017-09-21 01:36:41.127720');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-21  8:39:47
