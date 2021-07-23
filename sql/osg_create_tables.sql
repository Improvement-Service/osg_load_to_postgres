/* STEP 1. DROP THE EXISTING ADDRESSBASE PREMIUM SCHEMA (OSG)*/
--DROP SCHEMA IF EXISTS OSG CASCADE;

/* STEP 2. CREATE THE ADDRESS BASE PREMIUM SCHEMA (ABP) */
--CREATE SCHEMA IF NOT EXISTS OSG AUTHORIZATION "SISedit";

/* STEP 3. SET THE SEARCH PATH TO INCLUDE THE ABP SCHEMA SO POSTGIS / POSTGRES FUNCTIONS AND SQL CAN BE USED */
--SET search_path TO osg;

\i sql/create_tables/10.sql;
\i sql/create_tables/11.sql;
\i sql/create_tables/13.sql;
\i sql/create_tables/15.sql;
\i sql/create_tables/12.sql;
\i sql/create_tables/21.sql;
\i sql/create_tables/22.sql;
\i sql/create_tables/23.sql;
\i sql/create_tables/24.sql;
\i sql/create_tables/29.sql;
\i sql/create_tables/30.sql;
\i sql/create_tables/31.sql;
\i sql/create_tables/32.sql;
\i sql/create_tables/99.sql;
