/* STEP 1. DROP THE EXISTING ADDRESSBASE PREMIUM SCHEMA (OSG)*/
--DROP SCHEMA IF EXISTS OSG CASCADE;

/* STEP 2. CREATE THE ADDRESS BASE PREMIUM SCHEMA (ABP) */
--CREATE SCHEMA IF NOT EXISTS OSG AUTHORIZATION "SISedit";

/* 
Create tables from individual table definition.
Schema should have been selected in prior command using SET search_path = xxxx
 */

\i sdtf_load/sql/create_tables/10.sql;
\i sdtf_load/sql/create_tables/11.sql;
\i sdtf_load/sql/create_tables/13.sql;
\i sdtf_load/sql/create_tables/15.sql;
\i sdtf_load/sql/create_tables/12.sql;
\i sdtf_load/sql/create_tables/21.sql;
\i sdtf_load/sql/create_tables/22.sql;
\i sdtf_load/sql/create_tables/23.sql;
\i sdtf_load/sql/create_tables/24.sql;
\i sdtf_load/sql/create_tables/29.sql;
\i sdtf_load/sql/create_tables/30.sql;
\i sdtf_load/sql/create_tables/31.sql;
\i sdtf_load/sql/create_tables/32.sql;
\i sdtf_load/sql/create_tables/99.sql;
