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
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `areas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'Tây Bắc'),(2,'Đông Bắc'),(3,'Đồng Bằng Sông Hồng'),(4,'Bắc Trung Bộ'),(5,'Nam Trung Bộ'),(6,'Tây Nguyên'),(7,'Đông Nam Bộ'),(8,'Đồng Bằng Sông Cửu Long');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add area',7,'add_area'),(20,'Can change area',7,'change_area'),(21,'Can delete area',7,'delete_area'),(22,'Can add basestation',8,'add_basestation'),(23,'Can change basestation',8,'change_basestation'),(24,'Can delete basestation',8,'delete_basestation'),(25,'Can add broadcastingstatus',9,'add_broadcastingstatus'),(26,'Can change broadcastingstatus',9,'change_broadcastingstatus'),(27,'Can delete broadcastingstatus',9,'delete_broadcastingstatus'),(28,'Can add broadcast',10,'add_broadcast'),(29,'Can change broadcast',10,'change_broadcast'),(30,'Can delete broadcast',10,'delete_broadcast'),(31,'Can add contract',11,'add_contract'),(32,'Can change contract',11,'change_contract'),(33,'Can delete contract',11,'delete_contract'),(34,'Can add machinelocation',12,'add_machinelocation'),(35,'Can change machinelocation',12,'change_machinelocation'),(36,'Can delete machinelocation',12,'delete_machinelocation'),(37,'Can add television',13,'add_television'),(38,'Can change television',13,'change_television'),(39,'Can delete television',13,'delete_television'),(40,'Can add timerange',14,'add_timerange'),(41,'Can change timerange',14,'change_timerange'),(42,'Can delete timerange',14,'delete_timerange'),(43,'Can add unitprice',15,'add_unitprice'),(44,'Can change unitprice',15,'change_unitprice'),(45,'Can delete unitprice',15,'delete_unitprice');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_stations`
--

DROP TABLE IF EXISTS `base_stations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_stations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `alias_name` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `location` varchar(100) NOT NULL,
  `manage_type` varchar(10) NOT NULL,
  `description` longtext,
  `area_id` int(11) DEFAULT NULL,
  `television_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `base_stations_area_id_817f161e_fk_areas_id` (`area_id`),
  KEY `base_stations_television_id_36867cfa_fk_televisions_id` (`television_id`),
  CONSTRAINT `base_stations_area_id_817f161e_fk_areas_id` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `base_stations_television_id_36867cfa_fk_televisions_id` FOREIGN KEY (`television_id`) REFERENCES `televisions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_stations`
--

