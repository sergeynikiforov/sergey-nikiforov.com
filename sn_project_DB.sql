-- MySQL dump 10.13  Distrib 5.6.27, for Linux (x86_64)
--
-- Host: localhost    Database: sn_project_db
-- ------------------------------------------------------
-- Server version	5.6.27

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Person',7,'add_person'),(20,'Can change Person',7,'change_person'),(21,'Can delete Person',7,'delete_person'),(22,'Can add Employer',8,'add_employer'),(23,'Can change Employer',8,'change_employer'),(24,'Can delete Employer',8,'delete_employer'),(25,'Can add Job',9,'add_job'),(26,'Can change Job',9,'change_job'),(27,'Can delete Job',9,'delete_job'),(28,'Can add Education',10,'add_education'),(29,'Can change Education',10,'change_education'),(30,'Can delete Education',10,'delete_education'),(31,'Can add Online Course',11,'add_onlinecourse'),(32,'Can change Online Course',11,'change_onlinecourse'),(33,'Can delete Online Course',11,'delete_onlinecourse'),(34,'Can add ContactMe message',12,'add_contactme'),(35,'Can change ContactMe message',12,'change_contactme'),(36,'Can delete ContactMe message',12,'delete_contactme'),(37,'Can add photoset',13,'add_photoset'),(38,'Can change photoset',13,'change_photoset'),(39,'Can delete photoset',13,'delete_photoset'),(40,'Can add photo',14,'add_photo'),(41,'Can change photo',14,'change_photo'),(42,'Can delete photo',14,'delete_photo'),(43,'Can add photo in photoset',15,'add_photoinphotoset'),(44,'Can change photo in photoset',15,'change_photoinphotoset'),(45,'Can delete photo in photoset',15,'delete_photoinphotoset');
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
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$7ERdA1MGe3WO$C8jdce4I8fJqY5IGtmVRaWN9noDFxP7jZ84toUAl7OQ=','2015-11-15 13:33:41.885578',1,'sergeynikiforov','','','serge.a.nikiforov@gmail.com',1,1,'2015-05-20 12:43:31.454170');
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
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-05-20 13:25:19.828151','1','SergeyNikiforov',1,'',7,1),(2,'2015-05-20 13:26:32.844427','1','SergeyNikiforov',2,'Changed address.',7,1),(3,'2015-05-20 13:39:05.176990','1','\'Manpower CIS\' LLC (Citibank outstaffing)',1,'',8,1),(4,'2015-05-20 13:43:03.447776','2','\'ATON\' LLC',1,'',8,1),(5,'2015-05-20 13:45:09.490531','3','Organizing Committee of the XXII Olympic Winter Games and XI Paralympic Winter Games of 2014 in Sochi',1,'',8,1),(6,'2015-05-20 13:47:52.399653','1','Direct Sales Specialist',1,'',9,1),(7,'2015-05-20 13:50:22.606609','2','Contact Center Specialist',1,'',9,1),(8,'2015-05-20 13:52:34.084565','3','Contact Center Senior Specialist',1,'',9,1),(9,'2015-05-20 13:55:23.412250','4','RateCard Manager',1,'',9,1),(10,'2015-05-20 14:06:24.600777','7','Master of Science at Peoples\' Friendship University of Russia, 2011',1,'',10,1),(11,'2015-05-20 14:07:23.746663','8','Bachelor of Science at Peoples\' Friendship University of Russia, 2009',1,'',10,1),(12,'2015-05-20 14:10:05.524837','1','LFS101x.2 Introduction to Linux',1,'',11,1),(13,'2015-05-20 14:10:50.864011','2','6.00.1x Introduction to Computer Science and Programming Using Python',1,'',11,1),(14,'2015-05-20 20:51:50.781313','4','RateCard Manager',2,'Changed description_json.',9,1),(15,'2015-05-20 20:52:05.771423','3','Contact Center Senior Specialist',2,'Changed description_json.',9,1),(16,'2015-05-20 20:52:20.241844','2','Contact Center Specialist',2,'Changed description_json.',9,1),(17,'2015-05-20 20:52:32.026137','1','Direct Sales Specialist',2,'Changed description_json.',9,1),(18,'2015-05-20 21:14:56.179784','2','Contact Center Specialist',2,'Changed description_json.',9,1),(19,'2015-05-22 11:44:24.282445','1','SergeyNikiforov',2,'Changed skills_json and hobbies_json.',7,1),(20,'2015-05-23 11:21:24.418844','1','test at 2015-05-23 11:20:40.594792+00:00',3,'',12,1),(21,'2015-05-23 11:24:10.014051','3','test at 2015-05-23 11:23:36.600067+00:00',3,'',12,1),(22,'2015-05-23 11:24:10.018582','2','test at 2015-05-23 11:22:34.251430+00:00',3,'',12,1),(23,'2015-05-23 11:29:33.035364','4','test at 2015-05-23 11:27:03.300517+00:00',3,'',12,1),(24,'2015-05-23 11:36:26.511626','6','test at 2015-05-23 11:36:02.249898+00:00',3,'',12,1),(25,'2015-05-23 11:36:26.517682','5','test at 2015-05-23 11:29:38.210551+00:00',3,'',12,1),(26,'2015-07-22 13:47:57.946817','1','Direct Sales Specialist',2,'Changed description.',9,1),(27,'2015-07-22 13:51:37.257804','1','\'Manpower CIS\' LLC (Citibank outstaffing)',2,'Changed description.',8,1),(28,'2015-07-22 13:52:00.726553','2','\'ATON\' LLC',2,'Changed description.',8,1),(29,'2015-07-22 13:52:29.886361','3','Organizing Committee of the XXII Olympic Winter Games and XI Paralympic Winter Games of 2014 in Sochi',2,'Changed description.',8,1),(30,'2015-08-28 13:06:40.377832','1','\"test\" photoset with 10 photos, viewed 0 time(s)',2,'Changed num_photos.',13,1),(31,'2015-08-28 17:16:43.433898','1','\"test\" photoset with 10 photos, viewed 0 time(s)',2,'Changed slug.',13,1),(32,'2015-09-02 11:40:14.547298','11','\"Untitled\" photo wesalhfeclf7deftdmpu, viewed 0 time(s)',3,'',14,1),(33,'2015-09-02 11:42:53.841039','12','\"Untitled\" photo lfcprtw8lxtnae6y8gpq, viewed 0 time(s)',3,'',14,1),(34,'2015-11-15 13:36:15.175782','1','\"test\" photoset with 10 photos, viewed 100 time(s)',2,'Changed description.',13,1);
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
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(12,'sn_app','contactme'),(10,'sn_app','education'),(8,'sn_app','employer'),(9,'sn_app','job'),(11,'sn_app','onlinecourse'),(7,'sn_app','person'),(14,'sn_app','photo'),(15,'sn_app','photoinphotoset'),(13,'sn_app','photoset');
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
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-05-18 23:13:17.465689'),(2,'auth','0001_initial','2015-05-18 23:13:18.229506'),(3,'admin','0001_initial','2015-05-18 23:13:18.402364'),(4,'contenttypes','0002_remove_content_type_name','2015-05-18 23:13:18.585406'),(5,'auth','0002_alter_permission_name_max_length','2015-05-18 23:13:18.668810'),(6,'auth','0003_alter_user_email_max_length','2015-05-18 23:13:18.748097'),(7,'auth','0004_alter_user_username_opts','2015-05-18 23:13:18.782355'),(8,'auth','0005_alter_user_last_login_null','2015-05-18 23:13:18.892670'),(9,'auth','0006_require_contenttypes_0002','2015-05-18 23:13:18.899460'),(10,'sessions','0001_initial','2015-05-18 23:13:18.976910'),(11,'sn_app','0001_initial','2015-05-20 11:33:14.188341'),(12,'sn_app','0002_auto_20150520_1556','2015-05-20 12:56:29.995631'),(13,'sn_app','0003_auto_20150520_1625','2015-05-20 13:26:02.753295'),(14,'sn_app','0004_auto_20150521_1420','2015-05-21 11:20:48.422737'),(15,'sn_app','0005_contactme','2015-05-22 10:21:19.325281'),(16,'sn_app','0006_auto_20150523_1419','2015-05-23 11:19:32.023495'),(17,'sn_app','0007_auto_20150524_2023','2015-05-24 17:23:32.545298'),(18,'sn_app','0008_job_description','2015-07-22 13:44:32.543579'),(19,'sn_app','0009_auto_20150722_1649','2015-07-22 13:50:04.676125'),(22,'sn_app','0010_auto_20150825_1639','2015-08-25 13:52:59.565461'),(23,'sn_app','0011_auto_20150827_2101','2015-08-27 18:01:51.671106'),(24,'sn_app','0012_photo_url','2015-08-28 12:23:56.633771'),(25,'sn_app','0013_photoset_slug','2015-08-28 17:13:06.999368'),(26,'sn_app','0014_auto_20150828_2047','2015-08-28 17:47:57.058822'),(27,'sn_app','0015_auto_20150902_1438','2015-09-02 11:39:03.791982');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3uo9nzlycqmb4wkkmac2ud890xjol6zn','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-11-29 13:33:41.891225'),('7ssd4avjwcqw2f2o5gxy83ste0jl1kpc','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-09-11 12:44:05.283247'),('92a15vv5hlwjtwwaizjcqkswa53f1ujf','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-09-11 17:11:18.646523'),('iqbaiq0unk6ywun3466cwh31dppmhaog','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-08-05 13:45:13.365893'),('pvkwdl208wbxfqhx48igf18xhdft5nvl','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-06-03 12:44:03.143225'),('zmyonb1nia9tw4ban853hnlpwessupb6','NTcyZGUwY2Q5NTk0NjMyMWE3YWY2ZDMwYjE4M2VhZWI5NWYyZjI1NDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc1ZDA4Yjg3NTQ1ZDI2Y2I5ZDM2ODMzZTk3NmE2ZjViZjJlMDY5MzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-09-16 11:39:18.260051');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_contactme`
--

DROP TABLE IF EXISTS `sn_app_contactme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_contactme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `time_sent` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_contactme`
--

LOCK TABLES `sn_app_contactme` WRITE;
/*!40000 ALTER TABLE `sn_app_contactme` DISABLE KEYS */;
INSERT INTO `sn_app_contactme` VALUES (7,'testt','test@test.comt','testm','2015-05-23 11:50:55.425384'),(8,'testt2','test@test.com','qwerty','2015-05-23 12:03:43.704336'),(9,'testt2','test@test.com','qwerty','2015-05-23 12:04:42.852784'),(10,'testt2','test@test.com','qwerty','2015-05-23 12:15:01.733589'),(11,'testt2','test@test.com','qwert','2015-05-23 12:51:59.258465'),(12,'testt2','test@test.com','qwert','2015-05-23 12:52:35.126619'),(13,'testt2','test@test.com','qwert','2015-05-23 12:52:56.454005'),(14,'asdf','test@test.com','qwerrty','2015-05-23 13:23:15.362823'),(15,'alan','acanthurus@yandex.ru','hello!','2015-05-23 13:26:27.752420'),(16,'test','test@test.com','пав','2015-05-23 14:31:38.236814'),(17,'test','test@test.com','Здравствуйте, Sergey!\r\n\r\nКомпания ТрейдФинанс ищет кандидата на вакансию \"Экономист-аналитик\".\r\nВаше резюме показалось нам очень интересным.\r\nПодробное описание вакансии Вы можете найти на сайте hh.ru\r\nЗайдите под своим логином и паролем, и на странице \"Отклики на вакансии\" Вы найдете ссылку на описание вакансии.\r\nЕсли наше предложение Вам интересно, перезвоните, пожалуйста, в рабочее время по телефону +7 (495) 5143360 (Шкарёва Виктория Викторовна).\r\n\r\nС уважением,\r\nШкарёва Виктория Викторовна\r\nВакансия: Экономист-аналитик  \r\nкомпании: ТрейдФинанс\r\n\r\nПосмотреть вакансию можно по этой ссылке: http://hh.ru/vacancy/13407791?utm_medium=email&utm_source=email&utm_campaign=company_interested&utm_content=2015_05_22\r\n\r\n--------------------\r\nPLEASE DO NOT REPLY THIS MESSAGE!\r\n','2015-05-23 14:32:37.734984'),(18,'sender','test@test.com','Здравствуйте, Sergey!\r\n\r\nКомпания ТрейдФинанс ищет кандидата на вакансию \"Экономист-аналитик\".\r\nВаше резюме показалось нам очень интересным.\r\nПодробное описание вакансии Вы можете найти на сайте hh.ru\r\nЗайдите под своим логином и паролем, и на странице \"Отклики на вакансии\" Вы найдете ссылку на описание вакансии.\r\nЕсли наше предложение Вам интересно, перезвоните, пожалуйста, в рабочее время по телефону +7 (495) 5143360 (Шкарёва Виктория Викторовна).\r\n\r\nС уважением,\r\nШкарёва Виктория Викторовна\r\nВакансия: Экономист-аналитик  \r\nкомпании: ТрейдФинанс\r\n\r\nПосмотреть вакансию можно по этой ссылке: http://hh.ru/vacancy/13407791?utm_medium=email&utm_source=email&utm_campaign=company_interested&utm_content=2015_05_22\r\n\r\n--------------------\r\nPLEASE DO NOT REPLY THIS MESSAGE!\r\n','2015-05-23 14:34:01.512114'),(19,'W','w@z.com','Tr','2015-10-12 20:52:43.616145'),(20,'name','mane@name.com','123test','2015-10-12 21:51:04.127409'),(21,'1','as@as.com','test1','2015-10-12 21:52:52.667142'),(22,'1','test@q1.ru','qwerty','2015-10-12 21:56:58.976241'),(23,'abc','abc@abc.abc','abc','2015-11-18 13:03:06.225045'),(24,'abc','abc@abc.abc','qweghf','2015-11-18 17:09:19.904565'),(25,'Цыкаете ','qwerty@afg.jff','Logged пробирки ','2015-11-18 17:17:16.742144'),(26,'abca','abc@abc.abc','lvmfl','2015-11-18 17:29:37.722886'),(27,'q','dwe@gfbf.wql','123','2015-11-18 17:35:43.428161'),(28,'1','abc@abc.abc','w','2015-11-18 17:36:42.440417'),(29,'123','q@q.qjl','rwfnwk','2015-11-18 17:40:09.258425'),(30,'Йцкн','wer@ifsd.ty','Sfhxfbc','2015-11-18 17:42:16.259212'),(31,'UHF','fhcc@yrd.cfg','Chg','2015-11-18 17:43:46.210078'),(32,'kdnjkn','dsv@lfmdl.kjj','123','2015-11-18 17:44:35.997566'),(33,'124','12@jgj.com','123','2015-11-18 17:46:21.916148'),(34,'89','hm@gj.com','djf','2015-11-18 17:48:48.039108'),(35,'085','fdsjn@dgf.fg','odfom','2015-11-18 17:49:32.590687'),(36,'Tyfd','dfg@cfg.cgj','Ffgg','2015-11-18 17:54:07.625938');
/*!40000 ALTER TABLE `sn_app_contactme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_education`
--

DROP TABLE IF EXISTS `sn_app_education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_education` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `location` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `website` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `degree` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `major` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sn_app_education_a8452ca7` (`person_id`),
  CONSTRAINT `sn_app_education_person_id_74b8800005bdb867_fk_sn_app_person_id` FOREIGN KEY (`person_id`) REFERENCES `sn_app_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_education`
