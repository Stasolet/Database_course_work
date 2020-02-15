CREATE DATABASE  IF NOT EXISTS `пассажироперевозочная` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `пассажироперевозочная`;
-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: пассажироперевозочная
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `автомобиль`
--

DROP TABLE IF EXISTS `автомобиль`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `автомобиль` (
  `Номер автомобиля` varchar(20) NOT NULL,
  `Производитель` varchar(45) DEFAULT NULL,
  `Модель` varchar(45) DEFAULT NULL,
  `Вместимость` int(11) unsigned DEFAULT NULL,
  `Дата покупки` date DEFAULT NULL,
  `Пробег` int(11) unsigned DEFAULT '0',
  PRIMARY KEY (`Номер автомобиля`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `автомобиль`
--

LOCK TABLES `автомобиль` WRITE;
/*!40000 ALTER TABLE `автомобиль` DISABLE KEYS */;
INSERT INTO `автомобиль` VALUES ('А321АА199','ПАЗ','ПАЗ-32053/54',37,'2016-02-03',0),('А321АА50','ПАЗ','ПАЗ-32053/54',37,'2016-02-03',0),('А321УУ46','Mercedes','Sprinter',15,'2015-01-02',0),('А877АА32','ЛИАЗ','5256',45,'2017-02-03',0),('Е212ММ32','Volkswagen','Crafter',15,'2015-02-03',0),('Н112ВВ31','ГАЗ','4012',15,'2015-01-01',0),('О932ОУ46','ЛИАЗ','5256',45,'2017-02-03',0),('Р212ОО46','Mercedes','Sprinter',15,'2015-01-02',0),('С212СА32','ЛИАЗ','ВОЯЖ',53,'2016-02-02',0),('С322АС32','ЛИАЗ','ВОЯЖ',53,'2016-02-03',0),('У323УУ50','Volkswagen','Crafter',15,'2015-06-03',0);
/*!40000 ALTER TABLE `автомобиль` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `водитель`
--

DROP TABLE IF EXISTS `водитель`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `водитель` (
  `Табельный номер` int(12) unsigned NOT NULL,
  `Номер водительского удостоверения` bigint(13) unsigned NOT NULL,
  `Фамилия` varchar(45) DEFAULT NULL,
  `Имя` varchar(45) DEFAULT NULL,
  `Отчество` varchar(45) DEFAULT NULL,
  `Дата найма` date DEFAULT NULL,
  PRIMARY KEY (`Табельный номер`),
  UNIQUE KEY `Номер водительского удостоверения_UNIQUE` (`Номер водительского удостоверения`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `водитель`
--

LOCK TABLES `водитель` WRITE;
/*!40000 ALTER TABLE `водитель` DISABLE KEYS */;
INSERT INTO `водитель` VALUES (100,3130512353,'Зубенко','Михаил','Петрович','2016-02-01'),(101,3130512351,'Астапенко','Алексей','Викторович','2016-02-10'),(102,4612343243,'Зарянов','Николай','Николаевич','2016-03-14'),(103,4612342544,'Мирный','Анатолий','Олегович','2017-05-13'),(104,5011123413,'Паровозов','Александр','Алексеевич','2018-03-21'),(105,5012384731,'Морковный','Виталий','Андреевич','2018-03-30'),(106,5231534362,'Скворцов','Пётр','Петрович','2018-04-15'),(107,3210123432,'Ивин','Иван','Петрович','2019-05-17'),(108,3210231482,'Ивин','Александр','Петрович','2019-05-17'),(109,3131512354,'Елей','Крен','Кренович','2017-02-02');
/*!40000 ALTER TABLE `водитель` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `замена водителя`
--

DROP TABLE IF EXISTS `замена водителя`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `замена водителя` (
  `Дата выдачи замены` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Номер наряда` bigint(12) unsigned NOT NULL,
  PRIMARY KEY (`Номер наряда`),
  KEY `замена_наряд_fk_idx` (`Номер наряда`),
  CONSTRAINT `fk_to_наряд` FOREIGN KEY (`Номер наряда`) REFERENCES `наряд` (`Номер наряда`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `замена водителя`
--

LOCK TABLES `замена водителя` WRITE;
/*!40000 ALTER TABLE `замена водителя` DISABLE KEYS */;
/*!40000 ALTER TABLE `замена водителя` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `маршрут`
--

DROP TABLE IF EXISTS `маршрут`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `маршрут` (
  `Номер маршрута` int(11) unsigned NOT NULL,
  `Станция отправления` int(11) unsigned DEFAULT NULL,
  `Станция прибытия` int(11) unsigned DEFAULT NULL,
  `Расстояние` float unsigned DEFAULT NULL,
  `Стоимость` float DEFAULT NULL,
  `Часы в пути` int(11) unsigned DEFAULT NULL,
  `Минуты в пути` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`Номер маршрута`),
  KEY `path_town_end_fk_idx` (`Станция прибытия`),
  KEY `path_town_start_fk_idx` (`Станция отправления`),
  CONSTRAINT `маршр_стц_fk_end` FOREIGN KEY (`Станция прибытия`) REFERENCES `станция` (`Код станции`),
  CONSTRAINT `маршр_стц_fk_start` FOREIGN KEY (`Станция отправления`) REFERENCES `станция` (`Код станции`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `маршрут`
--

LOCK TABLES `маршрут` WRITE;
/*!40000 ALTER TABLE `маршрут` DISABLE KEYS */;
INSERT INTO `маршрут` VALUES (1,2,7,620,1000,12,15),(2,2,5,100,500,2,30),(3,5,2,100,450,2,40),(4,9,5,150,520,3,10),(5,5,2,11111,111,111,111),(6,9,7,1200,1200,12,12);
/*!40000 ALTER TABLE `маршрут` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `маршрут_view`
--

DROP TABLE IF EXISTS `маршрут_view`;
/*!50001 DROP VIEW IF EXISTS `маршрут_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `маршрут_view` AS SELECT 
 1 AS `Номер маршрута`,
 1 AS `Станция отправления`,
 1 AS `Станция прибытия`,
 1 AS `Расстояние`,
 1 AS `Стоимость`,
 1 AS `Часы в пути`,
 1 AS `Минуты в пути`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `назначение автомобиля водителю`
--

DROP TABLE IF EXISTS `назначение автомобиля водителю`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `назначение автомобиля водителю` (
  `Табельный номер` int(10) unsigned NOT NULL,
  `Номер автомобиля` varchar(20) NOT NULL,
  PRIMARY KEY (`Табельный номер`,`Номер автомобиля`),
  KEY `назначение_автомобиль_fk_idx` (`Номер автомобиля`),
  CONSTRAINT `назначение_автомобиль_fk` FOREIGN KEY (`Номер автомобиля`) REFERENCES `автомобиль` (`Номер автомобиля`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `назначение_автомобиля_водитель_fk` FOREIGN KEY (`Табельный номер`) REFERENCES `водитель` (`Табельный номер`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `назначение автомобиля водителю`
--

LOCK TABLES `назначение автомобиля водителю` WRITE;
/*!40000 ALTER TABLE `назначение автомобиля водителю` DISABLE KEYS */;
INSERT INTO `назначение автомобиля водителю` VALUES (100,'А321АА199'),(107,'А321АА199'),(102,'А321АА50');
/*!40000 ALTER TABLE `назначение автомобиля водителю` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `наряд`
--

DROP TABLE IF EXISTS `наряд`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `наряд` (
  `Номер наряда` bigint(12) unsigned NOT NULL,
  `Номер маршрута` int(10) unsigned NOT NULL,
  `Табельный номер` int(10) unsigned NOT NULL,
  `Номер автомобиля` varchar(20) NOT NULL,
  `Количество пассажиров` int(10) unsigned DEFAULT NULL,
  `Выручка` float DEFAULT NULL,
  `Дата отправления` datetime NOT NULL,
  `Дата прибытия` datetime DEFAULT NULL,
  PRIMARY KEY (`Номер наряда`),
  KEY `order_auto_fk_idx` (`Номер автомобиля`),
  KEY `order_driver_fk_idx` (`Табельный номер`),
  KEY `order_path_fk_idx` (`Номер маршрута`),
  CONSTRAINT `order_auto_fk` FOREIGN KEY (`Номер автомобиля`) REFERENCES `автомобиль` (`Номер автомобиля`) ON UPDATE CASCADE,
  CONSTRAINT `order_driver_fk` FOREIGN KEY (`Табельный номер`) REFERENCES `водитель` (`Табельный номер`) ON UPDATE CASCADE,
  CONSTRAINT `order_path_fk` FOREIGN KEY (`Номер маршрута`) REFERENCES `маршрут` (`Номер маршрута`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `наряд`
--

LOCK TABLES `наряд` WRITE;
/*!40000 ALTER TABLE `наряд` DISABLE KEYS */;
/*!40000 ALTER TABLE `наряд` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `наряд_BEFORE_INSERT_авторасчёт_времени_прибытия` BEFORE INSERT ON `наряд` FOR EACH ROW BEGIN
    declare `Расчётное время прибытия` datetime;
if new.`Дата прибытия` is NULL
	then

    SELECT ADDDATE(ADDDATE(NOW(), INTERVAL `Часы в пути` HOUR),
								INTERVAL `Минуты в пути` MINUTE) 
		FROM
			маршрут 
		where 
			маршрут.`Номер маршрута` = new.`Номер маршрута`
	into `Расчётное время прибытия`;
    set new.`Дата прибытия` = `Расчётное время прибытия`;
end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `наряд_BEFORE_INSERT_учёт_вместимости_авто` BEFORE INSERT ON `наряд` FOR EACH ROW BEGIN
	declare вместимость_авто integer;
SELECT 
    Вместимость
INTO вместимость_авто FROM
    `пассажироперевозочная`.`автомобиль`
    where `автомобиль`.`Номер автомобиля` = NEW.`Номер автомобиля` limit 1;
    if  NEW.`Количество пассажиров` > вместимость_авто
    then 
	signal sqlstate '99999'
    SET MESSAGE_TEXT = 'Пассажиров больше чем мест в автомобиле';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `наряд_BEFORE_INSERT_запрет_на_водителя_в_рейсе` BEFORE INSERT ON `наряд` FOR EACH ROW BEGIN
	declare таб_номер integer;
SELECT 
    `наряд`.`Табельный номер`
INTO таб_номер FROM
    `пассажироперевозочная`.`наряд`
    where `наряд`.`Табельный номер` = NEW.`Табельный номер` and `наряд`.`Дата прибытия` > now() limit 1;
    if таб_номер = NEW.`Табельный номер`
    then 
	signal sqlstate '99999'
    SET MESSAGE_TEXT = 'Водитель находится в рейсе';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `наряд_BEFORE_INSERT_регистрация_замены_водителя` AFTER INSERT ON `наряд` FOR EACH ROW BEGIN
	declare useless integer;
SELECT 
    COUNT(*)
INTO useless FROM
    `пассажироперевозочная`.`назначение автомобиля водителю`
    where `назначение автомобиля водителю`.`Табельный номер` = NEW.`Табельный номер` AND `назначение автомобиля водителю`.`Номер автомобиля` = NEW.`Номер автомобиля`;
    if useless = 0
    then 
	insert into `замена водителя`(`Номер наряда`) values(new.`Номер наряда`);
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `наряд_view`
--

DROP TABLE IF EXISTS `наряд_view`;
/*!50001 DROP VIEW IF EXISTS `наряд_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `наряд_view` AS SELECT 
 1 AS `Номер наряда`,
 1 AS `Маршрут`,
 1 AS `Водитель`,
 1 AS `Автомобиль`,
 1 AS `Количество пассажиров`,
 1 AS `Выручка`,
 1 AS `Дата отправления`,
 1 AS `Дата прибытия`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `населённый пункт`
--

DROP TABLE IF EXISTS `населённый пункт`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `населённый пункт` (
  `Код пункта` int(11) unsigned NOT NULL,
  `Код региона` int(11) unsigned NOT NULL,
  `Название пункта` varchar(255) NOT NULL,
  PRIMARY KEY (`Код пункта`),
  KEY `town_region_fk_idx` (`Код региона`),
  CONSTRAINT `town_region_fk` FOREIGN KEY (`Код региона`) REFERENCES `регион` (`Код региона`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `населённый пункт`
--

LOCK TABLES `населённый пункт` WRITE;
/*!40000 ALTER TABLE `населённый пункт` DISABLE KEYS */;
INSERT INTO `населённый пункт` VALUES (1,31,'Белгород'),(2,31,'Старый Оскол'),(3,46,'Курск'),(4,50,'Москва'),(5,36,'Воронеж'),(6,57,'Орёл'),(7,71,'Тула');
/*!40000 ALTER TABLE `населённый пункт` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `населённый_пункт_view`
--

DROP TABLE IF EXISTS `населённый_пункт_view`;
/*!50001 DROP VIEW IF EXISTS `населённый_пункт_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `населённый_пункт_view` AS SELECT 
 1 AS `Код пункта`,
 1 AS `Название пункта`,
 1 AS `Наименование региона`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `регион`
--

DROP TABLE IF EXISTS `регион`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `регион` (
  `Код региона` int(11) unsigned NOT NULL,
  `Наименование региона` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Код региона`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `регион`
--

LOCK TABLES `регион` WRITE;
/*!40000 ALTER TABLE `регион` DISABLE KEYS */;
INSERT INTO `регион` VALUES (31,'Белгородская область'),(36,'Воронежская область'),(46,'Курская область'),(50,'Московская область'),(57,'Орловская область'),(71,'Тульская область');
/*!40000 ALTER TABLE `регион` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `состав маршрута`
--

DROP TABLE IF EXISTS `состав маршрута`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `состав маршрута` (
  `Номер маршрута` int(10) unsigned NOT NULL,
  `Номер перемещения в маршруте` int(10) unsigned NOT NULL,
  `Код станции` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`Номер маршрута`,`Номер перемещения в маршруте`),
  KEY `path_include_way_idx` (`Номер маршрута`),
  KEY `way_station_idx` (`Код станции`),
  CONSTRAINT `way_path` FOREIGN KEY (`Номер маршрута`) REFERENCES `маршрут` (`Номер маршрута`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `way_station` FOREIGN KEY (`Код станции`) REFERENCES `станция` (`Код станции`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `состав маршрута`
--

LOCK TABLES `состав маршрута` WRITE;
/*!40000 ALTER TABLE `состав маршрута` DISABLE KEYS */;
INSERT INTO `состав маршрута` VALUES (1,1,1),(1,0,3),(4,1,4),(3,1,5),(1,2,7),(2,1,7),(6,1,7),(6,0,9);
/*!40000 ALTER TABLE `состав маршрута` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `состав_маршрута_view`
--

DROP TABLE IF EXISTS `состав_маршрута_view`;
/*!50001 DROP VIEW IF EXISTS `состав_маршрута_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `состав_маршрута_view` AS SELECT 
 1 AS `Номер маршрута`,
 1 AS `Номер перемещения в маршруте`,
 1 AS `Код станции`,
 1 AS `Станция`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `станция`
--

DROP TABLE IF EXISTS `станция`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `станция` (
  `Код станции` int(11) unsigned NOT NULL,
  `Код пункта` int(11) unsigned NOT NULL,
  `Адрес` varchar(255) NOT NULL,
  `Описание` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Код станции`),
  KEY `point_town_fk_idx` (`Код пункта`),
  CONSTRAINT `point_town_fk` FOREIGN KEY (`Код пункта`) REFERENCES `населённый пункт` (`Код пункта`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `станция`
--

LOCK TABLES `станция` WRITE;
/*!40000 ALTER TABLE `станция` DISABLE KEYS */;
INSERT INTO `станция` VALUES (1,1,'пр-кт Б. Хмельницкого, 160','Автовокзал'),(2,2,'улица Архитектора Бутовой, 9','Автовокзал'),(3,3,'улица.50 лет Октября 114','Автовокзал'),(4,4,'Ореховый бульвар, вл. 24, корп. 1Г ','Автостанция \"Красногвардейская\" '),(5,4,'Щёлковское шоссе, 75 ','Автостанция \"Центральная\" '),(6,4,'Новоясеневский проспект, 4 стр.9 ','Автостанция \"Тёплый Стан\" '),(7,5,'Московский пр-т, 17','Автовокзал'),(8,6,'Улица Ленина, 23','Автовокзал'),(9,7,'Улица Ленина 26','Автовокзал');
/*!40000 ALTER TABLE `станция` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `станция_view`
--

DROP TABLE IF EXISTS `станция_view`;
/*!50001 DROP VIEW IF EXISTS `станция_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `станция_view` AS SELECT 
 1 AS `Код станции`,
 1 AS `Населённый пункт`,
 1 AS `Адрес`,
 1 AS `Описание`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'пассажироперевозочная'
--

--
-- Dumping routines for database 'пассажироперевозочная'
--
/*!50003 DROP PROCEDURE IF EXISTS `station_from_pattern` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `station_from_pattern`()
BEGIN
SELECT 
    станция.`Код станции`,
    регион.`Наименование региона`,
    `населённый пункт`.`Название пункта`,
    станция.`Описание`,
    станция.`Адрес`
FROM
    `населённый пункт`
        JOIN
    станция ON станция.`Код пункта` = `населённый пункт`.`Код пункта`
        JOIN
    регион ON регион.`Код региона` = `населённый пункт`.`Код региона`
WHERE
    `Название пункта` LIKE "%оск%";
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Маршруты_через_точку` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Маршруты_через_точку`(in path_point int)
BEGIN
select `Номер маршрута` from `состав маршрута`
where `Индекс перемещения` in(SELECT `Индекс перемещения` from `путь между станциями` where `Станция прибытия` = path_point or `Станция отправления` = path_point);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Путь между станциями` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Путь между станциями`(`ст отправления` int unsigned, `ст прибытия` int unsigned)
BEGIN
SELECT 
    `Индекс перемещения`
FROM
    `путь между станциями`
WHERE
    `Станция отправления` = `ст отправления`
        AND `Станция прибытия` = `ст прибытия`;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `маршрут_view`
--

/*!50001 DROP VIEW IF EXISTS `маршрут_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `маршрут_view` AS select `маршрут`.`Номер маршрута` AS `Номер маршрута`,`stp`.`Название пункта` AS `Станция отправления`,`enp`.`Название пункта` AS `Станция прибытия`,`маршрут`.`Расстояние` AS `Расстояние`,`маршрут`.`Стоимость` AS `Стоимость`,`маршрут`.`Часы в пути` AS `Часы в пути`,`маршрут`.`Минуты в пути` AS `Минуты в пути` from ((((`маршрут` join `станция` `sts` on((`маршрут`.`Станция отправления` = `sts`.`Код станции`))) join `станция` `ends` on((`маршрут`.`Станция прибытия` = `ends`.`Код станции`))) join `населённый пункт` `stp` on((`sts`.`Код пункта` = `stp`.`Код пункта`))) join `населённый пункт` `enp` on((`ends`.`Код пункта` = `enp`.`Код пункта`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `наряд_view`
--

/*!50001 DROP VIEW IF EXISTS `наряд_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `наряд_view` AS select `наряд`.`Номер наряда` AS `Номер наряда`,concat(`маршрут_view`.`Станция отправления`,'-',`маршрут_view`.`Станция прибытия`) AS `Маршрут`,concat(`водитель`.`Фамилия`,' ',`водитель`.`Имя`,' ',`водитель`.`Отчество`) AS `Водитель`,concat(`автомобиль`.`Номер автомобиля`,', ',`автомобиль`.`Производитель`,', ',`автомобиль`.`Модель`,', ',`автомобиль`.`Вместимость`,' мест') AS `Автомобиль`,`наряд`.`Количество пассажиров` AS `Количество пассажиров`,`наряд`.`Выручка` AS `Выручка`,`наряд`.`Дата отправления` AS `Дата отправления`,`наряд`.`Дата прибытия` AS `Дата прибытия` from (((`наряд` join `водитель` on((`наряд`.`Табельный номер` = `водитель`.`Табельный номер`))) join `маршрут_view` on((`маршрут_view`.`Номер маршрута` = `наряд`.`Номер маршрута`))) join `автомобиль` on((`наряд`.`Номер автомобиля` = `автомобиль`.`Номер автомобиля`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `населённый_пункт_view`
--

/*!50001 DROP VIEW IF EXISTS `населённый_пункт_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `населённый_пункт_view` AS select `населённый пункт`.`Код пункта` AS `Код пункта`,`населённый пункт`.`Название пункта` AS `Название пункта`,`регион`.`Наименование региона` AS `Наименование региона` from (`населённый пункт` join `регион` on((`населённый пункт`.`Код региона` = `регион`.`Код региона`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `состав_маршрута_view`
--

/*!50001 DROP VIEW IF EXISTS `состав_маршрута_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `состав_маршрута_view` AS select `состав маршрута`.`Номер маршрута` AS `Номер маршрута`,`состав маршрута`.`Номер перемещения в маршруте` AS `Номер перемещения в маршруте`,`состав маршрута`.`Код станции` AS `Код станции`,concat(`станция_view`.`Населённый пункт`,', ',`станция_view`.`Описание`,', ',`станция_view`.`Адрес`) AS `Станция` from (`состав маршрута` join `станция_view` on((`станция_view`.`Код станции` = `состав маршрута`.`Код станции`))) order by `состав маршрута`.`Номер маршрута`,`состав маршрута`.`Номер перемещения в маршруте` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `станция_view`
--

/*!50001 DROP VIEW IF EXISTS `станция_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `станция_view` AS select `станция`.`Код станции` AS `Код станции`,concat(`населённый_пункт_view`.`Название пункта`,', ',`населённый_пункт_view`.`Наименование региона`) AS `Населённый пункт`,`станция`.`Адрес` AS `Адрес`,`станция`.`Описание` AS `Описание` from (`станция` join `населённый_пункт_view` on((`станция`.`Код пункта` = `населённый_пункт_view`.`Код пункта`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-15 13:22:10
