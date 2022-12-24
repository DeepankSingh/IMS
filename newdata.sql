
DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `Choose` varchar(55) NOT NULL,
  `SapID` varchar(100) NOT NULL,
  `UniqueID` varchar(50) NOT NULL, 
  `Name` varchar(45) DEFAULT NULL,
  `Age_sex` varchar(10) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Issuedate` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `ChronicAilment` varchar(45) DEFAULT NULL,
  `Allergies` varchar(45) DEFAULT NULL,
  `FurtherInformation` varchar(45) DEFAULT NULL,

  PRIMARY KEY (`UniqueID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES ('Day Scholar','500088015','Aakash Nigam','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088016','Nagam Siddique','20/f','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088017','Neelambuzz singh','21/m','Betech 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088018','Rudransh Kumar','21/m','Betech 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088019','Arun Singh','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088020','Daksh tyagi','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088021','Anupriya maklogha','21/f','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088022','Suraj Kumar','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088023','Gautam annand','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C'),('Day Scholar','500088024','Vedant Bhatt','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;



-- DROP TABLE IF EXISTS hospital;

-- CREATE TABLE hospital (
-- Choose varchar(55) NOT NULL,
-- SapID varchar(100) NOT NULL,
-- Unique_ID VARCHAR(50) NOT NULL,
-- Name varchar(45) DEFAULT NULL,
-- Course varchar(45) DEFAULT NULL,
-- Age_sex varchar(10) DEFAULT NULL,
-- Issuedate varchar(45) DEFAULT NULL,
-- Time varchar(45) DEFAULT NULL,
-- ChronicAilment varchar(45) DEFAULT NULL,
-- Allergies varchar(45) DEFAULT NULL,
-- FurtherInformation varchar(45) DEFAULT NULL,
-- PRIMARY KEY (Unique_ID)
-- )

-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- LOCK TABLES hospital WRITE;
-- /*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
-- INSERT INTO hospital VALUES ('Day Scholar','500088015','Aakash
-- Nigam','21/m','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088016','Nagam
-- Siddique','20/f','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088017','Neelambuzz
-- singh','21/m','Betech 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088018','Rudransh
-- Kumar','21/m','Betech 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088019','Arun
-- Singh','21/m','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088020','Daksh
-- tyagi','21/m','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088021','Anupriya
-- maklogha','21/f','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088022','Suraj
-- Kumar','21/m','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088023','Gautam
-- annand','21/m','BCA 3','24/12/2022','02:22
-- pm','null','null','98^C'),('Day Scholar','500088024','Vedant
-- Bhatt','21/m','BCA 3','24/12/2022','02:22 pm','null','null','98^C');
-- /*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
-- UNLOCK TABLES;