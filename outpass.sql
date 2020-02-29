-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 29, 2020 at 06:58 PM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Bio`
--

-- --------------------------------------------------------

--
-- Table structure for table `outpass`
--

CREATE TABLE `outpass` (
  `id` int(30) NOT NULL,
  `name` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `bc` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `dept` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `rank` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `barcode` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `img` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `outpass`
--

INSERT INTO `outpass` (`id`, `name`, `bc`, `dept`, `rank`, `barcode`, `img`) VALUES
(1, 'protoe', '33669', 'MEC', 'Lecturer', 'C074', 'test.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `outpass`
--
ALTER TABLE `outpass`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `outpass`
--
ALTER TABLE `outpass`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
