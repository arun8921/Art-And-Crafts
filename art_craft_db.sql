-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2023 at 04:25 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `art_craft_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add complaint', 8, 'add_complaint'),
(30, 'Can change complaint', 8, 'change_complaint'),
(31, 'Can delete complaint', 8, 'delete_complaint'),
(32, 'Can view complaint', 8, 'view_complaint'),
(33, 'Can add district', 9, 'add_district'),
(34, 'Can change district', 9, 'change_district'),
(35, 'Can delete district', 9, 'delete_district'),
(36, 'Can view district', 9, 'view_district'),
(37, 'Can add feedback', 10, 'add_feedback'),
(38, 'Can change feedback', 10, 'change_feedback'),
(39, 'Can delete feedback', 10, 'delete_feedback'),
(40, 'Can view feedback', 10, 'view_feedback'),
(41, 'Can add login', 11, 'add_login'),
(42, 'Can change login', 11, 'change_login'),
(43, 'Can delete login', 11, 'delete_login'),
(44, 'Can view login', 11, 'view_login'),
(45, 'Can add notification', 12, 'add_notification'),
(46, 'Can change notification', 12, 'change_notification'),
(47, 'Can delete notification', 12, 'delete_notification'),
(48, 'Can view notification', 12, 'view_notification'),
(49, 'Can add order', 13, 'add_order'),
(50, 'Can change order', 13, 'change_order'),
(51, 'Can delete order', 13, 'delete_order'),
(52, 'Can view order', 13, 'view_order'),
(53, 'Can add product', 14, 'add_product'),
(54, 'Can change product', 14, 'change_product'),
(55, 'Can delete product', 14, 'delete_product'),
(56, 'Can view product', 14, 'view_product'),
(57, 'Can add state', 15, 'add_state'),
(58, 'Can change state', 15, 'change_state'),
(59, 'Can delete state', 15, 'delete_state'),
(60, 'Can view state', 15, 'view_state'),
(61, 'Can add user_register', 16, 'add_user_register'),
(62, 'Can change user_register', 16, 'change_user_register'),
(63, 'Can delete user_register', 16, 'delete_user_register'),
(64, 'Can view user_register', 16, 'view_user_register'),
(65, 'Can add artist_register', 17, 'add_artist_register'),
(66, 'Can change artist_register', 17, 'change_artist_register'),
(67, 'Can delete artist_register', 17, 'delete_artist_register'),
(68, 'Can view artist_register', 17, 'view_artist_register'),
(69, 'Can add raw_materials', 18, 'add_raw_materials'),
(70, 'Can change raw_materials', 18, 'change_raw_materials'),
(71, 'Can delete raw_materials', 18, 'delete_raw_materials'),
(72, 'Can view raw_materials', 18, 'view_raw_materials'),
(73, 'Can add artist_work', 19, 'add_artist_work'),
(74, 'Can change artist_work', 19, 'change_artist_work'),
(75, 'Can delete artist_work', 19, 'delete_artist_work'),
(76, 'Can view artist_work', 19, 'view_artist_work'),
(77, 'Can add order_artist_work', 20, 'add_order_artist_work'),
(78, 'Can change order_artist_work', 20, 'change_order_artist_work'),
(79, 'Can delete order_artist_work', 20, 'delete_order_artist_work'),
(80, 'Can view order_artist_work', 20, 'view_order_artist_work'),
(81, 'Can add order_raw_materials', 21, 'add_order_raw_materials'),
(82, 'Can change order_raw_materials', 21, 'change_order_raw_materials'),
(83, 'Can delete order_raw_materials', 21, 'delete_order_raw_materials'),
(84, 'Can view order_raw_materials', 21, 'view_order_raw_materials'),
(85, 'Can add work_comment', 22, 'add_work_comment'),
(86, 'Can change work_comment', 22, 'change_work_comment'),
(87, 'Can delete work_comment', 22, 'delete_work_comment'),
(88, 'Can view work_comment', 22, 'view_work_comment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$QY3UT6fKBX7fzzZysQrbNx$dx0kjmxe/5OcinTwH4+wrucbWF/PFuizDM/aGkim7cQ=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-04-09 09:14:31.051188');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(17, 'artcraftapp', 'artist_register'),
(19, 'artcraftapp', 'artist_work'),
(7, 'artcraftapp', 'category'),
(8, 'artcraftapp', 'complaint'),
(9, 'artcraftapp', 'district'),
(10, 'artcraftapp', 'feedback'),
(11, 'artcraftapp', 'login'),
(12, 'artcraftapp', 'notification'),
(13, 'artcraftapp', 'order'),
(20, 'artcraftapp', 'order_artist_work'),
(21, 'artcraftapp', 'order_raw_materials'),
(14, 'artcraftapp', 'product'),
(18, 'artcraftapp', 'raw_materials'),
(15, 'artcraftapp', 'state'),
(16, 'artcraftapp', 'user_register'),
(22, 'artcraftapp', 'work_comment'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-09 08:34:15.444463'),
(2, 'auth', '0001_initial', '2023-04-09 08:34:15.914490'),
(3, 'admin', '0001_initial', '2023-04-09 08:34:16.014733'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-09 08:34:16.030354'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-09 08:34:16.045977'),
(6, 'artcraftapp', '0001_initial', '2023-04-09 08:34:16.177460'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-04-09 08:34:16.262114'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-04-09 08:34:16.315522'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-04-09 08:34:16.346766'),
(10, 'auth', '0004_alter_user_username_opts', '2023-04-09 08:34:16.362388'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-04-09 08:34:16.431390'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-04-09 08:34:16.447010'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-04-09 08:34:16.447010'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-04-09 08:34:16.478255'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-04-09 08:34:16.516029'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-04-09 08:34:16.547258'),
(17, 'auth', '0011_update_proxy_permissions', '2023-04-09 08:34:16.562881'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-04-09 08:34:16.578500'),
(19, 'sessions', '0001_initial', '2023-04-09 08:34:16.616280'),
(20, 'artcraftapp', '0002_artist_register', '2023-04-09 09:33:57.643814'),
(21, 'artcraftapp', '0003_raw_materials', '2023-04-10 00:28:23.621252'),
(22, 'artcraftapp', '0004_artist_work', '2023-04-10 01:16:25.049647'),
(23, 'artcraftapp', '0005_artist_work_artist_login_id', '2023-04-10 01:32:29.119095'),
(24, 'artcraftapp', '0006_order_artist_work_order_raw_materials_and_more', '2023-04-30 15:33:43.699828'),
(25, 'artcraftapp', '0007_work_comment', '2023-05-01 01:35:12.853133'),
(26, 'artcraftapp', '0008_rename_status_work_comment_comment', '2023-05-01 01:56:27.275343');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4d5h4pkvhfzaihjomu6ckc75349ph46h', 'eyJzdW5hbWUiOiJqYW4xMjMiLCJzbG9naWQiOjN9:1prfoX:nvtaPMFM0Qv2-pNc289-E3bMOl-60929hSNOQB97gm4', '2023-05-10 14:08:09.690684'),
('54avzdxkv1lxdbsn1f7q8238ys11jjtf', 'eyJzdW5hbWUiOiJqYW4xMjMiLCJzbG9naWQiOjN9:1pqp37:wHKLu1G5CCl4vjGMhmsBUTekiqmoML5jjIamSSHQAZY', '2023-05-08 05:47:41.256780'),
('raxzm1cx24d4dwkbzx00fznl2nt6obb4', 'eyJzdW5hbWUiOiJqYW4xMjMiLCJzbG9naWQiOjN9:1plgav:fqV5Fyh2lM-cZqyxtt8QX7aiOhrCr_eH-Tm7ukj-UoE', '2023-04-24 01:45:21.332812'),
('w7qyig410gdrq9ofszse8bnj88377bcx', 'eyJzdW5hbWUiOiJqYW4xMjMiLCJzbG9naWQiOjN9:1pqp3P:QY_PueXxyhzSYFKpOsB059dXT8jqYuQgFsUZgzDhM1c', '2023-05-08 05:47:59.261287');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_artist`
--

