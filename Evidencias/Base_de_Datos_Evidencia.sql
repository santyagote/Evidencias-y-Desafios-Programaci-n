-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gimnasio
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `maquinas`
--

DROP TABLE IF EXISTS `maquinas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maquinas` (
  `id_maquina` int NOT NULL AUTO_INCREMENT,
  `peso_minimo` int NOT NULL,
  `peso_maximo` int NOT NULL,
  `repeticiones_objetivo` int NOT NULL,
  `tiempo_descanso_base` int NOT NULL,
  PRIMARY KEY (`id_maquina`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maquinas`
--

LOCK TABLES `maquinas` WRITE;
/*!40000 ALTER TABLE `maquinas` DISABLE KEYS */;
INSERT INTO `maquinas` VALUES (1,20,100,10,60),(2,30,120,12,65),(3,25,150,8,55),(4,40,180,15,70),(5,50,200,10,80),(6,20,100,10,60),(7,30,120,12,65),(8,25,150,8,55),(9,40,180,15,70),(10,50,200,10,80);
/*!40000 ALTER TABLE `maquinas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registros_uso`
--

DROP TABLE IF EXISTS `registros_uso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registros_uso` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_maquina` int NOT NULL,
  `peso_usado` int NOT NULL,
  `repeticiones_realizadas` int NOT NULL,
  `movimiento_completo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_registro`),
  KEY `id_maquina` (`id_maquina`),
  CONSTRAINT `registros_uso_ibfk_1` FOREIGN KEY (`id_maquina`) REFERENCES `maquinas` (`id_maquina`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registros_uso`
--

LOCK TABLES `registros_uso` WRITE;
/*!40000 ALTER TABLE `registros_uso` DISABLE KEYS */;
INSERT INTO `registros_uso` VALUES (1,1,30,10,1),(2,1,40,8,0),(3,2,50,12,1),(4,3,25,7,1),(5,4,70,15,1),(6,5,90,10,0),(7,1,50,9,1),(8,2,100,12,1),(9,3,30,8,0),(10,4,80,14,1),(11,1,30,10,1),(12,1,40,8,0),(13,2,50,12,1),(14,3,25,7,1),(15,4,70,15,1),(16,5,90,10,0),(17,1,50,9,1),(18,2,100,12,1),(19,3,30,8,0),(20,4,80,14,1);
/*!40000 ALTER TABLE `registros_uso` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-08 15:07:05
