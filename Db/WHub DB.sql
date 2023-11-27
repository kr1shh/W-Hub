/*
SQLyog Community v13.1.9 (64 bit)
MySQL - 8.0.34 : Database - whub
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`whub` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `whub`;

/*Table structure for table `groups` */

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `uid` int DEFAULT NULL,
  `groupname` varchar(100) DEFAULT NULL,
  `groupdes` varchar(300) DEFAULT NULL,
  `grouplink` varchar(300) DEFAULT NULL,
  `groupdp` varchar(200) DEFAULT NULL,
  `gid` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`gid`),
  KEY `uid` (`uid`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `login` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `groups` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `login` */

/*Table structure for table `signup` */

DROP TABLE IF EXISTS `signup`;

CREATE TABLE `signup` (
  `uid` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  CONSTRAINT `signup_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `login` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `signup` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
