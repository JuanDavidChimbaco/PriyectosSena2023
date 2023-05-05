-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2023 a las 18:47:53
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventarioconstruccion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_detalleentradamateriales`
--

CREATE TABLE `appgestioninv_detalleentradamateriales` (
  `id` bigint(20) NOT NULL,
  `detCantidad` int(11) NOT NULL,
  `detPrecioUnitario` double NOT NULL,
  `detEstado` varchar(7) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `detEntradaMaterial_id` bigint(20) NOT NULL,
  `detMaterial_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_detallesolicuitud`
--

CREATE TABLE `appgestioninv_detallesolicuitud` (
  `id` bigint(20) NOT NULL,
  `detCantidadRequerida` int(11) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `detElemento_id` bigint(20) NOT NULL,
  `detSolicitud_id` bigint(20) NOT NULL,
  `detUnidadMedida_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_devolucionelemento`
--

CREATE TABLE `appgestioninv_devolucionelemento` (
  `id` bigint(20) NOT NULL,
  `devCantidadDevoluicion` int(11) NOT NULL,
  `devObservaciones` longtext DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `devSalida_id` bigint(20) NOT NULL,
  `devUsuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_devolutivo`
--

CREATE TABLE `appgestioninv_devolutivo` (
  `id` bigint(20) NOT NULL,
  `devPlacaSena` varchar(50) DEFAULT NULL,
  `devSerial` varchar(50) DEFAULT NULL,
  `devDescripcion` longtext NOT NULL,
  `devMarca` varchar(50) DEFAULT NULL,
  `devFechaIngresoSena` date NOT NULL,
  `devValor` decimal(5,2) NOT NULL,
  `devFoto` varchar(100) DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `devElemento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_elemento`
--

CREATE TABLE `appgestioninv_elemento` (
  `id` bigint(20) NOT NULL,
  `eleCodigo` varchar(15) NOT NULL,
  `eleNombre` varchar(50) NOT NULL,
  `eleTipo` varchar(12) NOT NULL,
  `eleEstado` varchar(50) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_entradamaterial`
--

