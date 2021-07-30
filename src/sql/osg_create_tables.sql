/* STEP 1. DROP THE EXISTING ADDRESSBASE PREMIUM SCHEMA (OSG)*/
--DROP SCHEMA IF EXISTS OSG CASCADE;

/* STEP 2. CREATE THE ADDRESS BASE PREMIUM SCHEMA (ABP) */
--CREATE SCHEMA IF NOT EXISTS OSG AUTHORIZATION "SISedit";

/* 
Create tables from individual table definition.
Schema should have been selected in prior command using SET search_path = xxxx
 */

\i src/sql/create_tables/10.sql;
\i src/sql/create_tables/11.sql;
\i src/sql/create_tables/13.sql;
\i src/sql/create_tables/15.sql;
\i src/sql/create_tables/12.sql;
\i src/sql/create_tables/21.sql;
\i src/sql/create_tables/22.sql;
\i src/sql/create_tables/23.sql;
\i src/sql/create_tables/24.sql;
\i src/sql/create_tables/29.sql;
\i src/sql/create_tables/30.sql;
\i src/sql/create_tables/31.sql;
\i src/sql/create_tables/32.sql;
\i src/sql/create_tables/99.sql;
