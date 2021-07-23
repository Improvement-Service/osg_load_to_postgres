/* STEP 1. DROP THE EXISTING ADDRESSBASE PREMIUM SCHEMA (OSG)*/
DROP SCHEMA IF EXISTS osg CASCADE;

/* STEP 2. CREATE THE ADDRESS BASE PREMIUM SCHEMA (ABP) */
CREATE SCHEMA IF NOT EXISTS OSG AUTHORIZATION "SISedit";

/* STEP 3. SET THE SEARCH PATH TO INCLUDE THE ABP SCHEMA SO POSTGIS / POSTGRES FUNCTIONS AND SQL CAN BE USED */
SET search_path TO osg,public;

\i create_tables/10.sql;
\i create_tables/11.sql;
\i create_tables/12.sql;
\i create_tables/13.sql;
\i create_tables/15.sql;
\i create_tables/29.sql;
\i create_tables/51.sql;
\i create_tables/52.sql;
\i create_tables/53.sql;
\i create_tables/99.sql;
