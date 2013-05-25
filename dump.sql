DROP TABLE IF EXISTS `bulletins`;
CREATE TABLE `bulletins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(36) DEFAULT NULL,
  `body` text,
  `author` int(11) DEFAULT NULL,
  `disaster` int(11) DEFAULT NULL,
  `posttime` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author` (`author`),
  KEY `disaster` (`disaster`),
  CONSTRAINT `bulletins_ibfk_2` FOREIGN KEY (`disaster`) REFERENCES `disasters` (`id`),
  CONSTRAINT `bulletins_ibfk_1` FOREIGN KEY (`author`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `disasters`;
CREATE TABLE `disasters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(36) DEFAULT NULL,
  `type` int(1) DEFAULT NULL,
  `location` int(4) DEFAULT NULL,
  `severity` int(1) DEFAULT NULL,
  `public` int(1) DEFAULT NULL,
  `reporttime` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `personnel`;
CREATE TABLE `personnel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(36) DEFAULT NULL,
  `role` int(1) DEFAULT NULL,
  `deployed` int(1) DEFAULT NULL,
  `location` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(36) DEFAULT NULL,
  `email` varchar(36) DEFAULT NULL,
  `password` char(54) DEFAULT NULL,
  `role` int(1) DEFAULT NULL,
  `regtime` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'Sysop','test@test.com','sha1$83IqenbU$6aa39bfd1915cd4c94a20563d0bd7e88031b9b0a',5,'2013-05-25 03:23:13');
UNLOCK TABLES;
