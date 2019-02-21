CREATE DATABASE `stock_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
CREATE TABLE `stocks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `code_UNIQUE` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=14289 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

USE `stock_data`;
CREATE TABLE `histories_1` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `open` varchar(20) DEFAULT NULL,
  `high` varchar(20) DEFAULT NULL,
  `low` varchar(20) DEFAULT NULL,
  `close` varchar(20) DEFAULT NULL,
  `preclose` varchar(20) DEFAULT NULL,
  `volume` varchar(20) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `adjustflag` varchar(1) DEFAULT NULL,
  `turn` varchar(20) DEFAULT NULL,
  `tradestatus` varchar(1) DEFAULT NULL,
  `pctChg` varchar(20) DEFAULT NULL,
  `peTTM` varchar(20) DEFAULT NULL,
  `pbMRQ` varchar(20) DEFAULT NULL,
  `psTTM` varchar(20) DEFAULT NULL,
  `pcfNcfTTM` varchar(20) DEFAULT NULL,
  `isST` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


USE `stock_data`;
CREATE TABLE `histories_2` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `open` varchar(20) DEFAULT NULL,
  `high` varchar(20) DEFAULT NULL,
  `low` varchar(20) DEFAULT NULL,
  `close` varchar(20) DEFAULT NULL,
  `preclose` varchar(20) DEFAULT NULL,
  `volume` varchar(20) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `adjustflag` varchar(1) DEFAULT NULL,
  `turn` varchar(20) DEFAULT NULL,
  `tradestatus` varchar(1) DEFAULT NULL,
  `pctChg` varchar(20) DEFAULT NULL,
  `peTTM` varchar(20) DEFAULT NULL,
  `pbMRQ` varchar(20) DEFAULT NULL,
  `psTTM` varchar(20) DEFAULT NULL,
  `pcfNcfTTM` varchar(20) DEFAULT NULL,
  `isST` varchar(1) DEFAULT NULL,
  `ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


USE `stock_data`;
CREATE TABLE `histories_3` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `code` varchar(45) DEFAULT NULL,
  `open` varchar(20) DEFAULT NULL,
  `high` varchar(20) DEFAULT NULL,
  `low` varchar(20) DEFAULT NULL,
  `close` varchar(20) DEFAULT NULL,
  `preclose` varchar(20) DEFAULT NULL,
  `volume` varchar(20) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `adjustflag` varchar(1) DEFAULT NULL,
  `turn` varchar(20) DEFAULT NULL,
  `tradestatus` varchar(1) DEFAULT NULL,
  `pctChg` varchar(20) DEFAULT NULL,
  `peTTM` varchar(20) DEFAULT NULL,
  `pbMRQ` varchar(20) DEFAULT NULL,
  `psTTM` varchar(20) DEFAULT NULL,
  `pcfNcfTTM` varchar(20) DEFAULT NULL,
  `isST` varchar(1) DEFAULT NULL,
  `ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



