-- MySQL dump 10.14  Distrib 5.5.33a-MariaDB, for Linux (i686)
--
-- Host: localhost    Database: mycloud
-- ------------------------------------------------------
-- Server version	5.5.33a-MariaDB

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
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `user_id` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('admin','admin'),('karthik','1234'),('kathir','kathir'),('mani','9978'),('mani44','kandan'),('test','test123');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usrdata`
--

DROP TABLE IF EXISTS `usrdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usrdata` (
  `user_id` varchar(20) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `file_obj` varchar(50) DEFAULT NULL,
  `fsplit_1` varchar(150) DEFAULT NULL,
  `fsplit_2` varchar(150) DEFAULT NULL,
  `e_key` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usrdata`
--

LOCK TABLES `usrdata` WRITE;
/*!40000 ALTER TABLE `usrdata` DISABLE KEYS */;
INSERT INTO `usrdata` VALUES ('mani','input2.txt','78d29caf1ec0L','784595c31b47ce173dcL/encr1input2.txt','94d5da2a0a5538ce7a2L/encr2input2.txt','6efd3757a795fa14'),('mani','input1.txt','16e87d732e871L','8083e0e9a8ec4edfe71L/encr1input1.txt','8b4bcf7cdf123456e80L/encr2input1.txt','4b055167e45898ac'),('mani','dbtest.py','694099a96da0L','1ef1c61fda551d18993L/encr1dbtest.py','963a3f7f1ae122f254cL/encr2dbtest.py','58eb5731ea60f89e'),('mani','input3.txt','1dab8dd6c5dbdL','2d55bbfeb206ea61e92L/encr1input3.txt','5e5745858f9f1ce039L/encr2input3.txt','93b3760f95a04d50');
/*!40000 ALTER TABLE `usrdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-01 23:41:56