LOCK TABLES `base_stations` WRITE;
/*!40000 ALTER TABLE `base_stations` DISABLE KEYS */;
INSERT INTO `base_stations` VALUES (1,'Phòng phát sóng Vệ tinh Giảng Võ','Giảng Võ 1','43, Nguyễn Chí Thanh, phường Ngọc Khánh, quận Ba Đình, Thành phố Hà Nội','43, Nguyễn Chí Thanh','0','VTV1,2,3,4,6SD VTV1,3,6HD BAND C',3,3),(2,'Phòng phát sóng Hà Nội','Giảng Võ 2 - Hà Nội','phường Mễ Trì, quận Nam Từ Liêm, Thành phố Hà Nội','Mễ Trì Hà Nội','0','VTV1,2,3,6 VÀ MÁY PHÁT SỐ',3,3),(3,'Phòng phát sóng Tam Đảo','Tam Đảo - Vĩnh Phúc','Tam Đảo, Vĩnh Phúc','Tx Tam Đảo','0','VTV1 VÀ MÁY PHÁT SỐ',3,3),(4,'Phòng phát sóng THQG Hải Phòng','Trạm KTTV - Hải Phòng','Đồi Thiên Văn, phường Trần Thành Ngọ, quận Kiến An, Thành Phố Hải Phòng','Nha Khí Tượng HP','0','MÁY SỐ',3,3),(5,'Phòng Quản lý phát sóng Bắc Trung Bộ','Huế','Thừa Thiên - Huế','Tp Huế','0','VTV1,2,3,6 VÀ KHU VỰC',4,3),(6,'Phòng Quản lý phát sóng Miền Trung','Đà Nẵng','Cao điểm 620, Đài phát sóng Quốc gia Sơn Trà, đỉnh núi Sơn Trà, bán đảo Sơn Trà, phường Thọ Quang, quận Sơn Trà, TP Đà Nẵng','Sơn Trà','0','VTV1,2,3,6,KHU VỰC VÀ MÁY PHÁT SỐ',5,3),(7,'Phòng Quản lý phát sóng Nam Trung Bộ','Chóp Chài - Phú Yên','Phú Yên','Chóp Chài','0','VTV1,2,3,6 VÀ KHU VỰC',5,3),(8,'Phòng phát sóng Bình Dương','Thủ Dầu Một - Bình Dương','Đài PSQG Thủ Dầu Một, Xã An Thạnh, Huyện Thuận An, Thành phố Thủ Dầu Một, tỉnh Bình Dương.','Thủ Dầu Một - Bình Dương','0','VTV1,2,3,6 VÀ MÁY PHÁT SỐ',7,3),(9,'Phòng phát sóng THQG Bà Rịa - Vũng Tàu','Bà Rịa - Vũng Tàu','Bà Rịa, Vũng Tàu','Tx Bà Rịa','0','VTV1, 2, 3',7,3),(10,'Phòng phát sóng Cần Thơ','Cần Thơ','Đài PTTH Cần Thơ, 407 Đường 30/4, phường Hưng Lợi, quận Ninh Kiều, TP Cần Thơ','Tp Cần Thơ','0','VTV1,2,3,6,KHU VỰC VÀ MÁY PHÁT SỐ',8,3),(11,'Phòng phát sóng Cần Thơ tại Núi Sam','Cần Thơ - Núi Sam','Núi Sam Cần Thơ','Núi Sam','0','KHU VỰC',8,3),(12,'Hà Giang','Hà Giang','Hà Giang','Tx Hà Giang','0','',2,2),(13,'Lào Cai','Lào Cai','Lào Cai','Tp Lào Cai','0','',2,3),(14,'Cao Bằng','Cao Bằng','Cao Bằng','Tx Cao Bằng','0','',2,4),(15,'Điện Biên','Điện Biên','Điện Biên','Tp Điện Biên','0','',1,5),(16,'Lai Châu','Lai Châu','Lai Châu','Tx Lai Châu','0','',1,6),(17,'Tuyên Quang','Tuyên Quang','Tuyên Quang','Tx Tuyên Quang','0','',2,7),(18,'Yên Bái','Yên Bái','Yên Bái','Tp Yên Bái','0','',1,8),(19,'Sơn La','Sơn La','Sơn La','Tx Sơn La','0','',1,9),(20,'Bắc Kạn','Bắc Kạn','Bắc Kạn','Tx Bắc Kạn','0','',2,10),(21,'Lạng Sơn','Lạng Sơn','Lạng Sơn','Tp Lạng Sơn','0','',2,11),(22,'Lạng Sơn - Mẫu Sơn','Mẫu Sơn - Lạng Sơn','Lạng Sơn','Đỉnh Mẫu Sơn','0','',2,11),(23,'Hòa Bình','Hòa Bình','Hòa Bình','Tp Hòa Bình','0','',1,12),(24,'Hải Phòng','Hải Phòng','Hải Phòng','Tp Hải Phòng','0','',3,13),(25,'Quảng Ninh Hạ Long','Hạ Long - Quảng Ninh','Quảng Ninh Hạ Long','Tp Hạ Lọng','0','',2,14),(26,'Quảng Ninh Móng Cái','Móng Cái - Quảng Ninh','Quảng Ninh Móng Cái','Tx Móng Cái','0','',2,14),(27,'Thái Bình','Thái Bình','Thái Bình','Tp Thái Bình','0','',3,15),(28,'Nam Định','Nam Định','Nam Định','Tp Nam Định','0','',3,16),(29,'Ninh Bình','Ninh Bình','Ninh Bình','Tp Ninh Bình','0','',3,18),(30,'Thanh Hóa - Quyết Thắng','Quyết Thắng - Thanh Hóa','Thanh Hóa','Đồi Quyết Thắng','0','',4,19),(31,'Thanh Hóa - Bá Thước','Bá Thước - Thanh Hóa','Thanh Hóa','Đồi Bá Thước','0','',4,19),(32,'Nghệ An','Vinh - Nghệ An','Nghệ An','Tp Vinh','0','',4,20),(33,'Hà Tĩnh - Thiên Tượng','Thiên Tượng - Hà Tĩnh','Hà Tĩnh','Đồi Thiên Tượng','0','',4,21),(34,'Hà Tĩnh','Hà Tĩnh','Hà Tĩnh','Tp Hà Tĩnh','0','',4,21),(35,'Quảng Bình','Đồng Hới - Quảng Bình','Quảng Bình','Tp Đồng Hới','0','',4,22),(36,'Quảng Trị','Đông Hà - Quảng Trị','Quảng Trị','Tp Đông Hà','0','',4,23),(37,'Quảng Nam','Tam Kỳ - Quảng Nam','Quảng Nam','Tp Tam Kỳ','0','',5,24),(38,'Quảng Ngãi','Quảng Ngãi','Quảng Ngãi','Tp Quảng Ngãi','0','',5,25),(39,'Bình Định','Quy Nhơn - Bình Định','Bình Định','Núi Vũng Chua','0','',5,26),(40,'Khánh Hòa','Nha Trang - Khánh Hòa','Khánh Hòa','Đồng Đế (VOV)','0','',5,27),(41,'Ninh Thuận','Phan Rang - Ninh Thuận','Ninh Thuận','Tp Phan Rang','0','',5,28),(42,'Bình Thuận','Phan Thiết - Bình Thuận','Bình Thuận','Tp Phan Thiết','0','',5,29),(43,'Kon Tum','Kon Tum','Kon Tum','Tx Kon Tum','0','',6,30),(44,'Gia Lai Hàm Rồng','Playku - Gia Lai','Gia Lai Hàm Rồng','Tp Playcu','0','',6,31),(45,'Đắk Lắk Hà Lan','Hà Lan - Đắk Lắk','Đắk Lắk Hà Lan','Đèo Hà Lan','0','',6,32),(46,'Đắk Lắk BMT','Buôn Ma Thuột - Đắk Lắk','Đắk Lắk BMT','Buôn Ma Thuột','0','',6,32),(47,'Đắk Nông','Gia Nghĩa - Đắk Nông','Đắk Nông','Tx Gia Nghĩa','0','',6,33),(48,'Lâm Đồng Đà Lạt','Đà Lạt - Lâm Đồng','Lâm Đồng Đà Lạt','Tp Đà Lạt','0','',6,34),(49,'Lâm Đồng Cầu Đất','Cầu Đất - Lâm Đồng','Lâm Đồng Cầu Đất','Núi Cầu Đất','0','',6,34),(50,'Bình Phước','Bà Rá - Bình Phước','Bình Phước','Núi Bà Rá','0','',7,35),(51,'Tây Ninh','Bà Đen - Tây Ninh','Tây Ninh','Núi Bà Đen','0','',7,36),(52,'An Giang','Núi Cấm - An Giang','An Giang','Núi Cấm','0','',8,38),(53,'Bến Tre','Bến Tre','Bến Tre','Tx Bến Tre','0','',8,39),(54,'Sóc Trăng','Sóc Trăng','Sóc Trăng','Tx Sóc Trăng','0','',8,40),(55,'Kiên Giang Hà Tiên','Hà Tiên - Kiên Giang','Kiên Giang Hà Tiên','Tx Hà Tiên','0','',8,41),(56,'Kiên Giang Hòn Me','Hòn Me - Kiên Giang','Kiên Giang Hòn Me','Hòn Me','0','',8,41),(57,'Bạc Liêu','Bạc Liêu','Bạc Liêu','Tx Bạc Liêu','0','',8,42),(58,'Cà Mau','Cà Mau','Cà Mau','Tp Cà Mau','0','',8,43);
/*!40000 ALTER TABLE `base_stations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `broadcasting_status`
--

DROP TABLE IF EXISTS `broadcasting_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `broadcasting_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `power_T` varchar(10) DEFAULT NULL,
  `power_PX` varchar(10) DEFAULT NULL,
  `reporter` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `broadcast_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `broadcasting_status_broadcast_id_750fc399_fk_broadcasts_id` (`broadcast_id`),
  CONSTRAINT `broadcasting_status_broadcast_id_750fc399_fk_broadcasts_id` FOREIGN KEY (`broadcast_id`) REFERENCES `broadcasts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `broadcasting_status`
--

LOCK TABLES `broadcasting_status` WRITE;
/*!40000 ALTER TABLE `broadcasting_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `broadcasting_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `broadcasts`
--

DROP TABLE IF EXISTS `broadcasts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `broadcasts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `contract_start_date` date NOT NULL,
  `contract_end_date` date NOT NULL,
  `broadcasting_hours` varchar(2) NOT NULL,
  `frequency_channel` varchar(2) DEFAULT NULL,
  `power` varchar(6) DEFAULT NULL,
  `broadcasting_type` varchar(15) NOT NULL,
  `time_segment` smallint(6) NOT NULL,
  `machine_brand` varchar(20) DEFAULT NULL,
  `description` longtext,
  `is_by_contract` tinyint(1) NOT NULL,
  `is_by_region` tinyint(1) NOT NULL,
  `base_station_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `broadcasts_base_station_id_45c1fa2f_fk_base_stations_id` (`base_station_id`),
  CONSTRAINT `broadcasts_base_station_id_45c1fa2f_fk_base_stations_id` FOREIGN KEY (`base_station_id`) REFERENCES `base_stations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `broadcasts`
--

LOCK TABLES `broadcasts` WRITE;
/*!40000 ALTER TABLE `broadcasts` DISABLE KEYS */;
INSERT INTO `broadcasts` VALUES (1,'VTV_So','2015-01-01','2018-12-31','24','','0.25','Vệ Tinh',1,'','VTV1;VTV2;VTV3;VTV6',0,0,1),(2,'VTV1','2015-01-01','2018-12-31','24','9','30','Tương tự',1,'Plish','',0,0,2),(3,'VTV2','2015-01-01','2018-12-31','24','11','10','Tương tự',1,'HARIS','',0,0,2),(4,'VTV3','2015-01-01','2018-12-31','24','22','20','Tương tự',1,'THOMCAST','',0,0,2),(5,'VTV6','2015-01-01','2018-12-31','24','54','10','Tương tự',1,'HARIS','',0,0,2),(6,'VTV_So','2015-01-01','2018-12-31','24','51','5','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',0,0,2),(7,'VTV1','2015-01-01','2018-12-31','24','3','20','Tương tự',1,'THOMCAST','',0,0,3),(8,'VTV_So','2015-01-01','2018-12-31','24','26','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',0,0,3),(9,'VTV_So','2015-01-01','2018-12-31','24','43','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',0,0,4),(10,'VTV1','2015-01-01','2018-12-31','24','22','10','Tương tự',1,'HARIS','',0,0,5),(11,'VTV2','2015-01-01','2018-12-31','24','46','10','Tương tự',1,'Btesa','',0,0,5),(12,'VTV3','2015-01-01','2018-12-31','24','7','5','Tương tự',1,'THOMCAST','',0,0,5),(13,'VTV6','2015-01-01','2018-12-31','24','41','10','Tương tự',1,'HARIS','',0,0,5),(14,'VTV_Hue','2015-01-01','2018-12-31','24','25','10','Tương tự',1,'HARIS','',0,1,5),(15,'VTV1','2015-01-01','2018-12-31','24','12','10','Tương tự',1,'HARIS','',0,0,6),(16,'VTV2','2015-01-01','2018-12-31','24','26','10','Tương tự',1,'Btesa','',0,0,6),(17,'VTV3','2015-01-01','2018-12-31','24','21','10','Tương tự',1,'R&S','',0,0,6),(18,'VTV6','2015-01-01','2018-12-31','24','47','10','Tương tự',1,'HARIS','',0,0,6),(19,'VTV_So','2015-01-01','2018-12-31','24','49','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6;VTV_DaNang',0,0,6),(20,'VTV_DaNang','2015-01-01','2018-12-31','24','9','10','Tương tự',1,'HARIS','',0,1,6),(21,'VTV1','2015-01-01','2018-12-31','24','9','2','Tương tự',1,'Btesa','',0,0,7),(22,'VTV2','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'NEC','',0,0,7),(23,'VTV3','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'R&S','',0,0,7),(24,'VTV6','2015-01-01','2018-12-31','24','41','5','Tương tự',1,'HARIS','',0,0,7),(25,'VTV_PhuYen','2015-01-01','2018-12-31','24','7','5','Tương tự',1,'R&S','',0,1,7),(26,'VTV1','2015-01-01','2018-12-31','24','21','50','Tương tự',1,'Toshiba','',0,0,8),(27,'VTV2','2015-01-01','2018-12-31','24','46','10','Tương tự',1,'HARIS','',0,0,8),(28,'VTV3','2015-01-01','2018-12-31','24','28','50','Tương tự',1,'Toshiba','',0,0,8),(29,'VTV6','2015-01-01','2018-12-31','24','48','10','Tương tự',1,'HARIS','',0,0,8),(30,'VTV_So','2015-01-01','2018-12-31','24','25','5','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6;VTV_DaNang',0,0,8),(31,'VTV1','2015-01-01','2018-12-31','24','38','5','Tương tự',1,'Btesa','',0,0,9),(32,'VTV2','2015-01-01','2018-12-31','24','61','5','Tương tự',1,'R&S','',0,0,9),(33,'VTV3','2015-01-01','2018-12-31','24','24','5','Tương tự',1,'R&S','',0,0,9),(34,'VTV1','2015-01-01','2018-12-31','24','46','30','Tương tự',1,'VIHITECH','',0,0,10),(35,'VTV2','2015-01-01','2018-12-31','24','12','10','Tương tự',1,'NEC','',0,0,10),(36,'VTV3','2015-01-01','2018-12-31','24','6','20','Tương tự',1,'HARIS','',0,0,10),(37,'VTV6','2015-01-01','2018-12-31','24','22','5','Tương tự',1,'HARIS','',0,0,10),(38,'VTV_So','2015-01-01','2018-12-31','24','45','2','Số',1,'R&S','',0,0,10),(39,'VTVCT1','2015-01-01','2018-12-31','24','49','30','Tương tự',1,'NEC','',0,1,10),(40,'VTVCT2','2015-01-01','2018-12-31','19','51','30','Tương tự',1,'R&S','',0,1,10),(41,'VTVCT1','2015-01-01','2018-12-31','24','56','1','Tương tự',1,'HARIS','',0,1,11),(42,'VTVCT2','2015-01-01','2018-12-31','19','11','0.1','Tương tự',1,'NEC','',0,1,11),(43,'VTV1','2015-01-01','2018-12-31','19','8','2','Tương tự',1,'Btesa','',1,0,12),(44,'VTV2','2015-01-01','2018-12-31','19','23','5','Tương tự',1,'Btesa','',1,0,12),(45,'VTV3','2015-01-01','2018-12-31','19','6','2','Tương tự',2,'Btesa','',1,0,12),(46,'VTV1','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'VTC','',1,0,13),(47,'VTV2','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'R&S','',1,0,13),(48,'VTV3','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'R&S','',1,0,13),(49,'VTV6','2015-01-01','2018-12-31','24','27','5','Tương tự',1,'Harris','',1,0,13),(50,'VTV1','2015-01-01','2018-12-31','24','8','0.5','Tương tự',1,'thcst','',1,0,14),(51,'VTV2','2015-01-01','2018-12-31','19','11','1','Tương tự',3,'thson','',1,0,14),(52,'VTV3','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'Btesa','',1,0,14),(53,'VTV1','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'R&S','',1,0,15),(54,'VTV2','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'VTC','',1,0,15),(55,'VTV3','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'R&S','',1,0,15),(56,'VTV6','2015-01-01','2018-12-31','24','10','2','Tương tự',1,'VTC','',1,0,15),(57,'VTV1','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'R&S','',1,0,16),(58,'VTV2','2015-01-01','2018-12-31','24','8','2','Tương tự',1,'R&S','',1,0,16),(59,'VTV3','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'R&S','',1,0,16),(60,'VTV2','2015-01-01','2018-12-31','24','34','5','Tương tự',1,'Harris','',1,0,17),(61,'VTV3','2015-01-01','2018-12-31','24','26','5','Tương tự',1,'Harris','',1,0,17),(62,'VTV1','2015-01-01','2018-12-31','24','10','2','Tương tự',1,'Harris','',1,0,18),(63,'VTV2','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'Btesa','',1,0,18),(64,'VTV3','2015-01-01','2018-12-31','19','27','5','Tương tự',1,'Harris','',1,0,18),(65,'VTV1','2015-01-01','2018-12-31','24','8','2','Tương tự',1,'VTC','',1,0,19),(66,'VTV2','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'VTC','',1,0,19),(67,'VTV3','2015-01-01','2018-12-31','24','10','1','Tương tự',1,'VTC','',1,0,19),(68,'VTV1','2015-01-01','2018-12-31','24','12','1.5','Tương tự',1,'Intedico','',1,0,20),(69,'VTV2','2015-01-01','2018-12-31','24','10','2','Tương tự',1,'R&S','',1,0,20),(70,'VTV3','2015-01-01','2018-12-31','24','25','5','Tương tự',1,'R&S','',1,0,20),(71,'VTV6','2015-01-01','2018-12-31','24','33','0.5','Tương tự',1,'Italia','',1,0,20),(72,'VTV1','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'R&S','',1,0,21),(73,'VTV2','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'Harris','',1,0,21),(74,'VTV3','2015-01-01','2018-12-31','24','7','2','Tương tự',1,'VTC','',1,0,21),(75,'VTV6','2015-01-01','2018-12-31','24','33','1','Tương tự',1,'Italia','',1,0,22),(76,'VTV1','2015-01-01','2018-12-31','24','12','1','Tương tự',1,'Harris','',1,0,23),(77,'VTV2','2015-01-01','2018-12-31','24','28','5','Tương tự',1,'R&S','',1,0,23),(78,'VTV3','2015-01-01','2018-12-31','24','33','5','Tương tự',1,'R&S','',1,0,23),(79,'VTV6','2015-01-01','2018-12-31','24','10','0.5','Tương tự',1,'VTC','',1,0,23),(80,'VTV1','2015-01-01','2018-12-31','24','10','5','Tương tự',1,'thcst','',1,0,24),(81,'VTV1','2015-01-01','2018-12-31','24','33','10','Tương tự',1,'NEC','',1,0,25),(82,'VTV3','2015-01-01','2018-12-31','24','27','2','Tương tự',1,'NEC','',1,0,25),(83,'VTV_So','2015-01-01','2018-12-31','24','31','10','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',1,0,25),(84,'VTV1','2015-01-01','2018-12-31','24','6','5','Tương tự',1,'Btesa','',1,0,26),(85,'VTV2','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'R&S','',1,0,26),(86,'VTV3','2015-01-01','2018-12-31','24','25','10','Tương tự',1,'R&S','',1,0,26),(87,'VTV1','2015-01-01','2018-12-31','24','32','5','Tương tự',1,'Btesa','',1,0,27),(88,'VTV2','2015-01-01','2018-12-31','24','6','5','Tương tự',1,'Thosn','',1,0,27),(89,'VTV2','2015-01-01','2018-12-31','24','25','5','Tương tự',1,'Harris','',1,0,28),(90,'VTV3','2015-01-01','2018-12-31','24','50','5','Tương tự',1,'Harris','',1,0,28),(91,'VTV6','2015-01-01','2018-12-31','24','53','10','Tương tự',1,'Harris','',1,0,28),(92,'VTV1','2015-01-01','2018-12-31','24','27','5','Tương tự',1,'Btesa','',1,0,29),(93,'VTV3','2015-01-01','2018-12-31','24','12','1','Tương tự',1,'NEC','',1,0,29),(94,'VTV1','2015-01-01','2018-12-31','24','24','5','Tương tự',1,'Harris','',1,0,30),(95,'VTV2','2015-01-01','2018-12-31','24','12','5','Tương tự',1,'CTC','',1,0,30),(96,'VTV3','2015-01-01','2018-12-31','24','7','5','Tương tự',1,'Optm','',1,0,30),(97,'VTV6','2015-01-01','2018-12-31','24','40','10','Tương tự',1,'Harris','',1,0,30),(98,'VTV3','2015-01-01','2018-12-31','24','10','2','Tương tự',1,'Italia','',1,0,31),(99,'VTV1','2015-01-01','2018-12-31','24','8','5','Tương tự',1,'R&S','',1,0,32),(100,'VTV3','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'NEC','',1,0,32),(101,'VTV6','2015-01-01','2018-12-31','24','43','10','Tương tự',1,'Harris','',1,0,32),(102,'VTV3','2015-01-01','2018-12-31','24','12','1','Tương tự',1,'Alpha','',1,0,33),(103,'VTV6','2015-01-01','2018-12-31','24','9','1','Tương tự',1,'Thomson','',1,0,33),(104,'VTV1','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'R&S','',1,0,34),(105,'VTV2','2015-01-01','2018-12-31','24','26','5','Tương tự',1,'Harris','',1,0,34),(106,'VTV_So','2015-01-01','2018-12-31','24','25','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',1,0,34),(107,'VTV1','2015-01-01','2018-12-31','24','12','5','Tương tự',1,'R&S','',1,0,35),(108,'VTV2','2015-01-01','2018-12-31','24','10','2','Tương tự',1,'CTC','',1,0,35),(109,'VTV3','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'Harris','',1,0,35),(110,'VTV1','2015-01-01','2018-12-31','24','6','5','Tương tự',1,'R&S','',1,0,36),(111,'VTV2','2015-01-01','2018-12-31','24','8','1','Tương tự',1,'Thomson','',1,0,36),(112,'VTV3','2015-01-01','2018-12-31','24','30','5','Tương tự',1,'Harris','',1,0,36),(113,'VTV1','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'Btesa','',1,0,37),(114,'VTV2','2015-01-01','2018-12-31','24','6','1','Tương tự',1,'VTC','',1,0,37),(115,'VTV3','2015-01-01','2018-12-31','24','33','5','Tương tự',1,'Harris','',1,0,37),(116,'VTV1','2015-01-01','2018-12-31','24','10','5','Tương tự',1,'Thocst','',1,0,38),(117,'VTV2','2015-01-01','2018-12-31','24','12','1','Tương tự',1,'thson','',1,0,38),(118,'VTV3','2015-01-01','2018-12-31','24','35','5','Tương tự',1,'Harris','',1,0,38),(119,'VTV1','2015-01-01','2018-12-31','24','12','5','Tương tự',1,'R&S','',1,0,39),(120,'VTV2','2015-01-01','2018-12-31','24','8','5','Tương tự',1,'TQT','',1,0,39),(121,'VTV3','2015-01-01','2018-12-31','24','27','5','Tương tự',1,'Harris','',1,0,39),(122,'VTV6','2015-01-01','2018-12-31','24','10','1','Tương tự',1,'TQT','',1,0,39),(123,'VTV1','2015-01-01','2018-12-31','24','12','2','Tương tự',1,'Btesa','',1,0,40),(124,'VTV2','2015-01-01','2018-12-31','24','22','5','Tương tự',1,'Harris','',1,0,40),(125,'VTV3','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'TQT','',1,0,40),(126,'VTV_So','2015-01-01','2018-12-31','24','31','10','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',1,0,40),(127,'VTV1','2015-01-01','2018-12-31','24','6','2','Tương tự',1,'Btesa','',1,0,41),(128,'VTV2','2015-01-01','2018-12-31','24','30','10','Tương tự',1,'R&S','',1,0,41),(129,'VTV3','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'R&S','',1,0,41),(130,'VTV1','2015-01-01','2018-12-31','24','8','2','Tương tự',1,'Btesa','',1,0,42),(131,'VTV2','2015-01-01','2018-12-31','24','26','5','Tương tự',1,'Harris','',1,0,42),(132,'VTV3','2015-01-01','2018-12-31','24','28','5','Tương tự',1,'Harris','',1,0,42),(133,'VTV1','2015-01-01','2018-12-31','24','8','2','Tương tự',1,'Btesa','',1,0,43),(134,'VTV2','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'R&S','',1,0,43),(135,'VTV3','2015-01-01','2018-12-31','24','23','5','Tương tự',1,'R&S','',1,0,43),(136,'VTV1','2015-01-01','2018-12-31','24','9','5','Tương tự',1,'Btesa','',1,0,44),(137,'VTV2','2015-01-01','2018-12-31','24','7','2','Tương tự',1,'TQT','',1,0,44),(138,'VTV3','2015-01-01','2018-12-31','24','25','10','Tương tự',1,'R&S','',1,0,44),(139,'VTV1','2015-01-01','2018-12-31','24','12','5','Tương tự',1,'Btesa','',1,0,45),(140,'VTV2','2015-01-01','2018-12-31','24','31','10','Tương tự',1,'R&S','',1,0,45),(141,'VTV3','2015-01-01','2018-12-31','24','28','10','Tương tự',1,'R&S','',1,0,45),(142,'VTV2','2015-01-01','2018-12-31','19','8','0.3','Tương tự',1,'TQT','',1,0,46),(143,'VTV6','2015-01-01','2018-12-31','24','38','1','Tương tự',1,'TQT','',1,0,46),(144,'VTV1','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'R&S','',1,0,47),(145,'VTV2','2015-01-01','2018-12-31','24','24','5','Tương tự',1,'R&S','',1,0,47),(146,'VTV3','2015-01-01','2018-12-31','24','27','5','Tương tự',1,'R&S','',1,0,47),(147,'VTV6','2015-01-01','2018-12-31','24','6','1','Tương tự',1,'Thomson','',1,0,47),(148,'VTV1','2015-01-01','2018-12-31','24','8','1','Tương tự',1,'thcst','',1,0,48),(149,'VTV1','2015-01-01','2018-12-31','24','9','5','Tương tự',1,'Btesa','',1,0,49),(150,'VTV2','2015-01-01','2018-12-31','24','25','10','Tương tự',1,'Btesa','',1,0,49),(151,'VTV3','2015-01-01','2018-12-31','24','11','5','Tương tự',1,'Thalse','',1,0,49),(152,'VTV1','2015-01-01','2018-12-31','24','8','2','Tương tự',1,'thcst','',1,0,50),(153,'VTV2','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'Btesa','',1,0,50),(154,'VTV3','2015-01-01','2018-12-31','24','12','0.5','Tương tự',1,'Inteco','',1,0,50),(155,'VTV1','2015-01-01','2018-12-31','24','22','2','Tương tự',1,'thcst','',1,0,51),(156,'VTV1','2015-01-01','2018-12-31','24','24','5','Tương tự',1,'Btesa','',1,0,52),(157,'VTV2','2015-01-01','2018-12-31','24','53','10','Tương tự',1,'R&S','',1,0,52),(158,'VTV3','2015-01-01','2018-12-31','24','41','10','Tương tự',1,'R&S','',1,0,52),(159,'VTV_So','2015-01-01','2018-12-31','24','21','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',1,0,52),(160,'VTV1','2015-01-01','2018-12-31','24','37','5','Tương tự',1,'Btesa','',1,0,53),(161,'VTV2','2015-01-01','2018-12-31','24','40','5','Tương tự',1,'R&S','',1,0,53),(162,'VTV3','2015-01-01','2018-12-31','24','52','5','Tương tự',1,'R&S','',1,0,53),(163,'VTV_So','2015-01-01','2018-12-31','24','27','2','Số',1,'R&S','VTV1;VTV2;VTV3;VTV6',1,0,53),(164,'VTV2','2015-01-01','2018-12-31','24','50','5','Tương tự',2,'Harris','',1,0,54),(165,'VTV1','2015-01-01','2018-12-31','24','47','5','Tương tự',1,'Btesa','',1,0,55),(166,'VTV1','2015-01-01','2018-12-31','24','23','10','Tương tự',1,'Btesa','',1,0,56),(167,'VTV3','2015-01-01','2018-12-31','24','28','10','Tương tự',1,'NEC','',1,0,56),(168,'VTV1','2015-01-01','2018-12-31','24','27','5','Tương tự',1,'Btesa','',1,0,57),(169,'VTV2','2015-01-01','2018-12-31','24','47','5','Tương tự',1,'R&S','',1,0,57),(170,'VTV3','2015-01-01','2018-12-31','24','21','5','Tương tự',1,'R&S','',1,0,57),(171,'VTV1','2015-01-01','2018-12-31','24','39','10','Tương tự',1,'Btesa','',1,0,58),(172,'VTV3','2015-01-01','2018-12-31','24','42','5','Tương tự',1,'Harris','',1,0,58);
/*!40000 ALTER TABLE `broadcasts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contracts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contract_number` varchar(20) NOT NULL,
  `sign_date` date NOT NULL,
  `contract_type` varchar(10) NOT NULL,
  `tax` decimal(5,2) NOT NULL,
  `cancel_date` date DEFAULT NULL,
  `broadcast_id` int(11) NOT NULL,
  `unit_price_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `broadcast_id` (`broadcast_id`),
  KEY `contracts_unit_price_id_8dfe8db6_fk_unit_prices_id` (`unit_price_id`),
  CONSTRAINT `contracts_broadcast_id_a1e27581_fk_broadcasts_id` FOREIGN KEY (`broadcast_id`) REFERENCES `broadcasts` (`id`),
  CONSTRAINT `contracts_unit_price_id_8dfe8db6_fk_unit_prices_id` FOREIGN KEY (`unit_price_id`) REFERENCES `unit_prices` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contracts`
--

LOCK TABLES `contracts` WRITE;
/*!40000 ALTER TABLE `contracts` DISABLE KEYS */;
INSERT INTO `contracts` VALUES (1,'39/2015/HĐKT/VTV1','2015-01-01','Tiếp Phát',5.00,NULL,43,39),(2,'33/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,44,41),(3,'44/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',5.00,NULL,45,42),(4,'04/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,46,9),(5,'05/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,47,11),(6,'46/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,48,12),(7,'18/2015/HĐKT/VTV6','2015-01-01','Khai Thác',5.00,NULL,49,11),(8,'01/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,50,9),(9,'22/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,51,42),(10,'03/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,52,12),(11,'03/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,53,8),(12,'38/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,54,12),(13,'49/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,55,12),(14,'01/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',10.00,NULL,56,48),(15,'40/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,57,24),(16,'39/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,58,21),(17,'50/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,59,24),(18,'46/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,60,11),(19,'59/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,61,8),(20,'44/2015/HĐKT/VTV1','2015-01-01','Tiếp Phát',5.00,NULL,62,48),(21,'28/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,63,47),(22,'60/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,64,8),(23,'18/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,65,9),(24,'32/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,66,48),(25,'39/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',5.00,NULL,67,48),(26,'42/2015/HĐKT/VTV1','2015-01-01','Tiếp Phát',5.00,NULL,68,48),(27,'35/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,69,9),(28,'30/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,70,11),(29,'09/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',5.00,NULL,71,48),(30,'02/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,72,9),(31,'50/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,73,11),(32,'24/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,74,12),(33,'19/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',5.00,NULL,75,48),(34,'38/2015/HĐKT/VTV1','2015-01-01','Tiếp Phát',10.00,NULL,76,45),(35,'30/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,77,11),(36,'42/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,78,11),(37,'03/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',10.00,NULL,79,48),(38,'06/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,80,8),(39,'07/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,81,7),(40,'19/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,82,10),(41,'02/2015/HĐKT/VTV_So','2015-02-01','Khai Thác',10.00,NULL,83,12),(42,'23/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,84,35),(43,'24/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,85,34),(44,'34/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,86,34),(45,'21/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,87,8),(46,'34/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',10.00,NULL,88,47),(47,'43/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,89,11),(48,'54/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,90,8),(49,'14/2015/HĐKT/VTV6','2015-01-01','Khai Thác',5.00,NULL,91,10),(50,'20/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,92,48),(51,'08/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',5.00,NULL,93,8),(52,'43/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,94,8),(53,'54/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,95,47),(54,'21/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,96,11),(55,'17/2015/HĐKT/VTV6','2015-01-01','Khai Thác',5.00,NULL,97,10),(56,'40/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',5.00,NULL,98,48),(57,'09/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,99,8),(58,'05/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,100,10),(59,'13/2015/HĐKT/VTV6','2015-01-01','Khai Thác',10.00,NULL,101,10),(60,'55/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',10.00,NULL,102,48),(61,'05/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',10.00,NULL,103,48),(62,'10/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,104,8),(63,'48/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,105,11),(64,'05/2015/HĐKT/VTV_So','2015-02-01','Khai Thác',5.00,NULL,106,12),(65,'11/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,107,8),(66,'51/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,108,48),(67,'67/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,109,11),(68,'14/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,110,8),(69,'52/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,111,48),(70,'61/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,112,11),(71,'22/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,113,7),(72,'45/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',10.00,NULL,114,48),(73,'62/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,115,11),(74,'19/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,116,8),(75,'04/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',10.00,NULL,117,48),(76,'63/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,118,11),(77,'12/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,119,8),(78,'36/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',10.00,NULL,120,47),(79,'64/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,121,11),(80,'22/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',10.00,NULL,122,48),(81,'24/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,123,9),(82,'49/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,124,11),(83,'23/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,125,12),(84,'06/2015/HĐKT/VTV_So','2015-02-01','Khai Thác',5.00,NULL,126,12),(85,'25/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,127,9),(86,'37/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,128,10),(87,'48/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,129,10),(88,'33/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,130,9),(89,'47/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,131,11),(90,'65/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,132,11),(91,'29/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,133,9),(92,'14/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,134,11),(93,'38/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,135,11),(94,'34/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,136,20),(95,'41/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,137,60),(96,'37/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,138,22),(97,'28/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,139,20),(98,'26/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,140,22),(99,'36/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,141,22),(100,'20/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',5.00,NULL,142,42),(101,'06/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',5.00,NULL,143,42),(102,'41/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,144,11),(103,'40/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,145,11),(104,'51/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,146,11),(105,'15/2015/HĐKT/VTV6','2015-01-01','Tiếp Phát',10.00,NULL,147,45),(106,'15/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,148,9),(107,'31/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,149,35),(108,'21/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,150,34),(109,'31/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,151,35),(110,'16/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,152,21),(111,'27/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,153,22),(112,'58/2015/HĐKT/VTV3','2015-01-01','Tiếp Phát',10.00,NULL,154,60),(113,'17/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,155,21),(114,'30/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,156,20),(115,'42/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,157,22),(116,'53/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,158,22),(117,'04/2015/HĐKT/VTV_So','2015-02-01','Khai Thác',10.00,NULL,159,12),(118,'26/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,160,8),(119,'25/2015/HĐKT/VTV2','2015-01-01','Khai Thác',10.00,NULL,161,11),(120,'35/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,162,11),(121,'01/2015/HĐKT/VTV_So','2015-02-01','Khai Thác',10.00,NULL,163,12),(122,'18/2015/HĐKT/VTV2','2015-01-01','Tiếp Phát',10.00,NULL,164,38),(123,'36/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,165,32),(124,'35/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,166,10),(125,'18/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,167,10),(126,'27/2015/HĐKT/VTV1','2015-01-01','Khai Thác',5.00,NULL,168,8),(127,'31/2015/HĐKT/VTV2','2015-01-01','Khai Thác',5.00,NULL,169,11),(128,'43/2015/HĐKT/VTV3','2015-01-01','Khai Thác',5.00,NULL,170,11),(129,'37/2015/HĐKT/VTV1','2015-01-01','Khai Thác',10.00,NULL,171,7),(130,'66/2015/HĐKT/VTV3','2015-01-01','Khai Thác',10.00,NULL,172,11);
/*!40000 ALTER TABLE `contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'areas','area'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'basestations','basestation'),(9,'broadcastingstatus','broadcastingstatus'),(10,'broadcasts','broadcast'),(5,'contenttypes','contenttype'),(11,'contracts','contract'),(12,'machinelocations','machinelocation'),(6,'sessions','session'),(13,'televisions','television'),(14,'timeranges','timerange'),(15,'unitprices','unitprice');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine_locations`
--

DROP TABLE IF EXISTS `machine_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `machine_locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `owner` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine_locations`
--

LOCK TABLES `machine_locations` WRITE;
/*!40000 ALTER TABLE `machine_locations` DISABLE KEYS */;
INSERT INTO `machine_locations` VALUES (1,'Địa điểm đặt máy cùng với Đài địa phương','Đài Truyền hình Quốc gia'),(2,'Địa điểm đặt máy đặc biệt khó khăn','Đài Truyền hình Quốc gia'),(3,'Cụm máy phát độc lập của Đài Truyền hình Quốc gia','Đài Truyền hình Quốc gia'),(4,'Địa điểm đặt máy bình thường','Đài Truyền hình Địa phương'),(5,'Địa điểm đặt máy đặc biệt khó khăn','Đài Truyền hình Địa phương');
/*!40000 ALTER TABLE `machine_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `televisions`
--

DROP TABLE IF EXISTS `televisions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `televisions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `province` varchar(50) NOT NULL,
  `representative` varchar(50) NOT NULL,
  `position` varchar(20) NOT NULL,
  `address` longtext NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  `tax_code` varchar(15) DEFAULT NULL,
  `bank_account` varchar(20) NOT NULL,
  `bank` varchar(100) NOT NULL,
  `decision_number` varchar(20) DEFAULT NULL,
  `decision_date` date DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `televisions`
--

LOCK TABLES `televisions` WRITE;
/*!40000 ALTER TABLE `televisions` DISABLE KEYS */;
INSERT INTO `televisions` VALUES (1,'TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam','Hà Nội','TRẦN QUỐC TUẤN','P. Giám đốc','Số 9, Nguyên Hồng, Ba Đình Hà Nội','(04) 3 8317 440','(04) 3 771 6244','101567589','102010001355996','Ngân hàng TMCP Công thương Việt Nam - Chi nhánh Thành phố Hà Nội','2048/QĐ-THVN','2014-11-19',''),(2,'ĐÀI PTTH HÀ GIANG','Hà Giang','TÔ TUYÊN','Giám đốc','Tổ 7 Phường Trần Phú – Thành phố Hà Giang, tỉnh Hà Giang','(0219) 3864 732','(0219) 3860 043','5100102068','34510000000410','Ngân hàng đầu tư và phát triển tỉnh Hà Giang','12/QĐ-UBND','2012-01-04',''),(3,'ĐÀI PTTH TỈNH LÀO CAI','Lào Cai','PHAN QUANG HƯNG','Giám đốc','Đường 30/4 Phường Nam Cường – Thành phố Lào Cai, tỉnh Lào Cai','(020) 3 840093','(020) 3 3825304','5300140085','37510000000154','Ngân hàng Đầu tư & Phát triển tỉnh Lào Cai','2684/QĐ-UBND','2009-08-31',''),(4,'ĐÀI PTTH TỈNH CAO BẰNG','Cao Bằng','LA VŨ QUANG','Giám đốc','87 Phố Bế Văn Đàn, Hợp giang, thị xã Cao Bằng','(026) 3852 250','(026) 3854 022','','102010001447581','Ngân hàng TMCP Công thương Việt Nam chi nhánh Cao Bằng','302/QĐUB','1993-11-16',''),(5,'ĐÀI PTTH ĐIỆN BIÊN','Điện Biên','NGUYỄN NGỌC KỶ','Giám đốc','Đường võ nguyên giáp Phường Mường Thanh, thành phố Điện Biên, tỉnh Điện Biên','(0230) 3824 836','(0230) 3824 035','5600128272','8900211000025','Ngân hàng Agribank chi nhánh tỉnh Điện Biên','70/QĐ UBND','1977-04-18',''),(6,'ĐÀI PTTH LAI CHÂU','Lai Châu','NGUYỄN NGỌC KỶ','Giám đốc','Phường Đoàn Kết, Thị xã Lai Châu, Tỉnh Lai Châu','(0231) 3 876 979','(0231) 3 876 97','6200000304','37130104157600000','Kho bạc Nhà nước tỉnh Lai Châu','47/2004/QĐUB','2004-02-25',''),(7,'ĐÀI PTTH TUYÊN QUANG','Tuyên Quang','MA XUÂN QUANG','Giám đốc','Số 219 Đường Tân Trào, Thành phố Tuyên Quang','027 3 822 435','0273 824 435','5000146449','371221013623','Kho bạc Nhà nước tỉnh Tuyên Quang','423/QĐ-UBND','2009-10-26',''),(8,'ĐÀI PTTH YÊN BÁI','Yên Bái','HÀ MINH ẤT','Giám đốc','Số 1, Trần Quốc Toản, phường Đồng Tâm, Thành phố Yên Bái','(029) 3 855 792','(029) 3853 491','','102010000672377','Ngân hàng TMCP Công thương VN - chi nhánh Yên Bái','632/QĐ-UBND','2011-05-09',''),(9,'ĐÀI PTTH SƠN LA','Sơn La','LÃ MINH TUẤN','Giám đốc','Tổ 1, phường Quyết Thắng Thành phố Sơn La','(022)3 853 912','(022)3 853 559','5500155032','371221018340','Kho bạc Nhà nước tỉnh Sơn La','645/QĐ-TC','1977-09-26',''),(10,'ĐÀI PTTH BẮC KẠN','Bắc Kạn','MA ĐÌNH VIỆT','Giám đốc','Phường Phùng Chí Kiên, thị xã Bắc Kạn tỉnh Bắc Kạn','(0281) 3879 753','(0281) 3871 183','4700113422','102010001534102','Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Bắc Kạn','909/2011','2011-06-01',''),(11,'ĐÀI PTTH LẠNG SƠN','Lạng Sơn','NÔNG LƯƠNG CHẤN','Giám đốc','Số 9 đường Hoàng Văn Thụ, Phường Chi Lăng, Thành phố Lạng Sơn','(025)3 813 531','(025)3 812 749','','37121106230800000','Kho bạc Nhà nước tỉnh Lạng Sơn','217/QĐUB','1991-03-18',''),(12,'ĐÀI PTTH HÒA BÌNH','Hoà Bình','TÔ DUY NHẤT','Giám đốc','Đường Trần Hưng Đạo - Thành  phố Hòa Bình, tỉnh Hòa Bình','(0218) 3 894056','(0218) 3 852743','5400103506','45510000317006','Ngân hàng TMCP Đầu tư & phát triển - chi nhánh Hòa Bình','40575','2011-03-21',''),(13,'ĐÀI PTTH THÀNH PHỐ HẢI PHÒNG','Thành phố Hải Phòng','ĐOÀN VĂN CHƯƠNG','Giám đốc','199 Tô Hiệu, quận Lê Chân, thành phố Hải Phòng','(031)3 610 599','(031)3 846 838','','102010001013100','Ngân hàng TMCP Công thương Việt Nam - Chi nhánh Tô Hiệu, Hải Phòng',NULL,NULL,''),(14,'ĐÀI PTTH QUẢNG NINH','Quảng Ninh','','Giám đốc','Phường Hồng Hải - Thành phố Hạ Long','(033) 3 825 363','(033) 3 827 507','','37131044593','Kho bạc Nhà nước tỉnh Quảng Ninh',NULL,NULL,''),(15,'ĐÀI PTTH THÁI BÌNH','Thái Bình','VŨ ANH THAO','Giám đốc','Phường Hoàng Diệu, Thành phố Thái Bình, tỉnh Thái Bình','(036) 3 745416','(036)3 748 263','1000215536','102010000358312','Ngân hàng TMCP Công Thương Việt Nam chi nhánh Thái Bình','72/2004/QĐ-UBND','2004-07-22',''),(16,'ĐÀI PTTH NAM ĐỊNH','Nam Định','TRỊNH XUÂN LỘC','Giám đốc','255 đường Hàn Thuyên, Thành phố Nam Định, tỉnh Nam Định','(0350) 3643 485','(0350) 3643 077','','37130109458700000','Kho bạc Nhà nước tỉnh Nam Định',NULL,NULL,''),(17,'ĐÀI PTTH HÀ NAM','Hà Nam','TRỊNH NGÂN LIÊN','Giám đốc','Phường Hai Bà Trưng, Thị xã Phủ Lý, tỉnh Hà Nam','(0351) 3851 780','(0351) 3854 460','','37121066908','Kho bạc Nhà nước tỉnh Hà Nam',NULL,NULL,''),(18,'ĐÀI PTTH NINH BÌNH','Ninh Bình','HOÀNG TUẤN DŨNG','Giám đốc','Phố 10, phường Đông Thành, thị xã Ninh Bình','(030) 3 889 357','(030) 3 875 513','2700139353','371321004241','Kho bạc Nhà nước tỉnh Ninh Bình','2798/QĐ - UBND','2007-12-10',''),(19,'ĐÀI PTTH THANH HOÁ','Thanh Hoá','LÊ HOÀI CHÂU','Giám đốc','Số 8 đường Hạc Thành, thành phố Thanh Hoá','(037) 3856 293','(037) 3857 159','2800230447','3500431101001500','Ngân hàng NN & PTNT tỉnh Thanh Hoá','3188/2002','2012-08-23',''),(20,'ĐÀI PTTH NGHỆ AN','Nghệ An','NGUYỄN NHƯ KHÔI','Giám đốc','Số 1 Nguyễn Thị Minh Khai, Thành phố Vinh','(038) 3 598457','(038) 3 844700','2900325815','102010000485306','Ngân hàng công thương Bến Thủy','61/2012/QĐ-UB.TC','2012-08-23',''),(21,'ĐÀI PTTH HÀ TĨNH','Hà Tĩnh','ĐINH VĂN THIỀM','Giám đốc','Số 22 Phan Đình Phùng, Thành phố Hà Tĩnh','(039) 3 855 540','(039) 3 857 410','','201000586888','Ngân hàng TMCP Ngoại thương Hà Tĩnh','999/2002/QĐ-UB-TC','2002-05-09',''),(22,'ĐÀI PTTH QUẢNG BÌNH','Quảng Bình','LÊ KHÁNH HÒA','Giám đốc','54 Quang Trung, Thành phố Đồng Hới, tỉnh Quảng Bình','(052) 3 822 522','(052) 3 822 102','','37130102058900','Kho bạc Nhà nước Quảng Bình','167/QĐUB','1993-03-08',''),(23,'ĐÀI PTTH QUẢNG TRỊ','Quảng Trị','TRẦN ĐỨC HỮU','Giám đốc','Phường 1, thành phố Đông Hà, tỉnh Quảng Trị','(053)3 850 509','(053) 3850 516','','102010000508087','Ngân hàng Công thương Quảng Trị','07/QĐUB','2011-04-14',''),(24,'ĐÀI PTTH QUẢNG NAM','Quảng Nam','MAI VĂN TƯ','Giám đốc','58 Hùng Vương Tam Kỳ tỉnh Quảng Nam','(0510) 384 5340','(0510) 3852 401','','651000623899','Ngân hàng VCB Quảng Nam','04/2011/QĐUB','2004-02-09',''),(25,'ĐÀI PTTH QUẢNG NGÃI','Quảng Ngãi','TRƯƠNG QUANG TẤN','Phó Giám đốc','Số 165 đại lộ Hùng Vương, thành phố Quảng Ngãi','(055) 3 822 051','(055) 3 825 420','','371321082709','Kho bạc Nhà nước tỉnh Quảng Ngãi','113/2002/QĐUB','2002-10-01',''),(26,'ĐÀI PTTH BÌNH ĐỊNH','Bình Định','PHẠM VĨNH THÁI','Giám đốc','23 Mai Xuân Thưởng Quy Nhơn tỉnh Bình Định','(056) 3822 878','(056) 3824 718','4100259331','51000323365','Ngân hàng Ngoại thương Quy Nhơn','738/QĐ-UBND','2008-12-26',''),(27,'ĐÀI PTTH KHÁNH HOÀ','Khánh Hoà','TRƯƠNG TẤN MINH','Giám đốc','Số 70 Trần Phú, Thành phố Nha Trang, tỉnh Khánh Hoà','(058) 3 525 959','(058) 3523 158','','37121021454','Kho bạc Nhà nước tỉnh Khánh Hoà','2575/QĐUB','1994-11-22',''),(28,'ĐÀI PTTH NINH THUẬN','Ninh Thuận','NGUYỄN MINH HÀ','Giám đốc','285A đường 21/8, Phước Mỹ, Thị xã Phan Rang, Ninh Thuận','(068) 823 759','(068) 831 177','','61510000004474','Ngân hàng TMCP Đầu tư và phát triển Việt Nam – Chi nhánh tỉnh Ninh Thuận','186/2004/QĐ-UB','2004-11-15',''),(29,'ĐÀI PTTH BÌNH THUẬN','Bình Thuận','LÊ VĂN BẢY','Giám đốc','339/ 341 Thủ khoa Huân- T.p Phan Thiết - tỉnh Bình Thuận','(062) 3 833 409','(062) 3 835 781','3400189122','371301020103','Kho bạc Nhà nước tỉnh Bình Thuận','3455/QĐUB','2006-12-28',''),(30,'ĐÀI PTTH KON TUM','Kon Tum','PHAN CƯ','Giám đốc','Số 258A Phan Đình Phùng, Thành phố Kon Tum, tỉnh Kon Tum','(060) 3 866261','(060) 3 866261','6100108713','371301037641','Kho bạc Nhà nước tỉnh Kon Tum','30','1991-11-30',''),(31,'ĐÀI PTTH GIA LAI','Gia Lai','ĐỖ NGỌC KỲ','Giám đốc','Số 1 Đường Lý Thái Tổ - Thành phố Pleiku tỉnh Gia Lai','(059) 3 824222','(059) 3 716659','59001809891','291000252292','Ngân hàng Ngoại thương Gia Lai','27/2009/QĐ-UB','2009-08-21',''),(32,'ĐÀI PTTH ĐẮK LẮK','Đắk Lắk','TÔ THANH BÌNH','Giám đốc','Số 01 Nguyễn Tất Thành, thành phố Buôn Mê Thuột','(050) 3852 544','(050) 3810 375','','5214201000860','Ngân hàng Nông nghiệp và phát triển nông thôn tỉnh tỉnh Đắk Lắk – chi nhánh Phan Chu Trinh','241/QĐUB','2009-02-06',''),(33,'ĐÀI PTTH ĐẮK NÔNG','Đắc Nông','HÀ TRUNG KÝ','Giám đốc','Thị xã Gia Nghĩa, tỉnh Đắc Nông','(050) 3543 866','(050) 3543 866','','102010001399736','Ngân hàng TMCP Công thương Việt Nam – Chi nhánh Đắc Nông','1987/QĐ-UBND','2010-12-08',''),(34,'ĐÀI PTTH LÂM ĐỒNG','Lâm Đồng','NGUYỄN THANH NHÂN','Giám đốc','Số 10 Trần Hưng Đạo, Thành phố Đà Lạt','(063) 3 820 875','(063) 3 829 510','5800075927','5400211000760','Ngân hàng Nông nghiệp và phát triển nông thôn tỉnh Lâm Đồng','32/2011/QĐ UBND','2011-06-23',''),(35,'ĐÀI PTTH BÌNH PHƯỚC','Bình Phước','PHAN MINH HOÀNG','Giám đốc','Số 1, Đường Trần Hưng Đạo, phường Tân Phú, thị xã Đồng Xoài, tỉnh Bình Phước','(0651) 388 7062','(0651) 387 0720','3800101316','65510000008520','Ngân hàng Đầu tư và phát triển Bình Phước','113/2005/QĐ-UBND','2005-09-29',''),(36,'ĐÀI PTTH TÂY NINH','Tây Ninh','NGUYỄN NAM GIANG','Giám đốc','Số 322, đường 30/4, Phường 3 Thành phố Tây Ninh','(066) 3828 781','(066) 3820 970','','934020000130','Kho bạc Nhà nước tỉnh Tây Ninh','20','2011-06-29',''),(37,'ĐÀI TRUYỀN HÌNH THÀNH PHỐ HỒ CHÍ MINH','Thành phố Hồ Chí Minh','NGUYỄN QUÝ HÒA','Tổng Giám đốc','Số 14 Phố Đinh Tiên Hoàng, quận 1, Thành phố Hồ Chí Minh','(08) 39102 354','(08) 39102 354','','945020025003','Kho bạc Nhà nước Thành phố Hồ chí Minh','15/2007/QĐ-UBND','2007-02-02',''),(38,'ĐÀI PTTH AN GIANG','An Giang','CAO QUANG LIÊM','Giám đốc','45/1 Trần Hưng Đạo, Phường Bình Khánh Thành phố Long Xuyên','(076) 3 852342','(076) 3 956100','16003539471','70110000052675','Ngân hàng Đầu tư và Phát triển Việt Nam - Chi nhánh An Giang','43/2009/QĐ-UBND','2009-09-25',''),(39,'ĐÀI PTTH BẾN TRE','Bến Tre','TRẦN VĂN HỮU','Giám đốc','1/3 Trần Quốc Tuấn, phường 4, Thành phố Bến Tre','(075) 3822 248 (106)','(075) 3825 787','1300109296','72110000094770','Ngân hàng đầu tư và phát triển Bến Tre','4131/2007/QĐ-UBND','2005-11-28',''),(40,'ĐÀI PTTH SÓC TRĂNG','Sóc Trăng','LÂM THỊ LỆ PHƯƠNG','Giám đốc','Đường 132 Trần Văn Bảy, phường 3, Thành phố Sóc Trăng','(079) 3826 765','(079) 3825 876','','371221042820','Kho bạc Nhà nước Sóc Trăng',NULL,NULL,''),(41,'ĐÀI PTTH KIÊN GIANG','Kiên Giang','NGUYỄN THANH CAO','Giám đốc','Số 39 Đống Đa Vĩnh Lạc Thành phố Rạch Giá tỉnh Kiên Giang','(077) 3927 066','(077) 3813 990','','1003546997','Ngân hàng SHB Kiên Giang',NULL,NULL,''),(42,'ĐÀI PTTH BẠC LIÊU','Bạc Liêu','LÊ HỮU BUÔL','Giám đốc','410 Đường 23/8 Phường 8, Thành phố Bạc Liêu','(0781) 3825 397','(0781) 3823 989','1900137231','102010001557655','Ngân hàng TMCP Công thương tỉnh Bạc Liêu','25/QĐUB','2010-12-31',''),(43,'ĐÀI PTTH CÀ MAU','Cà Mau','ĐỖ KIẾN QUỐC','Giám đốc','413 Nguyễn Trãi, Phường 9, Thành phố Cà Mau','(0780) 3831 664','(0780) 3833 621','','102010000327479','Ngân hàng công thương tỉnh Cà Mau','58/QĐUB','1997-01-01','');
/*!40000 ALTER TABLE `televisions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `time_ranges`
--

DROP TABLE IF EXISTS `time_ranges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `time_ranges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `broadcasting_status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `time_ranges_broadcasting_status__75ec943d_fk_broadcast` (`broadcasting_status_id`),
  CONSTRAINT `time_ranges_broadcasting_status__75ec943d_fk_broadcast` FOREIGN KEY (`broadcasting_status_id`) REFERENCES `broadcasting_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time_ranges`
--

LOCK TABLES `time_ranges` WRITE;
/*!40000 ALTER TABLE `time_ranges` DISABLE KEYS */;
/*!40000 ALTER TABLE `time_ranges` ENABLE KEYS */;
UNLOCK TABLES;

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

-- Dump completed on 2017-09-21  8:39:02