--

LOCK TABLES `sn_app_education` WRITE;
/*!40000 ALTER TABLE `sn_app_education` DISABLE KEYS */;
INSERT INTO `sn_app_education` VALUES (7,'Peoples\' Friendship University of Russia','Moscow, Russia','http://www.rudn.ru','Master of Science','Applied Math','2009-09-01','2011-06-01',1),(8,'Peoples\' Friendship University of Russia','Moscow, Russia','http://www.rudn.ru','Bachelor of Science','Computer Science','2004-09-01','2009-06-01',1);
/*!40000 ALTER TABLE `sn_app_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_employer`
--

DROP TABLE IF EXISTS `sn_app_employer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_employer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `location` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `website` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `number_of_employees` int(11) NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_employer`
--

LOCK TABLES `sn_app_employer` WRITE;
/*!40000 ALTER TABLE `sn_app_employer` DISABLE KEYS */;
INSERT INTO `sn_app_employer` VALUES (1,'\'Manpower CIS\' LLC (Citibank outstaffing)','Moscow, Russia','https://www.citibank.ru',5000,'Manpower provided outstaffing services for Citibank’s army of direct sales agents back then. Hardcore\r\nsales of credit cards was a routine job. These were fantastic several months: tough and stressed but\r\nrewarding.'),(2,'\'ATON\' LLC','Moscow, Russia','https://www.aton.ru/',500,'ATON is Russia’s oldest independent investment group. I was engaged in opening of its contact center -\r\nfirst as a specialist that deals with day-to-day customer inquiries about brokerage accounts and mutual\r\nfunds and then as a mentor and a department’s deputy manager to set things going flawlessly.'),(3,'Organizing Committee of the XXII Olympic Winter Games and XI Paralympic Winter Games of 2014 in Sochi','Sochi, Russia','http://www.sochi2014.com',10000,'The 2014 Olympics and Paralympics were the first Winter Games ever hosted in Russia. Actions took\r\nplace everywhere: from the Black Sea coast to the Krasnaya Polyana mountains. That was a joyful\r\nexperience - working in a multicultural, multilingual and fast-paced environment. I was a member of\r\nthe Rate Card team at the Main Press Center and my job was to help journalists from the leading press\r\nagencies to have their work done by ensuring that their technology and infrastructure needs are\r\nfullfilled.');
/*!40000 ALTER TABLE `sn_app_employer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_job`
--

DROP TABLE IF EXISTS `sn_app_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `achievements_json` longtext COLLATE utf8_unicode_ci,
  `employer_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sn_app_job_employer_id_1f7f8db141789e68_fk_sn_app_employer_id` (`employer_id`),
  KEY `sn_app_job_a8452ca7` (`person_id`),
  CONSTRAINT `sn_app_job_employer_id_1f7f8db141789e68_fk_sn_app_employer_id` FOREIGN KEY (`employer_id`) REFERENCES `sn_app_employer` (`id`),
  CONSTRAINT `sn_app_job_person_id_4479bbd84f9ae052_fk_sn_app_person_id` FOREIGN KEY (`person_id`) REFERENCES `sn_app_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_job`
--

LOCK TABLES `sn_app_job` WRITE;
/*!40000 ALTER TABLE `sn_app_job` DISABLE KEYS */;
INSERT INTO `sn_app_job` VALUES (1,'Direct Sales Specialist','2007-07-01','2007-11-30','[\"sold Citibank banking products and services (personal loans, credit cards, insurance plans) being among top-performers\", \"exceeded personal sales quota by 50%\"]',1,1),(2,'Contact Center Specialist','2010-11-09','2011-10-11','[\"successfully solved customer issues related to company’s services (brokerage on Moscow Exchange and mutual funds) via phone, e-mail and Skype constantly exceeding company’s customer service standards;\", \"was named \'Best employee of the month\' several times;\", \"promoted to senior specialist after one year.\"]',2,1),(3,'Contact Center Senior Specialist','2010-10-11','2013-12-25','[\"recruited, developed and mentored a team of 25 specialists to become effective in customer service, problem solving and cross-selling skills which resulted in their further promotion within the company;\", \"backed up contact center head’s functions (planning, controlling, operational management, statistics handling) safely whenever required;\", \"created and implemented training program for new employees which improved overall performance and reduced the period needed for new staff to be put on the hotline by 30%.\"]',2,1),(4,'RateCard Manager','2014-01-09','2014-05-31','[\"ensured timely provision of pre-ordered Rate Card services and goods worth $3.5M needed during the Games (technology, vehicles, furniture) to more than 200 customers: accredited press agencies, broadcasters, National Olympic Committees and partners;\", \"ensured accurate execution of games-time orders worth $300K (validation, fulfilment, delivery and removal) working directly with logistics, technology and transportation teams;\", \"achieved >90% customer satisfaction rate among leading press agencies (Associated Press, Thomson Reuters, Getty Images, etc.) while running Rate Card Service desk at the Main Press Center during the games under stress and tough deadlines;\", \"managed a team of 5 volunteers;\", \"secured timely deposit returns to customers working closely with finance and accounting teams after the games;\", \"received a commendation for the overall performance.\"]',3,1);
/*!40000 ALTER TABLE `sn_app_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_onlinecourse`
--

DROP TABLE IF EXISTS `sn_app_onlinecourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_onlinecourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `school` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `url` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sn_app_onlinecourse_a8452ca7` (`person_id`),
  CONSTRAINT `sn_app_onlinecour_person_id_2881709d328025a8_fk_sn_app_person_id` FOREIGN KEY (`person_id`) REFERENCES `sn_app_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_onlinecourse`
--

LOCK TABLES `sn_app_onlinecourse` WRITE;
/*!40000 ALTER TABLE `sn_app_onlinecourse` DISABLE KEYS */;
INSERT INTO `sn_app_onlinecourse` VALUES (1,'LFS101x.2 Introduction to Linux','Linux Foundation','2015-02-01','https://s3.amazonaws.com/verify.edx.org/downloads/1f9fe59b3a8e4b9aa3f8aeb0ce498009/Certificate.pdf',1),(2,'6.00.1x Introduction to Computer Science and Programming Using Python','MITx','2015-03-01','https://s3.amazonaws.com/verify.edx.org/downloads/c6a3aad72b474491ab9d0cd90b91cd2e/Certificate.pdf',1);
/*!40000 ALTER TABLE `sn_app_onlinecourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_person`
--

DROP TABLE IF EXISTS `sn_app_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `birthdate` date NOT NULL,
  `address` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `telephone` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `facebook_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `linkedin_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `instagram_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `flickr_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `github_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `twitter_link` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `skills_json` longtext COLLATE utf8_unicode_ci NOT NULL,
  `hobbies_json` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_person`
--

LOCK TABLES `sn_app_person` WRITE;
/*!40000 ALTER TABLE `sn_app_person` DISABLE KEYS */;
INSERT INTO `sn_app_person` VALUES (1,'Sergey','Nikiforov','1987-10-14','Moscow, Russia','serge.a.nikiforov@gmail.com','+7 (916) 323-69-73','https://www.facebook.com/serge.nikiforov','https://ru.linkedin.com/in/sergeynikiforov','https://instagram.com/dissolved_boy/','https://www.flickr.com/photos/dissolved_photos/','https://github.com/sergeynikiforov','https://twitter.com/dissolved_boy','[\"Linux\", \" C/C++\", \" Python\", \" HTML/CSS\"]','[\"active runner (finished half-marathon in Amsterdam, now training for the full one)\",\r\n\"deep interest in photography (publications, sales through Getty Images)\",\r\n\"passionate about travelling (most recent - 3-month trip to South-East Asia: Thailand, Cambodia, Vietnam, Laos)\"]');
/*!40000 ALTER TABLE `sn_app_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_photo`
--

DROP TABLE IF EXISTS `sn_app_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publicID` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `num_views` int(10) unsigned NOT NULL,
  `url` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_photo`
--

LOCK TABLES `sn_app_photo` WRITE;
/*!40000 ALTER TABLE `sn_app_photo` DISABLE KEYS */;
INSERT INTO `sn_app_photo` VALUES (1,'yhtla86f8wrkzbcqnad1','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765655/yhtla86f8wrkzbcqnad1.jpg'),(2,'rewnzkyecppbrjglmqvs','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765657/rewnzkyecppbrjglmqvs.jpg'),(3,'rqfvuwxxj0dnyjgh3zhb','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765660/rqfvuwxxj0dnyjgh3zhb.jpg'),(4,'fxicuyo78a15jj6bt8cj','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765663/fxicuyo78a15jj6bt8cj.jpg'),(5,'opuayvnoirsyxzqajiba','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765671/opuayvnoirsyxzqajiba.jpg'),(6,'fqlo0smkgxyaaxrczsex','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765674/fqlo0smkgxyaaxrczsex.jpg'),(7,'vvgoohw0jb8t72wswmad','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765676/vvgoohw0jb8t72wswmad.jpg'),(8,'qn0n0exvz5mzgcy2rsic','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765678/qn0n0exvz5mzgcy2rsic.jpg'),(9,'nzfnlygqnwhpphfvudgj','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765680/nzfnlygqnwhpphfvudgj.jpg'),(10,'poqwvapmpb1vgip8avit','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1440765682/poqwvapmpb1vgip8avit.jpg'),(13,'udjzhkdffu6bmkttpn6h','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195708/udjzhkdffu6bmkttpn6h.jpg'),(14,'z3zecnatmbp8fl7htlhm','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195712/z3zecnatmbp8fl7htlhm.jpg'),(15,'yh07qv5lctson5hjzhdr','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195714/yh07qv5lctson5hjzhdr.jpg'),(16,'rotsfoi4ri5cyalhxm4r','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195717/rotsfoi4ri5cyalhxm4r.jpg'),(17,'jx2zhtvelbnephbjtjut','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195720/jx2zhtvelbnephbjtjut.jpg'),(18,'vythkdw7cjdf297fxfkr','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195723/vythkdw7cjdf297fxfkr.jpg'),(19,'yq9bhddanbd7v9vte9km','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195725/yq9bhddanbd7v9vte9km.jpg'),(20,'pfjn8cpex6twiqjxsh0l','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195727/pfjn8cpex6twiqjxsh0l.jpg'),(21,'cfjtyku7vkhj70loxs7v','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195729/cfjtyku7vkhj70loxs7v.jpg'),(22,'rpbsa1i29owm6bet7ogw','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195732/rpbsa1i29owm6bet7ogw.jpg'),(23,'yczarfpz9bhflylyid53','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195734/yczarfpz9bhflylyid53.jpg'),(24,'tisdbjicxcwbzyjhs9py','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195736/tisdbjicxcwbzyjhs9py.jpg'),(25,'jr4dorlchslo7hfmidxr','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195739/jr4dorlchslo7hfmidxr.jpg'),(26,'e0qbwqhnb29v8s7wgmlp','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195741/e0qbwqhnb29v8s7wgmlp.jpg'),(27,'mckeyozhkpblmz6rgo7g','Untitled','No description',0,'https://res.cloudinary.com/sergeynikiforov/image/upload/v1441195744/mckeyozhkpblmz6rgo7g.jpg');
/*!40000 ALTER TABLE `sn_app_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_photoinphotoset`
--

DROP TABLE IF EXISTS `sn_app_photoinphotoset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_photoinphotoset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order` int(10) unsigned NOT NULL,
  `photo_id` int(11) NOT NULL,
  `photoset_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sn_app_photoinphoto_photo_id_3af3bcfc9012799a_fk_sn_app_photo_id` (`photo_id`),
  KEY `sn_app_photoinphotoset_26d670ac` (`photoset_id`),
  CONSTRAINT `sn_app_photoi_photoset_id_586fb3f1d5780f89_fk_sn_app_photoset_id` FOREIGN KEY (`photoset_id`) REFERENCES `sn_app_photoset` (`id`),
  CONSTRAINT `sn_app_photoinphoto_photo_id_3af3bcfc9012799a_fk_sn_app_photo_id` FOREIGN KEY (`photo_id`) REFERENCES `sn_app_photo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_photoinphotoset`
--

LOCK TABLES `sn_app_photoinphotoset` WRITE;
/*!40000 ALTER TABLE `sn_app_photoinphotoset` DISABLE KEYS */;
INSERT INTO `sn_app_photoinphotoset` VALUES (1,0,1,1),(2,1,2,1),(3,2,3,1),(4,3,4,1),(5,4,5,1),(6,5,6,1),(7,6,7,1),(8,7,8,1),(9,8,9,1),(10,9,10,1),(13,0,13,2),(14,1,14,2),(15,2,15,2),(16,3,16,2),(17,4,17,2),(18,5,18,2),(19,6,19,2),(20,7,20,2),(21,8,21,2),(22,9,22,2),(23,10,23,2),(24,11,24,2),(25,12,25,2),(26,13,26,2),(27,14,27,2);
/*!40000 ALTER TABLE `sn_app_photoinphotoset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sn_app_photoset`
--

DROP TABLE IF EXISTS `sn_app_photoset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sn_app_photoset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `num_views` int(10) unsigned NOT NULL,
  `num_photos` int(10) unsigned NOT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sn_app_photoset_title_407b46ea7ad6d65b_uniq` (`title`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sn_app_photoset`
--

LOCK TABLES `sn_app_photoset` WRITE;
/*!40000 ALTER TABLE `sn_app_photoset` DISABLE KEYS */;
INSERT INTO `sn_app_photoset` VALUES (1,'test','Est eu vidit deserunt, vidit reprimique an mel. No eius saepe facilisi vim, est officiis sapientem moderatius ne. Ad dicunt malorum accusam duo, et eam agam maiestatis. No eos quod cetero sensibus. Saepe tritani deseruisse ex mea, an usu sale atqui. Mei id magna lucilius adipiscing, vix reque debet reprimique ut, eros alterum bonorum ad vim. Omnis habeo sapientem no eam, eripuit perpetua disputando ne vis, mundi hendrerit sea ne.',716,10,'test'),(2,'andalusia_test','none',90,15,'andalusia_test');
/*!40000 ALTER TABLE `sn_app_photoset` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-18 21:46:22
