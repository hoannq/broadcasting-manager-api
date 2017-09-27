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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-21  8:39:48
