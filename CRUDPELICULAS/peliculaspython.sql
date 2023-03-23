-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2023 at 03:42 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `peliculaspython`
--
CREATE DATABASE IF NOT EXISTS `peliculaspython` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `peliculaspython`;

-- --------------------------------------------------------

--
-- Table structure for table `generos`
--

CREATE TABLE `generos` (
  `idGenero` int(11) NOT NULL,
  `genNombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `generos`
--

INSERT INTO `generos` (`idGenero`, `genNombre`) VALUES
(1, 'Terror'),
(2, 'Comedia'),
(3, 'Aventuras'),
(4, 'Ciencia Ficción'),
(5, 'Drama'),
(6, 'Accion'),
(7, 'Guerra'),
(8, 'Ficcion Historica');

-- --------------------------------------------------------

--
-- Table structure for table `peliculas`
--

CREATE TABLE `peliculas` (
  `idPeliculas` int(11) NOT NULL,
  `pelCodigo` int(11) NOT NULL,
  `pelTitulo` varchar(45) COLLATE utf8_spanish_ci NOT NULL COMMENT 'Título de la película',
  `pelDuracion` int(11) NOT NULL COMMENT 'Duración en minutos',
  `pelDirector` varchar(45) COLLATE utf8_spanish_ci NOT NULL COMMENT 'Nombre del director',
  `pelFechaLanzamiento` date NOT NULL COMMENT 'fecha de lanzamiento',
  `pelResumen` text COLLATE utf8_spanish_ci NOT NULL COMMENT 'breve resumen de la pelicula ',
  `pelGenero` int(11) NOT NULL COMMENT 'llave foranea'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `peliculas`
--

INSERT INTO `peliculas` (`idPeliculas`, `pelCodigo`, `pelTitulo`, `pelDuracion`, `pelDirector`, `pelFechaLanzamiento`, `pelResumen`, `pelGenero`) VALUES
(2, 7, 'Batman vs Superman', 190, 'zack Snyder', '2016-03-23', 'Batman se enfrenta a Superman', 4),
(3, 9, 'el hombre araña', 120, 'sam raimi', '2001-06-13', 'Peter parker se vuelve el hombre araña.', 6),
(4, 10, 'son como niños', 175, 'Dennis Dugan', '2010-02-21', 'Después de 30 años, cinco amigos se reúnen en una casa del lago para llorar la pérdida de su antiguo entrenador', 2),
(6, 8, 'El aro', 155, 'Gore Verbinski', '2002-10-17', 'Una reportera debe resolver el misterio de una cinta que trae muerte a sus espectadores, antes de que sucumba a su poder.', 1),
(10, 1, 'Los Simpson: La película', 87, 'David Silverman', '2007-07-27', 'La combinación de Homero, su nuevo puerco mascota, y un silo lleno de excremento podrían provocar un desastre que amenace no solo a Springfield, sino al mundo entero.', 3),
(11, 2, 'oblivion', 123, 'hollan crauzer', '2023-03-08', 'Jack Harper y Victoria Olsen son los únicos habitantes de la Tierra, destruida hace sesenta años.', 5),
(13, 4, 'Emoji', 120, 'Tony Leondis', '2017-07-24', 'Gene, un emoji con varias expresiones, pide a su amigo Hi-5 y al desencriptador Jailbreak que le ayuden a convertirse en un emoji de una cara, como todos sus amigos.', 4),
(14, 5, 'edge of tomorrow ', 120, 'algun wey', '2023-03-06', 'muer,vuelve a vivir.', 4),
(17, 6, 'hasta el ultimo hombre', 139, 'Mel Gibson', '2016-10-16', 'La historia de Desmond T. Doss, quien, debido a que se lo prohibía su fe, combatió en la Segunda Guerra Mundial sin portar un arma.', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`idGenero`);

--
-- Indexes for table `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`idPeliculas`),
  ADD UNIQUE KEY `pelCodigo` (`pelCodigo`),
  ADD KEY `pelGenero` (`pelGenero`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `idPeliculas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `peliculas`
--
ALTER TABLE `peliculas`
  ADD CONSTRAINT `peliculas_ibfk_1` FOREIGN KEY (`pelGenero`) REFERENCES `generos` (`idGenero`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