CREATE TABLE `appgestioninv_entradamaterial` (
  `id` bigint(20) NOT NULL,
  `entNumeroFactura` varchar(15) NOT NULL,
  `entFechaHora` datetime(6) NOT NULL,
  `entEntregadoPor` varchar(100) NOT NULL,
  `entObservaciones` longtext DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `entProveedor_id` bigint(20) NOT NULL,
  `entUsuarioRecibe_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_estadomantenimiento`
--

CREATE TABLE `appgestioninv_estadomantenimiento` (
  `id` bigint(20) NOT NULL,
  `estNombre` varchar(50) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_ficha`
--

CREATE TABLE `appgestioninv_ficha` (
  `id` bigint(20) NOT NULL,
  `ficCodigo` int(11) NOT NULL COMMENT 'Codigo de la Ficha',
  `ficNombre` varchar(100) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_mantenimientos`
--

CREATE TABLE `appgestioninv_mantenimientos` (
  `id` bigint(20) NOT NULL,
  `manObservaciones` longtext DEFAULT NULL,
  `manFechaHoraMantenimiento` datetime(6) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `manElemento_id` bigint(20) NOT NULL,
  `manEstado_id` bigint(20) NOT NULL,
  `manPersona_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_material`
--

CREATE TABLE `appgestioninv_material` (
  `id` bigint(20) NOT NULL,
  `matReferencia` longtext DEFAULT NULL,
  `matMarca` varchar(50) DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `matElemento_id` bigint(20) NOT NULL,
  `matUnidadMedida_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_proveedor`
--

CREATE TABLE `appgestioninv_proveedor` (
  `id` bigint(20) NOT NULL,
  `proTipo` varchar(16) NOT NULL,
  `proIdentificacion` varchar(45) NOT NULL,
  `proNombre` varchar(45) NOT NULL,
  `proRepresentanteLegal` varchar(60) DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_salidadetallesolicitud`
--

CREATE TABLE `appgestioninv_salidadetallesolicitud` (
  `id` bigint(20) NOT NULL,
  `salCantidadEntregada` int(11) NOT NULL,
  `salObservaciones` longtext DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `salDetalleSolicitud_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_solicitudelemento`
--

CREATE TABLE `appgestioninv_solicitudelemento` (
  `id` bigint(20) NOT NULL,
  `solProyecto` varchar(500) NOT NULL,
  `solFechaHoraRequerida` datetime(6) DEFAULT NULL,
  `solEstado` varchar(10) NOT NULL,
  `solObservaciones` longtext DEFAULT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `solFicha_id` bigint(20) NOT NULL,
  `solUsuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_ubicacionfisica`
--

CREATE TABLE `appgestioninv_ubicacionfisica` (
  `id` bigint(20) NOT NULL,
  `ubiDeposito` int(11) NOT NULL,
  `ubiEstante` int(11) DEFAULT NULL,
  `ubiEntrepano` int(11) DEFAULT NULL,
  `ubiLocker` smallint(6) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL,
  `ubiElemento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_unidadmedida`
--

CREATE TABLE `appgestioninv_unidadmedida` (
  `id` bigint(20) NOT NULL,
  `uniNombre` varchar(45) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_user`
--

CREATE TABLE `appgestioninv_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `userFoto` varchar(100) DEFAULT NULL,
  `userTipo` varchar(15) NOT NULL,
  `fechaHoraCreacion` datetime(6) NOT NULL,
  `FechaHoraActualizacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `appgestioninv_user`
--

INSERT INTO `appgestioninv_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `userFoto`, `userTipo`, `fechaHoraCreacion`, `FechaHoraActualizacion`) VALUES
(1, 'pbkdf2_sha256$600000$QH9cZMItK96WchUZKRNdot$gygpIuNNlIpO4NbLxkLJneeGnZWLR0QMhO5+iIHew9c=', NULL, 1, 'admin', '', '', 'dajun318@gmail.com', 1, 1, '2023-05-04 16:43:51.902909', '', '', '2023-05-04 16:43:52.185160', '2023-05-04 16:43:52.185160');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_user_groups`
--

CREATE TABLE `appgestioninv_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appgestioninv_user_user_permissions`
--

CREATE TABLE `appgestioninv_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-04 15:49:25.072007'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-05-04 16:40:31.271201'),
(3, 'auth', '0001_initial', '2023-05-04 16:40:31.470230'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-05-04 16:40:31.509234'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-05-04 16:40:31.513235'),
(6, 'auth', '0004_alter_user_username_opts', '2023-05-04 16:40:31.518237'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-05-04 16:40:31.522748'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-05-04 16:40:31.524749'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-05-04 16:40:31.529745'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-05-04 16:40:31.533747'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-05-04 16:40:31.537748'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-05-04 16:40:31.588746'),
(13, 'auth', '0011_update_proxy_permissions', '2023-05-04 16:40:31.593748'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-05-04 16:40:31.598748'),
(15, 'appGestionInv', '0001_initial', '2023-05-04 16:40:32.815051');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `appgestioninv_detalleentradamateriales`
--
ALTER TABLE `appgestioninv_detalleentradamateriales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_detall_detEntradaMaterial_i_cfd3ca0b_fk_appGestio` (`detEntradaMaterial_id`),
  ADD KEY `appGestionInv_detall_detMaterial_id_fde3dc0f_fk_appGestio` (`detMaterial_id`);

--
-- Indices de la tabla `appgestioninv_detallesolicuitud`
--
ALTER TABLE `appgestioninv_detallesolicuitud`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_detall_detElemento_id_804ce212_fk_appGestio` (`detElemento_id`),
  ADD KEY `appGestionInv_detall_detSolicitud_id_f70be717_fk_appGestio` (`detSolicitud_id`),
  ADD KEY `appGestionInv_detall_detUnidadMedida_id_88c5d76a_fk_appGestio` (`detUnidadMedida_id`);

--
-- Indices de la tabla `appgestioninv_devolucionelemento`
--
ALTER TABLE `appgestioninv_devolucionelemento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_devolu_devSalida_id_eb10623e_fk_appGestio` (`devSalida_id`),
  ADD KEY `appGestionInv_devolu_devUsuario_id_b8ff4cde_fk_appGestio` (`devUsuario_id`);

--
-- Indices de la tabla `appgestioninv_devolutivo`
--
ALTER TABLE `appgestioninv_devolutivo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_devolu_devElemento_id_f2b07d37_fk_appGestio` (`devElemento_id`);

--
-- Indices de la tabla `appgestioninv_elemento`
--
ALTER TABLE `appgestioninv_elemento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `eleCodigo` (`eleCodigo`);

--
-- Indices de la tabla `appgestioninv_entradamaterial`
--
ALTER TABLE `appgestioninv_entradamaterial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_entrad_entProveedor_id_f7914bc1_fk_appGestio` (`entProveedor_id`),
  ADD KEY `appGestionInv_entrad_entUsuarioRecibe_id_fb3d00d1_fk_appGestio` (`entUsuarioRecibe_id`);

--
-- Indices de la tabla `appgestioninv_estadomantenimiento`
--
ALTER TABLE `appgestioninv_estadomantenimiento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `estNombre` (`estNombre`);

--
-- Indices de la tabla `appgestioninv_ficha`
--
ALTER TABLE `appgestioninv_ficha`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ficCodigo` (`ficCodigo`);

--
-- Indices de la tabla `appgestioninv_mantenimientos`
--
ALTER TABLE `appgestioninv_mantenimientos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_manten_manElemento_id_3944d412_fk_appGestio` (`manElemento_id`),
  ADD KEY `appGestionInv_manten_manEstado_id_ef9c8d15_fk_appGestio` (`manEstado_id`),
  ADD KEY `appGestionInv_manten_manPersona_id_2b7f0bb3_fk_appGestio` (`manPersona_id`);

--
-- Indices de la tabla `appgestioninv_material`
--
ALTER TABLE `appgestioninv_material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_materi_matElemento_id_4994ab2b_fk_appGestio` (`matElemento_id`),
  ADD KEY `appGestionInv_materi_matUnidadMedida_id_2375a07e_fk_appGestio` (`matUnidadMedida_id`);

--
-- Indices de la tabla `appgestioninv_proveedor`
--
ALTER TABLE `appgestioninv_proveedor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `proIdentificacion` (`proIdentificacion`);

--
-- Indices de la tabla `appgestioninv_salidadetallesolicitud`
--
ALTER TABLE `appgestioninv_salidadetallesolicitud`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_salida_salDetalleSolicitud__71612176_fk_appGestio` (`salDetalleSolicitud_id`);

--
-- Indices de la tabla `appgestioninv_solicitudelemento`
--
ALTER TABLE `appgestioninv_solicitudelemento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_solici_solFicha_id_9eaf3e9e_fk_appGestio` (`solFicha_id`),
  ADD KEY `appGestionInv_solici_solUsuario_id_32c51367_fk_appGestio` (`solUsuario_id`);

--
-- Indices de la tabla `appgestioninv_ubicacionfisica`
--
ALTER TABLE `appgestioninv_ubicacionfisica`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appGestionInv_ubicac_ubiElemento_id_98aa41fd_fk_appGestio` (`ubiElemento_id`);

--
-- Indices de la tabla `appgestioninv_unidadmedida`
--
ALTER TABLE `appgestioninv_unidadmedida`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uniNombre` (`uniNombre`);

--
-- Indices de la tabla `appgestioninv_user`
--
ALTER TABLE `appgestioninv_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `appgestioninv_user_groups`
--
ALTER TABLE `appgestioninv_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `appGestionInv_user_groups_user_id_group_id_2402f77b_uniq` (`user_id`,`group_id`),
  ADD KEY `appGestionInv_user_groups_group_id_b204558f_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `appgestioninv_user_user_permissions`
--
ALTER TABLE `appgestioninv_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `appGestionInv_user_user__user_id_permission_id_3f3e3ae3_uniq` (`user_id`,`permission_id`),
  ADD KEY `appGestionInv_user_u_permission_id_18b62015_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `appgestioninv_detalleentradamateriales`
--
ALTER TABLE `appgestioninv_detalleentradamateriales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_detallesolicuitud`
--
ALTER TABLE `appgestioninv_detallesolicuitud`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_devolucionelemento`
--
ALTER TABLE `appgestioninv_devolucionelemento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_devolutivo`
--
ALTER TABLE `appgestioninv_devolutivo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_elemento`
--
ALTER TABLE `appgestioninv_elemento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_entradamaterial`
--
ALTER TABLE `appgestioninv_entradamaterial`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_estadomantenimiento`
--
ALTER TABLE `appgestioninv_estadomantenimiento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_ficha`
--
ALTER TABLE `appgestioninv_ficha`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_mantenimientos`
--
ALTER TABLE `appgestioninv_mantenimientos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_material`
--
ALTER TABLE `appgestioninv_material`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_proveedor`
--
ALTER TABLE `appgestioninv_proveedor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_salidadetallesolicitud`
--
ALTER TABLE `appgestioninv_salidadetallesolicitud`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_solicitudelemento`
--
ALTER TABLE `appgestioninv_solicitudelemento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_ubicacionfisica`
--
ALTER TABLE `appgestioninv_ubicacionfisica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_unidadmedida`
--
ALTER TABLE `appgestioninv_unidadmedida`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_user`
--
ALTER TABLE `appgestioninv_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_user_groups`
--
ALTER TABLE `appgestioninv_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `appgestioninv_user_user_permissions`
--
ALTER TABLE `appgestioninv_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `appgestioninv_detalleentradamateriales`
--
ALTER TABLE `appgestioninv_detalleentradamateriales`
  ADD CONSTRAINT `appGestionInv_detall_detEntradaMaterial_i_cfd3ca0b_fk_appGestio` FOREIGN KEY (`detEntradaMaterial_id`) REFERENCES `appgestioninv_entradamaterial` (`id`),
  ADD CONSTRAINT `appGestionInv_detall_detMaterial_id_fde3dc0f_fk_appGestio` FOREIGN KEY (`detMaterial_id`) REFERENCES `appgestioninv_material` (`id`);

--
-- Filtros para la tabla `appgestioninv_detallesolicuitud`
--
ALTER TABLE `appgestioninv_detallesolicuitud`
  ADD CONSTRAINT `appGestionInv_detall_detElemento_id_804ce212_fk_appGestio` FOREIGN KEY (`detElemento_id`) REFERENCES `appgestioninv_elemento` (`id`),
  ADD CONSTRAINT `appGestionInv_detall_detSolicitud_id_f70be717_fk_appGestio` FOREIGN KEY (`detSolicitud_id`) REFERENCES `appgestioninv_solicitudelemento` (`id`),
  ADD CONSTRAINT `appGestionInv_detall_detUnidadMedida_id_88c5d76a_fk_appGestio` FOREIGN KEY (`detUnidadMedida_id`) REFERENCES `appgestioninv_unidadmedida` (`id`);

--
-- Filtros para la tabla `appgestioninv_devolucionelemento`
--
ALTER TABLE `appgestioninv_devolucionelemento`
  ADD CONSTRAINT `appGestionInv_devolu_devSalida_id_eb10623e_fk_appGestio` FOREIGN KEY (`devSalida_id`) REFERENCES `appgestioninv_salidadetallesolicitud` (`id`),
  ADD CONSTRAINT `appGestionInv_devolu_devUsuario_id_b8ff4cde_fk_appGestio` FOREIGN KEY (`devUsuario_id`) REFERENCES `appgestioninv_user` (`id`);

--
-- Filtros para la tabla `appgestioninv_devolutivo`
--
ALTER TABLE `appgestioninv_devolutivo`
  ADD CONSTRAINT `appGestionInv_devolu_devElemento_id_f2b07d37_fk_appGestio` FOREIGN KEY (`devElemento_id`) REFERENCES `appgestioninv_elemento` (`id`);

--
-- Filtros para la tabla `appgestioninv_entradamaterial`
--
ALTER TABLE `appgestioninv_entradamaterial`
  ADD CONSTRAINT `appGestionInv_entrad_entProveedor_id_f7914bc1_fk_appGestio` FOREIGN KEY (`entProveedor_id`) REFERENCES `appgestioninv_proveedor` (`id`),
  ADD CONSTRAINT `appGestionInv_entrad_entUsuarioRecibe_id_fb3d00d1_fk_appGestio` FOREIGN KEY (`entUsuarioRecibe_id`) REFERENCES `appgestioninv_user` (`id`);

--
-- Filtros para la tabla `appgestioninv_mantenimientos`
--
ALTER TABLE `appgestioninv_mantenimientos`
  ADD CONSTRAINT `appGestionInv_manten_manElemento_id_3944d412_fk_appGestio` FOREIGN KEY (`manElemento_id`) REFERENCES `appgestioninv_elemento` (`id`),
  ADD CONSTRAINT `appGestionInv_manten_manEstado_id_ef9c8d15_fk_appGestio` FOREIGN KEY (`manEstado_id`) REFERENCES `appgestioninv_estadomantenimiento` (`id`),
  ADD CONSTRAINT `appGestionInv_manten_manPersona_id_2b7f0bb3_fk_appGestio` FOREIGN KEY (`manPersona_id`) REFERENCES `appgestioninv_user` (`id`);

--
-- Filtros para la tabla `appgestioninv_material`
--
ALTER TABLE `appgestioninv_material`
  ADD CONSTRAINT `appGestionInv_materi_matElemento_id_4994ab2b_fk_appGestio` FOREIGN KEY (`matElemento_id`) REFERENCES `appgestioninv_elemento` (`id`),
  ADD CONSTRAINT `appGestionInv_materi_matUnidadMedida_id_2375a07e_fk_appGestio` FOREIGN KEY (`matUnidadMedida_id`) REFERENCES `appgestioninv_unidadmedida` (`id`);

--
-- Filtros para la tabla `appgestioninv_salidadetallesolicitud`
--
ALTER TABLE `appgestioninv_salidadetallesolicitud`
  ADD CONSTRAINT `appGestionInv_salida_salDetalleSolicitud__71612176_fk_appGestio` FOREIGN KEY (`salDetalleSolicitud_id`) REFERENCES `appgestioninv_detallesolicuitud` (`id`);

--
-- Filtros para la tabla `appgestioninv_solicitudelemento`
--
ALTER TABLE `appgestioninv_solicitudelemento`
  ADD CONSTRAINT `appGestionInv_solici_solFicha_id_9eaf3e9e_fk_appGestio` FOREIGN KEY (`solFicha_id`) REFERENCES `appgestioninv_ficha` (`id`),
  ADD CONSTRAINT `appGestionInv_solici_solUsuario_id_32c51367_fk_appGestio` FOREIGN KEY (`solUsuario_id`) REFERENCES `appgestioninv_user` (`id`);

--
-- Filtros para la tabla `appgestioninv_ubicacionfisica`
--
ALTER TABLE `appgestioninv_ubicacionfisica`
  ADD CONSTRAINT `appGestionInv_ubicac_ubiElemento_id_98aa41fd_fk_appGestio` FOREIGN KEY (`ubiElemento_id`) REFERENCES `appgestioninv_elemento` (`id`);

--
-- Filtros para la tabla `appgestioninv_user_groups`
--
ALTER TABLE `appgestioninv_user_groups`
  ADD CONSTRAINT `appGestionInv_user_g_user_id_d45e56c2_fk_appGestio` FOREIGN KEY (`user_id`) REFERENCES `appgestioninv_user` (`id`),
  ADD CONSTRAINT `appGestionInv_user_groups_group_id_b204558f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `appgestioninv_user_user_permissions`
--
ALTER TABLE `appgestioninv_user_user_permissions`
  ADD CONSTRAINT `appGestionInv_user_u_permission_id_18b62015_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `appGestionInv_user_u_user_id_095dc508_fk_appGestio` FOREIGN KEY (`user_id`) REFERENCES `appgestioninv_user` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
