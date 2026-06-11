-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 20, 2024 at 06:21 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- --------------------------------------------------------

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
CREATE TABLE IF NOT EXISTS `dept` (
  `did` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(20) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `dept`
--

INSERT INTO `dept` (`did`, `dname`) VALUES
(1, 'IT'),
(2, 'FINANCE'),
(3, 'civil'),
(4, ''),
(5, 'advertisment'),
(6, 'electrical'),
(7, 'network');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 ,
  `object_repr` varchar(200) CHARACTER SET utf8mb4  NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4  NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-21 20:44:05'),
(2, 'auth', '0001_initial', '2024-02-21 20:44:06'),
(3, 'admin', '0001_initial', '2024-02-21 20:44:06'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-21 20:44:06'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-21 20:44:06'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-21 20:44:06'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-21 20:44:06'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-21 20:44:06'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-21 20:44:06'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-21 20:44:06'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-21 20:44:06'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-21 20:44:06'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-21 20:44:06'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-21 20:44:06'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-21 20:44:06'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-21 20:44:06'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-21 20:44:06'),
(18, 'sessions', '0001_initial', '2024-02-21 20:44:06');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6x1ptdsdtrhgbd6uvanifpgplc8woph6', '.eJyrVirNTFGyMrTUUSrNS8xNVbJSSiwqzVMCcgsSi4uRuCWVBSDZ1NwCpVoAzQQRFA:1riLAt:e21YTA2odXfbEfngt_1Qh77JdeAmnl7J5rAMeid9EaU', '2024-03-21 21:21:11'),
('axji59m46dnwk0fem7dc0heal5pfl30g', '.eJyrVirNTFGyMjLTUSrNS8xNVbJSyk3MK3VIz03MzNFLzs9VAkoUJBYXQyVA3JLKApC6jNTEFKVaAK_uFQ8:1rvaFE:M6BAnSZ47OgCDOLvvyGAmby_sSmhz2fiCOfrPdZ4Xuo', '2024-04-27 10:04:24'),
('fu250aei66jnocps9jrxmd986img0y4r', 'eyJ1bmFtZSI6InZpbnVAZ21haWwuY29tIiwidXBhc3MiOiJ2aW51In0:1rttkL:mNzZ-i2qXxoyPTVQtn-b4Yg3jfieCO6avTzp8om9zmw', '2024-04-22 18:29:33'),
('ovzmvjpe3m4a0fro9iozeqavoi06hez6', '.eJyrVirNS8xNVbJSSkzJzcxzSM9NzMzRS87PVdJRKi1ILC6GyYD4mSlKVgZAuqSyAK5DqRYA-VkV_g:1rx2gB:vsW7UZS3N3O6LP6rPU9xlE-p9XRhbWEEUhvSa8QzObQ', '2024-05-01 10:38:15'),
('u75fhqek6zyzhwawxiv6nd3gzwz4hkj5', '.eJyrVirNTFGyMjLTUSrNS8xNVbJSyk3MK3VIz03MzNFLzs9VAkoUJBYXQyVA3JLKApC6jNTEFKVaAK_uFQ8:1rvZgc:fv-MBXp6Pitj1PmOWgrzpu1KG6HBB0vPiPCnr1MxnZ0', '2024-04-27 09:28:38'),
('wsndpezur7533dezwum2sda9oubwki8n', 'N2RmNjBmNGMwYTNmMzdiYWMyMTdmNjdiMzFmMjQwNWRjZjBiYjM1NDp7InVuYW1lIjoiYW51QGdtYWlsLmNvbSIsInVwYXNzIjoiYW51IiwidWlkIjoyOCwidXR5cGUiOiJoZWFkIn0=', '2024-05-02 06:55:59'),
('z725w7ly2hvvam7skt3ia5qagj1cguog', 'NmVmMmFmN2Q4ZDc4YjhjMmY4NjBlNDIxOGJhN2E2YjQ2ODQ3NTdiNDp7InVuYW1lIjoibWludUBnbWFpbC5jb20iLCJ1cGFzcyI6Im1pbnUifQ==', '2024-05-04 06:20:55');

-- --------------------------------------------------------

--
-- Table structure for table `emotion`
--

DROP TABLE IF EXISTS `emotion`;
CREATE TABLE IF NOT EXISTS `emotion` (
  `eid` int NOT NULL AUTO_INCREMENT,
  `hid` int NOT NULL,
  `emotion` varchar(40) NOT NULL,
  `date` varchar(30) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emotion`
--

INSERT INTO `emotion` (`eid`, `hid`, `emotion`, `date`) VALUES
(1, 27, 'Stress', ''),
(2, 27, 'Stress', ''),
(3, 27, 'Stress', ''),
(4, 27, 'Stress', ''),
(5, 27, 'Stress', ''),
(6, 27, 'Stress', ''),
(7, 27, 'Stress', ''),
(8, 27, 'Stress', ''),
(9, 27, 'Stress', ''),
(10, 27, 'Stress', ''),
(11, 27, 'Stress', ''),
(12, 27, 'Stress', ''),
(13, 27, 'Stress', ''),
(14, 27, 'Stress', ''),
(15, 27, 'Stress', ''),
(16, 27, 'Stress', ''),
(17, 27, 'Stress', ''),
(18, 27, 'Stress', ''),
(19, 27, 'Stress', ''),
(20, 27, 'Stress', ''),
(21, 27, 'Stress', ''),
(22, 27, 'Stress', ''),
(23, 27, 'Stress', ''),
(24, 27, 'Stress', ''),
(25, 27, 'Stress', ''),
(26, 27, 'Stress', ''),
(27, 27, 'Stress', ''),
(28, 27, 'Stress', ''),
(29, 27, 'Stress', '2024-04-17'),
(30, 27, 'Stress', '2024-04-17'),
(31, 27, 'Stress', '2024-04-17'),
(32, 27, 'Stress', '2024-04-17'),
(33, 27, 'Stress', '2024-04-17'),
(34, 27, 'Stress', '2024-04-17'),
(35, 27, 'Stress', '2024-04-17'),
(36, 27, 'Stress', '2024-04-17'),
(37, 27, 'Stress', '2024-04-17'),
(38, 27, 'Stress', '2024-04-17'),
(39, 27, 'Stress', '2024-04-17'),
(40, 27, 'Stress', '2024-04-17'),
(41, 29, 'Stress', '2024-04-18'),
(42, 29, 'Stress', '2024-04-18'),
(43, 29, 'Stress', '2024-04-18'),
(44, 29, 'Stress', '2024-04-18'),
(45, 29, 'Stress', '2024-04-18'),
(46, 29, 'Stress', '2024-04-18'),
(47, 31, 'Stress', '2024-04-20'),
(48, 31, 'Stress', '2024-04-20'),
(49, 31, 'Stress', '2024-04-20'),
(50, 31, 'Stress', '2024-04-20'),
(51, 31, 'Stress', '2024-04-20'),
(52, 31, 'Stress', '2024-04-20');

-- --------------------------------------------------------

--
-- Table structure for table `head`
--

DROP TABLE IF EXISTS `head`;
CREATE TABLE IF NOT EXISTS `head` (
  `hid` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(15) NOT NULL,
  `fname` varchar(10) NOT NULL,
  `lname` varchar(10) NOT NULL,
  `address` varchar(30) NOT NULL,
  `phone` int NOT NULL,
  `gender` varchar(8) NOT NULL,
  `desig` varchar(15) NOT NULL,
  `exp` varchar(10) NOT NULL,
  `qual` varchar(20) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `doj` varchar(10) NOT NULL,
  `username` varchar(15) NOT NULL,
  `etype` varchar(10) NOT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `head`
--

INSERT INTO `head` (`hid`, `dname`, `fname`, `lname`, `address`, `phone`, `gender`, `desig`, `exp`, `qual`, `dob`, `doj`, `username`, `etype`) VALUES
(17, 'IT', 'aswin', 'k', 'Amal Bhavanam\r\n', 2147483647, 'male', 'project head', '6 years', 'MCA', '1992-08-19', '2024-04-19', 'aswin', 'head'),
(18, 'FINANCE', 'bobin', 'm', 'Bobin Nivas', 2147483647, 'male', 'coordinator', '5 years', 'MCOM', '1997-11-13', '2023-09-13', 'bobin', 'head'),
(19, 'IT', 'arun', 'l', 'arun Bhavanam', 564123958, 'male', 'Develpoer', '4 years', 'BCA', '1990-10-30', '2024-02-27', 'arun', 'emp'),
(20, 'FINANCE', 'varun', 'm', 'varunas villa', 2147483647, 'male', 'executive', '2 year', 'MCOM Finance', '1999-10-14', '2024-01-09', 'varun', 'emp'),
(21, 'IT', 'kannan', 'j', 'ghvchgc', 567687, 'male', 'Develpoer', '5 years', 'MCA', '2024-02-28', '2024-03-05', 'vishnu', 'emp'),
(24, '', 'aswin', 'm', 'Amal Bhavanam\r\nTheppupara P O', 2147483647, 'male', 'accountant', '2 year', 'BBA', '2024-04-27', '2024-04-13', 'aswinm123@gmail', 'head'),
(25, '', 'anju', 'm', 'ghgfd', 2147483647, 'female', 'ass', '4', 'bsc', '2024-02-07', '2024-04-02', 'anju123@gmail.c', 'emp'),
(26, 'advertisment', 'manu', 's', 'hhjj', 2147483647, 'male', 'ddd', '2', 'mca', '2024-04-20', '2024-04-20', 'manu@gmail.com', 'head'),
(27, 'advertisment', 'vinu m', 'm', 'kgghdd', 2147483647, 'male', 'hjvv', '5', 'BCA', '2024-04-18', '2024-04-10', 'vinu@gmail.com', 'emp'),
(28, 'electrical', 'Anu', 'Mathew', 'ddd', 2147483647, 'male', 'ftgg', '3', 'gg', '2000-10-18', '2023-03-22', 'anu@gmail.com', 'head'),
(29, 'electrical', 'tom', 'gg', 'gfff', 2147483647, 'male', 'gtgg', '6', 'tttyh', '1999-02-02', '2023-06-06', 'tom@gmail.com', 'emp'),
(30, 'network', 'Minu', 'Mathew', 'eee', 2147483647, 'female', 'fgg', '5', 'ggg', '2002-12-30', '2023-01-16', 'minu@gmail.com', 'head'),
(31, 'network', 'Eva', 'aa', 'sddd', 2147483647, 'female', 'ghgh', '3', 'ddft', '2001-01-20', '2023-01-01', 'eva@gmail.com', 'emp');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `lid` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL,
  `uname` varchar(15) NOT NULL,
  `upass` varchar(15) NOT NULL,
  `utype` varchar(15) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`lid`, `uid`, `uname`, `upass`, `utype`) VALUES
(1, 0, 'admin@gmail.com', 'admin', 'admin'),
(10, 3, 'aswin', 'aswin', 'head'),
(11, 4, 'bobin', 'bobin', 'head'),
(12, 5, 'jinu', 'jinu', 'head'),
(24, 17, 'aswin', 'aswin', 'head'),
(25, 18, 'bobin', 'bobin', 'head'),
(26, 19, 'arun', 'arun', 'emp'),
(27, 20, 'varun', 'varun', 'emp'),
(28, 21, 'vishnu', 'vishnu', 'emp'),
(29, 22, 'achu', 'achu', 'emp'),
(30, 23, '', '', 'head'),
(31, 24, 'aswinm123@gmail', 'aswinm', 'head'),
(32, 25, 'anju123@gmail.c', 'anjum', 'emp'),
(33, 26, 'manu@gmail.com', 'manu', 'head'),
(34, 27, 'vinu@gmail.com', 'vinu', 'emp'),
(35, 28, 'anu@gmail.com', 'anu', 'head'),
(36, 29, 'tom@gmail.com', 'tom', 'emp'),
(37, 30, 'minu@gmail.com', 'minu', 'head'),
(38, 31, 'eva@gmail.com', 'eva', 'emp');

-- --------------------------------------------------------

--
-- Table structure for table `survey`
--

DROP TABLE IF EXISTS `survey`;
CREATE TABLE IF NOT EXISTS `survey` (
  `sid` int NOT NULL AUTO_INCREMENT,
  `empid` int NOT NULL,
  `attr` varchar(10) NOT NULL,
  `stress` varchar(10) NOT NULL,
  `sdate` date NOT NULL,
  `month` varchar(10) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `survey`
--

INSERT INTO `survey` (`sid`, `empid`, `attr`, `stress`, `sdate`, `month`) VALUES
(1, 19, 'Nil', 'Possibiliy', '2024-03-20', '0000-00-00'),
(2, 19, 'Nil', 'Possibiliy', '2024-03-20', '0000-00-00'),
(3, 19, 'Nil', 'Possibiliy', '2024-03-20', '03'),
(4, 19, 'Nil', 'Depression', '2024-03-20', '03'),
(5, 19, 'Nil', 'Depression', '2024-03-20', '03'),
(6, 29, 'Might Not ', 'Normal', '2024-04-18', '04'),
(7, 31, 'Might Not ', 'Normal', '2024-04-20', '04');

-- --------------------------------------------------------

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
CREATE TABLE IF NOT EXISTS `task` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `pcode` int NOT NULL,
  `tname` varchar(20) NOT NULL,
  `details` varchar(600) NOT NULL,
  `ldate` date NOT NULL,
  `status` varchar(15) NOT NULL,
  `hid` int NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `task`
--

INSERT INTO `task` (`tid`, `pcode`, `tname`, `details`, `ldate`, `status`, `hid`) VALUES
(9, 1, 'sss', 'sssss', '2024-03-29', 'pending', 0),
(8, 1, 'sdd', 'dffg', '2024-03-22', 'pending', 21),
(7, 1, 'task2', 'sxdc', '2024-03-28', 'completed', 22),
(6, 1, 'task1', 'tas1 de', '2024-04-04', 'completed', 19),
(10, 4, 'design', 'hghj', '2025-12-04', 'pending', 19),
(11, 4, 'calculation', 'HVHGV', '0000-00-00', 'pending', 0),
(12, 6, 'task1m', 'jvgvgy', '2024-04-12', 'completed', 27),
(13, 7, 'task2', 'shbvhjhj', '2024-04-26', 'completed', 27),
(14, 8, 'er3322', 'dsdd', '2024-04-26', 'on progress', 29);

-- --------------------------------------------------------

--
-- Table structure for table `task_assign`
--

DROP TABLE IF EXISTS `task_assign`;
CREATE TABLE IF NOT EXISTS `task_assign` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `tid` int NOT NULL,
  `hid` int NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `task_assign`
--

INSERT INTO `task_assign` (`aid`, `tid`, `hid`) VALUES
(1, 1, 19);

-- --------------------------------------------------------

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
CREATE TABLE IF NOT EXISTS `works` (
  `pcode` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(15) NOT NULL,
  `pname` varchar(25) NOT NULL,
  `descrip` varchar(600) NOT NULL,
  `dos` date NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`pcode`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 ;

--
-- Dumping data for table `works`
--

INSERT INTO `works` (`pcode`, `dname`, `pname`, `descrip`, `dos`, `status`) VALUES
(2, 'FINANCE', 'sample1', 'new', '2024-03-20', ''),
(3, 'IT', 'sample', 'hghr', '2024-03-12', 'completed'),
(4, 'IT', 'gdhg', 'knnk', '2024-03-21', 'on going'),
(6, 'advertisment', 'new adv', 'hbuft', '2024-04-18', 'completed'),
(7, 'advertisment', 'new', 'hugv', '2024-04-19', 'pending'),
(8, 'electrical', 'Er33', 'dddd', '2024-05-18', 'pending');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
