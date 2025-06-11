-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: manga
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `artistas`
--

DROP TABLE IF EXISTS `artistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artistas` (
  `ID_ARTISTA` int NOT NULL,
  `NOMBRE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_ARTISTA`),
  UNIQUE KEY `ID_ARTISTA_UNIQUE` (`ID_ARTISTA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistas`
--

LOCK TABLES `artistas` WRITE;
/*!40000 ALTER TABLE `artistas` DISABLE KEYS */;
/*!40000 ALTER TABLE `artistas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demografias`
--

DROP TABLE IF EXISTS `demografias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `demografias` (
  `ID_DEMOGRAFIA` int NOT NULL,
  `NOMBRE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID_DEMOGRAFIA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demografias`
--

LOCK TABLES `demografias` WRITE;
/*!40000 ALTER TABLE `demografias` DISABLE KEYS */;
/*!40000 ALTER TABLE `demografias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escritores`
--

DROP TABLE IF EXISTS `escritores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `escritores` (
  `ID_ESCRITOR` int NOT NULL,
  `NOMBRE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_ESCRITOR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escritores`
--

LOCK TABLES `escritores` WRITE;
/*!40000 ALTER TABLE `escritores` DISABLE KEYS */;
/*!40000 ALTER TABLE `escritores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generos` (
  `ID_GENERO` int NOT NULL,
  `NOMBRE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_GENERO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manga_artista`
--

DROP TABLE IF EXISTS `manga_artista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manga_artista` (
  `ID_MANGA_ARTISTA` int NOT NULL,
  `ID_MANGA` int DEFAULT NULL,
  `ID_ARTISTA` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA_ARTISTA`),
  KEY `ID_ARTISTA_idx1` (`ID_ARTISTA`),
  KEY `ID_MANGA_idx1` (`ID_MANGA`),
  CONSTRAINT `ID_ARTISTA` FOREIGN KEY (`ID_ARTISTA`) REFERENCES `artistas` (`ID_ARTISTA`),
  CONSTRAINT `ID_MANGA` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manga_artista`
--

LOCK TABLES `manga_artista` WRITE;
/*!40000 ALTER TABLE `manga_artista` DISABLE KEYS */;
/*!40000 ALTER TABLE `manga_artista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manga_demografia`
--

DROP TABLE IF EXISTS `manga_demografia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manga_demografia` (
  `ID_MANGA_DEMOGRAFIA` int NOT NULL,
  `ID_MANGA` int DEFAULT NULL,
  `ID_DEMOGRAFIA` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA_DEMOGRAFIA`),
  KEY `ID_DEMOGRAFIA_idx` (`ID_DEMOGRAFIA`),
  KEY `ID_MANGA_4_idx` (`ID_MANGA`),
  CONSTRAINT `ID_DEMOGRAFIA` FOREIGN KEY (`ID_DEMOGRAFIA`) REFERENCES `demografias` (`ID_DEMOGRAFIA`),
  CONSTRAINT `ID_MANGA_4` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manga_demografia`
--

LOCK TABLES `manga_demografia` WRITE;
/*!40000 ALTER TABLE `manga_demografia` DISABLE KEYS */;
/*!40000 ALTER TABLE `manga_demografia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manga_escritor`
--

DROP TABLE IF EXISTS `manga_escritor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manga_escritor` (
  `ID_MANGA_ESCRITOR` int NOT NULL,
  `ID_MANGA` int DEFAULT NULL,
  `ID_ESCRITOR` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA_ESCRITOR`),
  KEY `ID_MANGA_2_idx` (`ID_MANGA`),
  KEY `ID_ESCRITOR_idx` (`ID_ESCRITOR`),
  CONSTRAINT `ID_ESCRITOR` FOREIGN KEY (`ID_ESCRITOR`) REFERENCES `escritores` (`ID_ESCRITOR`),
  CONSTRAINT `ID_MANGA_2` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manga_escritor`
--

LOCK TABLES `manga_escritor` WRITE;
/*!40000 ALTER TABLE `manga_escritor` DISABLE KEYS */;
/*!40000 ALTER TABLE `manga_escritor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manga_genero`
--

DROP TABLE IF EXISTS `manga_genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manga_genero` (
  `ID_MANGA_GENERO` int NOT NULL,
  `ID_MANGA` int DEFAULT NULL,
  `ID_GENERO` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA_GENERO`),
  KEY `ID_MANGA_3_idx` (`ID_MANGA`),
  KEY `ID_GENERO_idx` (`ID_GENERO`),
  CONSTRAINT `ID_GENERO` FOREIGN KEY (`ID_GENERO`) REFERENCES `generos` (`ID_GENERO`),
  CONSTRAINT `ID_MANGA_3` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manga_genero`
--

LOCK TABLES `manga_genero` WRITE;
/*!40000 ALTER TABLE `manga_genero` DISABLE KEYS */;
/*!40000 ALTER TABLE `manga_genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manga_tema`
--

DROP TABLE IF EXISTS `manga_tema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manga_tema` (
  `ID_MANGA_TEMA` int NOT NULL,
  `ID_MANGA` int DEFAULT NULL,
  `ID_TEMA` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA_TEMA`),
  KEY `ID_MANGA_idx` (`ID_MANGA`),
  KEY `ID_TEMA_idx` (`ID_TEMA`),
  CONSTRAINT `ID_MANGA_1` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`),
  CONSTRAINT `ID_TEMA` FOREIGN KEY (`ID_TEMA`) REFERENCES `temas` (`ID_TEMA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manga_tema`
--

LOCK TABLES `manga_tema` WRITE;
/*!40000 ALTER TABLE `manga_tema` DISABLE KEYS */;
/*!40000 ALTER TABLE `manga_tema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mangas`
--

DROP TABLE IF EXISTS `mangas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mangas` (
  `ID_MANGA` int NOT NULL,
  `VOLUMENES` int DEFAULT NULL,
  `CAPITULOS` int DEFAULT NULL,
  `STATUS` varchar(100) DEFAULT NULL,
  `ESTRENO` datetime DEFAULT NULL,
  `EDITORIAL` varchar(100) DEFAULT NULL,
  `LECTORES` int DEFAULT NULL,
  `ID_RANK` int DEFAULT NULL,
  PRIMARY KEY (`ID_MANGA`),
  KEY `ID_RANK_idx` (`ID_RANK`),
  CONSTRAINT `ID_RANK` FOREIGN KEY (`ID_RANK`) REFERENCES `ranks` (`ID_RANK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
ALTER TABLE mangas DROP FOREIGN KEY ID_RANK;
ALTER TABLE mangas DROP ID_RANK;
--
-- Dumping data for table `mangas`
--

LOCK TABLES `mangas` WRITE;
/*!40000 ALTER TABLE `mangas` DISABLE KEYS */;
/*!40000 ALTER TABLE `mangas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ranks`
--

DROP TABLE IF EXISTS `ranks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ranks` (
  `ID_RANK` int NOT NULL,
  `RANK` int DEFAULT NULL,
  `TITULO` varchar(200) DEFAULT NULL,
  `CALIFICACION` decimal(3,2) DEFAULT NULL,
  `LINK` varchar(500) DEFAULT NULL,
  `ID_MANGA` int DEFAULT NULL,
  PRIMARY KEY (`ID_RANK`),
  KEY `ID_MANGA_00_idx` (`ID_MANGA`),
  CONSTRAINT `ID_MANGA_00` FOREIGN KEY (`ID_MANGA`) REFERENCES `mangas` (`ID_MANGA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ranks`
--

LOCK TABLES `ranks` WRITE;
/*!40000 ALTER TABLE `ranks` DISABLE KEYS */;
/*!40000 ALTER TABLE `ranks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temas`
--

DROP TABLE IF EXISTS `temas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temas` (
  `ID_TEMA` int NOT NULL,
  `NOMBRE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID_TEMA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temas`
--

LOCK TABLES `temas` WRITE;
/*!40000 ALTER TABLE `temas` DISABLE KEYS */;
/*!40000 ALTER TABLE `temas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-06 20:21:58