CREATE TABLE `tbl_artist` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_artist`
--

INSERT INTO `tbl_artist` (`user_id`, `login_id`, `Name`, `phone_number`, `Email`, `Address`) VALUES
(1, 1, 'Unni K ', 9865457812, 'unni@gmail.com', 'unni bhavan Pathnamthitta'),
(2, 2, 'Aniyan ', 9865321245, 'aniyan@gmail.com', 'aniyan villa');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_artist_work`
--

CREATE TABLE `tbl_artist_work` (
  `artist_work_id` int(11) NOT NULL,
  `artist_work` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(50) NOT NULL,
  `artist_login_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_artist_work`
--

INSERT INTO `tbl_artist_work` (`artist_work_id`, `artist_work`, `description`, `image`, `artist_login_id`, `price`, `quantity`) VALUES
(3, 'My New Work', 'my Craft Work', '/media/14..jpg', 1, 1200, 1),
(5, 'Glass Work', 'Glass work', '/media/10..jpg', 1, 2400, 4),
(6, 'Paint Work', 'Paint Work', '/media/11..jpg', 1, 2300, 2),
(7, 'Glass Work1', 'sfdsf', '/media/12..jpg', 1, 2300, 2),
(8, 'My Work', 'fdsfsvfds ', '/media/13..jpg', 1, 2300, 2);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_category`
--

CREATE TABLE `tbl_category` (
  `category_id` int(11) NOT NULL,
  `category` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_category`
--

INSERT INTO `tbl_category` (`category_id`, `category`) VALUES
(1, 'Glass crafts'),
(2, 'Fibre and Textile crafts'),
(3, 'Flower Craft'),
(4, 'Leather Work'),
(5, 'Needle Craft'),
(6, 'Paper Craft'),
(7, 'Wood and furniture Craft'),
(8, 'Stone Craft'),
(9, 'Bottle Craft');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complaint`
--

CREATE TABLE `tbl_complaint` (
  `complaint_id` int(11) NOT NULL,
  `complaint_subject` varchar(50) NOT NULL,
  `complaint` varchar(150) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_complaint`
--

INSERT INTO `tbl_complaint` (`complaint_id`, `complaint_subject`, `complaint`, `user_login_id`, `reply`) VALUES
(1, 'Good Site for art and craft ', 'Good Site for art and craft ', 3, 'Nil');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_district`
--

CREATE TABLE `tbl_district` (
  `district_id` int(11) NOT NULL,
  `state_id` int(11) NOT NULL,
  `district` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE `tbl_feedback` (
  `feedback_id` int(11) NOT NULL,
  `feedback_subject` varchar(50) NOT NULL,
  `feedback` longtext NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`feedback_id`, `feedback_subject`, `feedback`, `user_login_id`, `reply`) VALUES
(1, 'ddw', 'eeeweqew', 3, 'Nil');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` longtext DEFAULT NULL,
  `Usertype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`login_id`, `username`, `password`, `Usertype`, `status`) VALUES
(1, 'unni123', 'unni34', 'Artist', 'Approved'),
(2, 'ani123', 'ani123', 'Artist', 'Not Approved'),
(3, 'jan123', 'jan123', 'User', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_notification`
--

CREATE TABLE `tbl_notification` (
  `notification_id` int(11) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_notification`
--

INSERT INTO `tbl_notification` (`notification_id`, `subject`, `description`, `image`) VALUES
(1, 'ondon Craft Week launches today and offers the opp', 'London Craft Week 2020: what to see and buy among 250 events across the capital this week', '/media/9..jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_order`
--

CREATE TABLE `tbl_order` (
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `entry_date` datetime(6) NOT NULL,
  `user_login_id` int(11) NOT NULL,
  `check_no_order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_order`
--

INSERT INTO `tbl_order` (`order_id`, `product_id`, `amount`, `quantity`, `status`, `entry_date`, `user_login_id`, `check_no_order`) VALUES
(1, 1, '300.00', 1, 'Not Paid', '2023-04-24 11:18:11.634524', 3, 631933),
(2, 1, '600.00', 2, 'Delivered', '2023-04-24 16:11:55.367155', 3, 427625),
(3, 1, '600.00', 2, 'Paid', '2023-04-24 16:33:22.547711', 3, 263439),
(4, 1, '300.00', 1, 'Not Paid', '2023-04-26 19:38:38.785256', 3, 819988);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_order_artist_work`
--

CREATE TABLE `tbl_order_artist_work` (
  `artist_order_id` int(11) NOT NULL,
  `artist_work_id` int(11) NOT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `entry_date` datetime(6) NOT NULL,
  `user_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_order_artist_work`
--

INSERT INTO `tbl_order_artist_work` (`artist_order_id`, `artist_work_id`, `amount`, `quantity`, `status`, `entry_date`, `user_login_id`) VALUES
(1, 3, '1200.00', 1, 'Delivered', '2023-05-01 06:23:59.677186', 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_order_raw_materials`
--

CREATE TABLE `tbl_order_raw_materials` (
  `raw_materials_order_id` int(11) NOT NULL,
  `raw_materials_id` int(11) NOT NULL,
  `amount` decimal(12,2) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `entry_date` datetime(6) NOT NULL,
  `artist_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_order_raw_materials`
--

INSERT INTO `tbl_order_raw_materials` (`raw_materials_order_id`, `raw_materials_id`, `amount`, `quantity`, `status`, `entry_date`, `artist_login_id`) VALUES
(1, 3, '2200.00', 1, 'Delivered', '2023-04-30 22:43:42.433566', 1),
(2, 1, '2500.00', 1, 'Delivered', '2023-04-30 23:10:12.659385', 1),
(3, 1, '2500.00', 1, 'Paid', '2023-05-01 05:22:15.348734', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_product`
--

CREATE TABLE `tbl_product` (
  `product_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `product` varchar(50) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(12,2) DEFAULT NULL,
  `image` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `features` longtext NOT NULL,
  `painter_name` varchar(50) NOT NULL,
  `entry_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_product`
--

INSERT INTO `tbl_product` (`product_id`, `category_id`, `product`, `quantity`, `price`, `image`, `description`, `features`, `painter_name`, `entry_date`) VALUES
(1, 1, 'pearls', 10, '300.00', '/media/8..jpg', 'rtyrty', 'dd', 'Jaimes', '2023-04-24 11:15:06.753174');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_raw_materials`
--

CREATE TABLE `tbl_raw_materials` (
  `raw_materials_id` int(11) NOT NULL,
  `raw_materials` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_raw_materials`
--

INSERT INTO `tbl_raw_materials` (`raw_materials_id`, `raw_materials`, `description`, `image`, `price`, `quantity`) VALUES
(1, 'White Pearls Craft ', 'Crafteez Jewellery Making Metal Link Extender Chain for Craft and DIY Making Purpose Silver Colors', '/media/1..JPG', 2500, 5),
(2, 'Metal Link Extender Chain', 'Crafteez Jewellery Making Metal Link Extender Chain for Craft and DIY Making Purpose Silver Colors', '/media/2..JPG', 2500, 1),
(3, 'Petalss', 'hghfgs', '/media/15..JPG', 2200, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_state`
--

CREATE TABLE `tbl_state` (
  `state_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_register`
--

CREATE TABLE `tbl_user_register` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_user_register`
--

INSERT INTO `tbl_user_register` (`user_id`, `login_id`, `Name`, `phone_number`, `Email`, `Address`) VALUES
(1, 3, 'jancy', 9874563214, 'jancy@gmail.com', 'jan villa, pathanamthitta');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_work_comment`
--

CREATE TABLE `tbl_work_comment` (
  `comment_id` int(11) NOT NULL,
  `artist_work_id` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `entry_date` datetime(6) NOT NULL,
  `user_login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_work_comment`
--

INSERT INTO `tbl_work_comment` (`comment_id`, `artist_work_id`, `comment`, `entry_date`, `user_login_id`) VALUES
(1, 3, 'sadsa', '2023-05-21 07:13:52.000000', 3),
(2, 3, 'fghgdh sffgdf', '2023-05-01 07:28:27.701260', 3),
(3, 3, 'gdfgd sgsg', '2023-05-01 07:28:33.720516', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_artist`
--
ALTER TABLE `tbl_artist`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tbl_artist_work`
--
ALTER TABLE `tbl_artist_work`
  ADD PRIMARY KEY (`artist_work_id`);

--
-- Indexes for table `tbl_category`
--
ALTER TABLE `tbl_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  ADD PRIMARY KEY (`complaint_id`);

--
-- Indexes for table `tbl_district`
--
ALTER TABLE `tbl_district`
  ADD PRIMARY KEY (`district_id`);

--
-- Indexes for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `tbl_notification`
--
ALTER TABLE `tbl_notification`
  ADD PRIMARY KEY (`notification_id`);

--
-- Indexes for table `tbl_order`
--
ALTER TABLE `tbl_order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `tbl_order_artist_work`
--
ALTER TABLE `tbl_order_artist_work`
  ADD PRIMARY KEY (`artist_order_id`);

--
-- Indexes for table `tbl_order_raw_materials`
--
ALTER TABLE `tbl_order_raw_materials`
  ADD PRIMARY KEY (`raw_materials_order_id`);

--
-- Indexes for table `tbl_product`
--
ALTER TABLE `tbl_product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `tbl_raw_materials`
--
ALTER TABLE `tbl_raw_materials`
  ADD PRIMARY KEY (`raw_materials_id`);

--
-- Indexes for table `tbl_state`
--
ALTER TABLE `tbl_state`
  ADD PRIMARY KEY (`state_id`);

--
-- Indexes for table `tbl_user_register`
--
ALTER TABLE `tbl_user_register`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tbl_work_comment`
--
ALTER TABLE `tbl_work_comment`
  ADD PRIMARY KEY (`comment_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `tbl_artist`
--
ALTER TABLE `tbl_artist`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_artist_work`
--
ALTER TABLE `tbl_artist_work`
  MODIFY `artist_work_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_category`
--
ALTER TABLE `tbl_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tbl_complaint`
--
ALTER TABLE `tbl_complaint`
  MODIFY `complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_district`
--
ALTER TABLE `tbl_district`
  MODIFY `district_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_feedback`
--
ALTER TABLE `tbl_feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_login`
--
ALTER TABLE `tbl_login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_notification`
--
ALTER TABLE `tbl_notification`
  MODIFY `notification_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_order`
--
ALTER TABLE `tbl_order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_order_artist_work`
--
ALTER TABLE `tbl_order_artist_work`
  MODIFY `artist_order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_order_raw_materials`
--
ALTER TABLE `tbl_order_raw_materials`
  MODIFY `raw_materials_order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_product`
--
ALTER TABLE `tbl_product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_raw_materials`
--
ALTER TABLE `tbl_raw_materials`
  MODIFY `raw_materials_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_state`
--
ALTER TABLE `tbl_state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_user_register`
--
ALTER TABLE `tbl_user_register`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_work_comment`
--
ALTER TABLE `tbl_work_comment`
  MODIFY `comment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
